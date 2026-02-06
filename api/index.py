from flask import Flask, render_template_string, request, jsonify
import base64

app = Flask(__name__)

# [SOVEREIGN KEY CONFIGURATION]
# تم اعتماد المفتاح الجديد MohEdwa2026 كأعلى سلطة وصول [cite: 2026-02-06]
EXECUTIVE_KEY = 'MohEdwa2026'
AUDIT_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING' # للمعاينة فقط [cite: 2026-02-04]

class ImperialGeneralCore:
    def __init__(self):
        self.modules = {f"P{i}": self._get_module_desc(i) for i in range(1, 71)}

    def _get_module_desc(self, i):
        if i == 1: return "Whale Financial Stream / رصد تدفقات الحيتان" [cite: 2026-02-01]
        if i == 70: return "Imperial Sovereignty / السيادة الإمبراطورية المطلقة"
        return f"Advanced Strategic Module P{i}"

    def process_request(self, code, payload):
        try:
            decoded_key = base64.b64decode(payload).decode('utf-8')
            # مستوى الوصول التنفيذي (Full Power)
            if decoded_input == EXECUTIVE_KEY:
                return {"msg": f"AUTHORIZED: {self.modules.get(code)} ACTIVE", "status": "GOD_MODE"}
            # مستوى الوصول للاطلاع (Audit Mode)
            elif decoded_input == AUDIT_KEY:
                return {"msg": "READ-ONLY ACCESS: Sovereign Protocol Restricted.", "status": "INSPECTION"}
            return {"msg": "BREACH DETECTED: ACCESS DENIED", "status": "TERMINATED"}, 403
        except:
            return {"msg": "ENCRYPTION ERROR", "status": "FAIL"}, 400

# [API ROUTES]
@app.route('/api/general')
def general_api():
    core = ImperialGeneralCore()
    return jsonify(core.process_request(request.args.get('code'), request.args.get('payload')))

app = app # الإصلاح النهائي لبيئة Vercel
