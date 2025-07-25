
# Troubleshooting Guide: Real-Time Security Alert Pipeline

This document highlights the key issues I encountered while building the SOC pipeline project, including errors from Kibana, Docker, Python scripts, and terminal setup. It also includes the hands-on steps I took to fix them and get the system fully working.

---

## 1. Kibana Not Showing Logs

**Issue:**  
Kibana Discover panel showed no logs even though logs were being generated.

**Cause:**  
Missing or incorrect index pattern.

**Fix:**
- Navigated to **Stack Management > Index Patterns**
- Created index pattern: `security-logs*`
- Selected `@timestamp` as the time field
- Refreshed fields

---

## 2. Flask Server Not Receiving Alerts

**Issue:**  
Alerts from Logstash were not hitting the Flask webhook.

**Cause:**  
- Flask server wasn't running  
- Incorrect Logstash output config

**Fix:**
- Started Flask server with: `python3 webhook_server.py`
- Updated Logstash output section:

```ruby
if [alert] == true {
  http {
    url => "http://localhost:5000/alert"
    http_method => "post"
    format => "json"
    content_type => "application/json"
  }
}
````

* Added `print()` statements in `webhook_server.py` to verify receipt.

---

## 3. Terminal Command Issues

**Issue:**
Running the Python script caused `No such file or directory`.

**Fix:**

* Ensured I was in the correct directory using `cd`
* Verified filename: `python3 log_generator.py`

---

## 4. Python Script Not Sending Logs Correctly

**Issue:**
Log entries were malformed or not reaching Logstash.

**Fix:**

* Used `json.dumps()` to create valid JSON
* Added error handling:

```python
try:
    s.sendto(log.encode(), (LOGSTASH_HOST, LOGSTASH_PORT))
except Exception as e:
    print("Error sending log:", e)
```

* Added a `time.sleep(0.1)` delay to prevent buffer overflows

---

## 5. Elasticsearch Container Failing (Docker)

**Issue:**
Elasticsearch wouldn’t start properly after a reboot.

**Cause:**
Volume issues or permissions error.

**Fix:**

* Stopped containers: `docker-compose down`
* Removed volumes: `docker volume prune`
* Rebuilt: `docker-compose up --build`
* Verified services: `docker ps`

---

## 6. Kibana Visualizations Showing "Other"

**Issue:**
Visualizations grouped most values into “Other”.

**Fix:**

* Increased top values from 5 to 10+
* Used `.keyword` fields (`src_ip.keyword`, `event_type.keyword`)
* Sorted by descending document count

---

## 7. Missing Fields in Discover Tab

**Issue:**
Fields like `alert`, `host`, or `event_type` weren’t visible.

**Fix:**

* Refreshed index pattern fields in Kibana
* Confirmed those fields exist in the source
* Used `.keyword` versions where needed

---

## 8. Dashboard Not Updating in Real-Time

**Issue:**
Kibana panels remained static or delayed.

**Fix:**

* Set dashboard time filter to “Last 15 minutes”
* Enabled auto-refresh every 10 seconds
* Used `@timestamp` on X-axis for visualizations

---

## 9. Limited Log Count in Elasticsearch

**Issue:**
Log count stuck at 14 despite active generation.

**Fix:**

* Verified Logstash was running and receiving data
* Restarted Logstash pipeline
* Confirmed log flow with:

```bash
curl http://localhost:9200/security-logs/_count?pretty
```

* Count increased after restarting everything cleanly

---

## 10. Final Clean Restart That Solved Everything

**Steps Taken:**

1. Stopped all containers
2. Cleared `.lock` files (if any)
3. Reran entire setup:

```bash
docker-compose up --build
python3 webhook_server.py
python3 log_generator.py
```

4. Checked health at `http://localhost:9200`
5. Verified logs in Kibana Discover tab

---

## Summary

These issues tested my ability to troubleshoot and debug a full-stack log pipeline. I learned how to:

* Resolve real-time pipeline issues
* Interact with Elasticsearch and Kibana directly
* Work with Docker and persistent volumes
* Handle Python socket and connection errors
* Tune Logstash and dashboard settings for production-level realism

This experience gave me a clear understanding of how to build, monitor, and fix a security alert pipeline like those used in real SOC environments.
