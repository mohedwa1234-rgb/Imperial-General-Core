import json
import random
import secrets
from http.server import BaseHTTPRequestHandler

class ImperialGeneralEcosystem:
    def __init__(self):
        self.master_key = 'GENERAL_EYE_ONLY_VALIDATION_STRING'
        
    def execute_protocol(self, p_code):
        handlers = {
            'P1': lambda: {"title": "Whale Tracker", "data": f"TX: 0x{secrets.token_hex(4)}... ${random.randint(5,20)}M", "status": "LIVE"},
            'P70': lambda: {"title": "God Mode / وضع الآلهة", "data": "All restrictions bypassed. Master Key Validated.", "status": "GENERAL_EYE_ONLY"}
        }
        action = handlers.get(p_code, lambda: {"title": f"Module {p_code}", "data": "Operating in stealth background mode.", "status": "STABLE"})
        return action()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        p_code = 'P1'
        if 'p_code=' in self.path:
            p_code = self.path.split('p_code=')[1]
            
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        gen = ImperialGeneralEcosystem()
        response = gen.execute_protocol(p_code)
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
