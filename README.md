# Real-Time Security Alert Pipeline

This project simulates how a real-world Security Operations Center (SOC) detects and responds to suspicious activity in real time.

It includes a Python log generator, Logstash pipeline, Flask alert receiver, and visualization using Kibana. It's designed to show how different tools can work together to automate security monitoring and incident response.

---

## What This Project Does

- Simulates common security events (e.g. failed logins, malware execution, port scans)
- Filters and analyzes those logs using Logstash
- Sends critical alerts to a Flask webhook in real time
- Visualizes logs using Kibana for monitoring and analysis

This setup is useful for learning about log pipelines, automation in security operations, and alerting systems.

---

## Tools Used

- **Python** – to simulate security logs
- **Logstash** – for log ingestion and filtering
- **Flask** – to receive alerts via HTTP
- **Elasticsearch + Kibana** – for storing and visualizing logs
- **Docker (optional)** – for easy deployment of the ELK stack

---

## Why I Built This

I wanted to understand how security teams handle logs and detect threats. Instead of reading about it, I built it myself.

This helped me learn how to:
- Stream logs over TCP
- Use conditional logic in Logstash to detect specific events
- Receive and respond to alerts with a webhook
- Visualize activity using real dashboards
- Work with real-time data flows

It was also a good opportunity to work with production tools like Elasticsearch, Kibana, and Docker.

---

## How It Works

1. **The Python script** (`log_generator.py`) generates log events with random IPs, usernames, and event types.
2. **Logstash** listens on a TCP port, filters the logs, and checks if an event should be flagged as an alert (like "malware_execution").
3. If an alert is found, **Logstash sends it via HTTP POST** to the **Flask server** (`webhook_server.py`), which receives and logs the alert.
4. All logs (including alerts) are forwarded to **Elasticsearch**, where they can be explored and visualized in **Kibana**.

---

## How to Run This Project

### Step 1: Set up Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
