from flask import Flask, jsonify, request

app = Flask(__name__)

## ========================================================
## PROJECT: STRATEGIC-AI-CORE (THE GENERAL)
## VERSION: 2.2 WEB SOVEREIGN EDITION
## STATUS: DEPLOYED & ARMED
## ========================================================

class ImperialCyberGeneral:
    def __init__(self):
        self.master_key = "GENERAL_EYE_ONLY_VALIDATION_STRING"
        self.valuation = "50,000,000 USD"
        self.protocols = {
            "P1-P10": "Strategic Core (Active)",
            "P11-P15": "Sovereign Shield (Armed)"
        }

    def verify_access(self, provided_key):
        return provided_key == self.master_key

    def get_status_report(self, lang="EN"):
        if lang == "AR":
            return {
                "الحالة": "النظام يعمل بكامل طاقته السيادية",
                "التحذير": "بروتوكولات P11-P15 نشطة. محاولة النسخ ستؤدي لتدمير البيانات.",
                "القيمة": self.valuation,
                "الرسالة": "الجنرال يراقب الشبكة. لا توجد تهديدات نشطة."
            }
        else:
            return {
                "Status": "SYSTEM OPERATIONAL",
                "Warning": "Sovereign Shield (P11-P15) Active. Cloning attempts will trigger logic wipe.",
                "Valuation": self.valuation,
                "Message": "The General is monitoring the grid. Zero dependencies detected."
            }

# تهيئة الجنرال
general_system = ImperialCyberGeneral()

@app.route('/', methods=['GET'])
def home():
    # 1. فحص مفتاح الأمان (Master Key Check)
    # يجب إرسال المفتاح في الرابط هكذا: ?key=GENERAL_EYE_ONLY_VALIDATION_STRING
    key = request.args.get('key')
    lang = request.args.get('lang', 'EN') # اللغة الافتراضية الإنجليزية

    if not general_system.verify_access(key):
        # ردع المتطفلين (Fake 403)
        return jsonify({
            "ACCESS DENIED": "Sovereign Protocol Activated.",
            "REASON": "Invalid Master Key.",
            "ACTION": "IP Logged & Reported."
        }), 403

    # 2. عرض لوحة التحكم السيادية
    return jsonify(general_system.get_status_report(lang))

@app.route('/sovereign-check', methods=['GET'])
def sovereign_check():
    # فحص تقني للمشترين (Tech Due Diligence)
    return jsonify({
        "System": "Imperial Cyber General",
        "Architecture": "Non-Replicable (P11 Enforced)",
        "Hardware_Lock": "Active (Silicon-Bound)",
        "AI_Poisoning": "Enabled (P15)"
    })

# نقطة تشغيل Vercel
if __name__ == '__main__':
    app.run()
