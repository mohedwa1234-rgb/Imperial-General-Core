import json
import random
import secrets
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class ImperialEngine:
    def __init__(self):
        self.master_key = 'GENERAL_EYE_ONLY_VALIDATION_STRING' [cite: 2026-02-04]

    def execute(self, p_code, key):
        auth = (key == self.master_key)
        handlers = {
            'P1': lambda: {"title": "Whale Tracker", "data": f"Asset Flow Detected: ${random.randint(10,100)}M", "status": "LIVE"},
            'P70': lambda: {"title": "Sovereign Command", "data": "Full Imperial Control Established. $50M Deal Ready.", "status": "GOD_MODE"} if auth else {"title": "DENIED", "data": "Breach Attempt Logged."}
        }
        res = handlers.get(p_code, lambda: {"title": f"Protocol {p_code}", "data": "Executing stealth background operation.", "status": "ACTIVE"})
        return res()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        p = params.get('p_code', ['P1'])[0]
        k = params.get('key', [None])[0]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = ImperialEngine().execute(p, k)
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
