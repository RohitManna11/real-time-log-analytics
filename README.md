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

### Step 1: Clone the Repository

```bash
git clone https://github.com/RohitManna11/real-time-log-analytics.git
cd real-time-log-analytics
