"""
main.py - Entry point for the Multi-Agent AI Platform
Starts the Flask server that exposes agent endpoints to the
Spring Boot backend.
"""

import sys
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
# Add both orchestrator and its parent workspace directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from flask import Flask  # noqa: E402
from flask_cors import CORS  # noqa: E402
from orchestrator.routes import register_routes  # noqa: E402

app = Flask(__name__)
CORS(app)  # Allow requests from Spring Boot backend

# Register all API routes
register_routes(app)

if __name__ == "__main__":
    print("🤖 Multi-Agent Platform is starting...")
    print("📡 Listening on http://localhost:5000")
    # Disable debug mode to prevent WinError 10038 crashes on Windows
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
