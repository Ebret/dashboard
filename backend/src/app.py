import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

try:
    from collections import Iterable
except ImportError:
    collections.Iterable = collections.abc.Iterable

try:
    from collections import Mapping
except ImportError:
    collections.Mapping = collections.abc.Mapping

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
import graphene
import oracledb

# Database connection details (replace with your actual details or environment variables)
DB_USER = "scott"
DB_PASSWORD = "tiger"
DB_DSN = "123.2.2.31:1521/ECL21"

class Data(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))
    all_data = graphene.List(Data)

    def resolve_hello(self, info, name):
        return f"Hello {name}"

    def resolve_all_data(self, info):
        try:
            with oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN) as connection:
                with connection.cursor() as cursor:
                    # Example: Fetch data from a table named 'YOUR_TABLE'
                    # Replace 'YOUR_TABLE' and column names with your actual table and columns
                    cursor.execute("SELECT id, name FROM YOUR_TABLE")
                    rows = cursor.fetchall()
                    return [Data(id=row[0], name=row[1]) for row in rows]
        except Exception as e:
            print(f"Error connecting to Oracle DB or fetching data: {e}")
            return []

schema = graphene.Schema(query=Query)

app = Flask(__name__)
CORS(app)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface for testing
    )
)

if __name__ == '__main__':
    app.run(debug=True)