from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)
# test test test
@app.route("/")
def home():
    return {
        "message": "Hello from DevOps project!",
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": os.uname().nodename
    }

@app.route("/health")
def health():
    return {
        "status": "OK"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
