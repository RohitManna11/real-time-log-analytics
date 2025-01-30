# Real-Time Log Analytics

This project implements a real-time log analytics system using **Prometheus**, **Grafana**, **Elasticsearch**, **Kibana**, and **cAdvisor**. It is designed to monitor containerized applications, visualize logs and metrics, and provide real-time insights for system performance and anomaly detection.

## Features

- **System Monitoring**: Collect container metrics like CPU, memory, disk, and network usage using cAdvisor and Prometheus.
- **Visualization**: Create interactive dashboards for metrics and logs with Grafana and Kibana.
- **Real-Time Alerts**: Configure alerts in Prometheus to notify on critical system thresholds.
- **Scalability**: Modular setup to add more containers or data sources.

---

## Project Setup

### Prerequisites

1. Docker and Docker Compose installed.
2. A Linux-based system (recommended: Ubuntu).
3. Internet access for downloading required images.
---
### Step 1: Clone the Repository

```bash
git clone https://github.com/RohitManna11/real-time-log-analytics.git
cd real-time-log-analytics
```
---
### Step 2: Start the Services

Run the following command to bring up all the containers:

```bash
docker-compose up -d
```
---

### Step 3: Verify the Setup

- **Prometheus**: Visit [http://localhost:9090](http://localhost:9090) to explore metrics.
- **Grafana**: Visit [http://localhost:3000](http://localhost:3000), default credentials:
  - **Username**: `admin`
  - **Password**: `admin`
- **Kibana**: Visit [http://localhost:5601](http://localhost:5601) for log analysis.
- **cAdvisor**: Visit [http://localhost:8081](http://localhost:8081) to monitor containers.

---
## Directory Structure
```
real-time-log-analytics/
├── docker-compose.yml # Service definitions for Docker
├── prometheus/
├── prometheus.yml # Prometheus configuration
├── grafana/
├── grafana.ini # Grafana configuration
├── dashboards/ # Preconfigured dashboards (JSON) ├── elasticsearch/ │ ├── elasticsearch.yml # Elasticsearch configuration ├── kibana/ │ ├── kibana.yml # Kibana configuration ├── cadvisor/ # Directory for cAdvisor configuration ├── logs/ # Log files (excluded in .gitignore) ├── .gitignore # Files to ignore in version control └── README.md # Project documentation
```
