import socket
import json
import time
import random

LOGSTASH_HOST = '127.0.0.1'
LOGSTASH_PORT = 5050

def generate_log():
    # Your log generation code here
    # Example:
    return {
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
        "src_ip": f"192.168.1.{random.randint(1,254)}",
        "username": random.choice(["admin", "user1", "guest", "root"]),
        "event_type": random.choice(["login_success", "login_failed", "malware_execution", "port_scan_detected", "normal_activity"]),
        "host": f"host-{random.randint(1,10)}"
    }

def send_log(log):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((LOGSTASH_HOST, LOGSTASH_PORT))
    s.sendall((json.dumps(log) + "\n").encode())
    s.close()

while True:
    log = generate_log()
    send_log(log)
    print(f"Sent log: {log}")
    time.sleep(1)

