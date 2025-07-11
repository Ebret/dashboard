# Oracle Dashboard README with deployment, API, and usage info

## 📊 Oracle Dashboard – Dynamic & Upload-Driven Visualization Platform

This project provides a full-stack solution to generate dashboards from Oracle data or uploaded files.

---

## 🔧 Features

### 🖥️ Frontend

* **Grafana UI** with automatic dashboard loading
* **React Dashboard Wizard**: upload file → preview → select columns → choose chart
* File upload support: `.csv`, `.xlsx`

### ⚙️ Backend (FastAPI)

* `/api/upload`: Handles file upload and preview
* `/api/dashboard/generate`: Accepts config, generates JSON, and reloads Grafana
* Oracle DB connectivity using `oracledb` via EZConnect or `tnsnames.ora`

### 📈 Dynamic Dashboard Generator

* Auto-create Grafana dashboard panels from uploaded files
* Panel types supported: Table, Line, Bar
* Support for custom titles, axes, and filters

### 📤 File Upload UI

* Drag-and-drop file upload
* CSV/XLSX preview with selectable columns

### 🤖 GPT-Enhanced Suggestions *(Optional)*

* Natural language → SQL
* SQL explainer panel

### 📦 Dockerized Deployment

* Docker Compose for Grafana, FastAPI, and React
* Ready for local dev or cloud deployment

### 🔐 Security

* JWT-based authentication (configurable via `.env`)
* GitHub Secrets support for CI/CD pipelines
* Role-based access support (Admin, Analyst, Viewer)

---

## 📁 Folder Structure

```
├── backend/
│   └── routes/
│       ├── upload.py
│       └── generate.py
├── frontend/
│   └── components/
│       └── DashboardWizard.tsx
├── config/
│   └── grafana/provisioning/dashboards/
├── uploads/
├── docs/
│   └── Postman/OracleDashboard.postman_collection.json
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

### 🐳 Docker Compose

```bash
git clone https://github.com/Ebret/Oracle-Dashboard.git
cd Oracle-Dashboard
docker-compose up --build
```

### 🌐 Access Interfaces

* **Grafana**: [http://localhost:3088](http://localhost:3088)  (default admin/admin)
* **File Uploader Wizard**: [http://localhost:3000](http://localhost:3000)
* **Backend API**: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Postman Collection

Import from:

```
docs/Postman/OracleDashboard.postman_collection.json
```

Endpoints:

* `POST /api/upload`
* `POST /api/dashboard/generate`

---

## 📘 .env Example

```env
ORACLE_CONN_TYPE=ezconnect
ORACLE_USER=admin
ORACLE_PASSWORD=oracle
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=orclpdb1
JWT_SECRET=mysecret
OPENAI_API_KEY=your_api_key_here
```

---

## 🔄 Grafana Reload (API)

After dashboard JSON is written:

```bash
curl -X POST http://localhost:3088/api/admin/provisioning/dashboards/reload \
  -H "Authorization: Bearer <YOUR_GRAFANA_API_KEY>"
```

This is triggered automatically by the backend.

---

## 📦 Deployment Targets

* 📄 GitHub Pages (for docs/wiki)
* ☁️ Vercel or DockerHub
* 🏢 On-prem or airgapped Oracle DB support

---

## 📌 Next Steps

* ✅ Push to GitHub
* 🔄 CI/CD via GitHub Actions
* ✨ GPT auto-query builder
* 📈 Drag & Drop SQL composer

---

MIT License © 2025 ebret888 / Oracle Dashboard Dev Team
