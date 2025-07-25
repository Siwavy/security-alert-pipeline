from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json
    print(f"\n⚠️  ALERT RECEIVED: {data}\n")
    
    # Simulate action (block IP, send email, etc.)
    if data.get("alert") == "true":
        print(f"🔐 Action: Investigating suspicious event_type = {data.get('event_type')} from {data.get('src_ip')}")
    
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=8080)

