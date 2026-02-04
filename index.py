from flask import Flask, request, render_template_string

app = Flask(__name__)

# المحرك السيادي
GENERAL_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
    "version": "2.2 Sovereign UI"
}

# تصميم الواجهة (HTML/CSS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="{{ 'ar' if lang == 'AR' else 'en' }}" dir="{{ 'rtl' if lang == 'AR' else 'ltr' }}">
<head>
    <meta charset="UTF-8">
    <title>Imperial Cyber General - Sovereign Core</title>
    <style>
        body { background-color: #0a0a0a; color: #e0e0e0; font-family: 'Courier New', Courier, monospace; margin: 0; padding: 20px; text-align: center; }
        .container { border: 2px solid #d4af37; border-radius: 10px; padding: 40px; max-width: 800px; margin: auto; box-shadow: 0 0 20px #d4af37; }
        h1 { color: #d4af37; text-transform: uppercase; letter-spacing: 5px; }
        .valuation { font-size: 3em; color: #ff4d4d; margin: 20px 0; text-shadow: 0 0 10px #ff0000; }
        .protocol-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 30px; text-align: left; }
        .protocol-item { background: #1a1a1a; padding: 10px; border-left: 3px solid #d4af37; font-size: 0.9em; }
        .status-active { color: #00ff00; font-weight: bold; }
        .footer { margin-top: 40px; font-size: 0.8em; color: #555; }
        .alert { color: #ff4d4d; font-weight: bold; border: 1px solid #ff4d4d; padding: 10px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Imperial Cyber General</h1>
        <p>[ {{ "السيادة المطلقة" if lang == "AR" else "TOTAL SOVEREIGNTY" }} ]</p>
        
        <div class="valuation">${{ valuation }} USD</div>
        
        <div class="alert">
            {{ "تنبيه: بروتوكولات P11-P15 نشطة. النظام مرتبطة مادياً بالعتاد." if lang == "AR" else "WARNING: P11-P15 Protocols Active. Hardware-Bound Sovereignty Enforced." }}
        </div>

        <div class="protocol-grid">
            <div class="protocol-item">P1-P10: {{ "النواة الاستراتيجية" if lang == "AR" else "Strategic Core" }} <span class="status-active">ONLINE</span></div>
            <div class="protocol-item">P11: {{ "التعدد الجيني" if lang == "AR" else "Genetic Polymorphism" }} <span class="status-active">ACTIVE</span></div>
            <div class="protocol-item">P12: {{ "الفدية العكسية" if lang == "AR" else "Reverse Ransomware" }} <span class="status-active">ARMED</span></div>
            <div class="protocol-item">P13: {{ "المقاومة الكمية" if lang == "AR" else "Quantum Bridge" }} <span class="status-active">SECURE</span></div>
            <div class="protocol-item">P14: {{ "الارتباط المادي" if lang == "AR" else "Hardware Lock" }} <span class="status-active">LOCKED</span></div>
            <div class="protocol-item">P15: {{ "حماية الملكية" if lang == "AR" else "Anti-AI Poison" }} <span class="status-active">ENFORCED</span></div>
        </div>

        <div class="footer">
            System Version: {{ version }} | Unauthorized access will trigger logic wipe.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    lang = request.args.get('lang', 'EN').upper()

    if key != GENERAL_CONFIG["master_key"]:
        return """<body style="background:black;color:red;display:flex;justify-content:center;align-items:center;height:100vh;font-family:monospace;">
                  <h1>ACCESS DENIED: SOVEREIGN PROTOCOL ACTIVE</h1></body>""", 403

    return render_template_string(
        HTML_TEMPLATE, 
        valuation=GENERAL_CONFIG["valuation"], 
        version=GENERAL_CONFIG["version"],
        lang=lang
    )

if __name__ == '__main__':
    app.run()
