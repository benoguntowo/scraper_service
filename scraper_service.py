from flask import Flask, request, jsonify
from prometheus_client import Counter, start_http_server
import requests
import threading

app = Flask(__name__)

# Define the Prometheus counter metric
http_get_counter = Counter(
    'http_get', 'HTTP GET request status codes',
    ['url', 'code']
)

@app.route('/', methods=['POST'])
def scrape_url():
    data = request.json
    if 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = data['url']
    try:
        response = requests.get(url)
        code = response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

    # Increment the Prometheus counter
    http_get_counter.labels(url=url, code=str(code)).inc()

    return jsonify({"url": url, "code": code}), 200

def start_prometheus_server():
    start_http_server(9095)

if __name__ == '__main__':
    # Start Prometheus server on port 9095 in a separate thread
    threading.Thread(target=start_prometheus_server).start()
    # Start Flask app on port 8787
    app.run(host='0.0.0.0', port=8787)
