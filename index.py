from flask import Flask, request, render_template_string

app = Flask(__name__)

# إعدادات السيادة
CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

# بيانات البروتوكولات باللغتين
PROTOCOLS_DATA = {
    "AR": [
        ("P1", "معالجة البيانات الضخمة"), ("P2", "توليد الأنظمة العابرة للمنصات"),
        ("P3", "التحليل التنبؤي الاستباقي"), ("P4", "صياغة العقود التقنية"),
        ("P5", "منطق كاسر الأدوات"), ("P6", "التدقيق المعماري الهيكلي"),
        ("P7", "نمذجة الشخصيات النفسية"), ("P8", "الأتمتة المنطقية الكاملة"),
        ("P9", "التشفير الخفي المستتر"), ("P10", "خارطة التحسين الذاتي"),
        ("P11", "التعدد الجيني البرمجي"), ("P12", "الفدية العكسية الهجومية"),
        ("P13", "الجسر المقاوم للكم"), ("P14", "الارتباط الفيزيائي بالعتاد"),
        ("P15", "تسميم تدريب الذكاء الاصطناعي")
    ],
    "EN": [
        ("P1", "Big Data Processing"), ("P2", "Cross-Platform Generation"),
        ("P3", "Predictive Analysis"), ("P4", "Technical Drafting"),
        ("P5", "Tool Breaker Logic"), ("P6", "Architectural Audit"),
        ("P7", "Persona Modeling"), ("P8", "Logic Automation"),
        ("P9", "Stealth Encryption"), ("P10", "Self-Optimization"),
        ("P11", "Genetic Mutation"), ("P12", "Reverse Ransomware"),
        ("P13", "Quantum Shield"), ("P14", "Hardware Binding"),
        ("P15", "Anti-AI Poisoning")
    ]
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="{{ 'ar' if lang == 'AR' else 'en' }}" dir="{{ 'rtl' if lang == 'AR' else 'ltr' }}">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL - COMMAND CENTER</title>
    <style>
        body { background-color: #050505; color: #d4af37; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; overflow-x: hidden; }
        .dashboard { padding: 20px; border: 1px solid #d4af37; margin: 10px; position: relative; min-height: 90vh; }
        
        /* زر تبديل اللغة */
        .lang-toggle { position: absolute; top: 20px; left: 20px; background: #d4af37; color: black; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; border-radius: 5px; text-decoration: none; }
        
        /* الرادار النشط */
        .radar-container { width: 120px; height: 120px; border: 2px solid #d4af37; border-radius: 50%; position: relative; margin: 10px auto; overflow: hidden; opacity: 0.8; }
        .radar-sweep { width: 100%; height: 100%; background: conic-gradient(from 0deg, transparent, rgba(212, 175, 55, 0.4)); animation: sweep 3s linear infinite; border-radius: 50%; }
        @keyframes sweep { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        
        h1 { text-align: center; letter-spacing: 5px; color: #d4af37; text-shadow: 0 0 10px #d4af37; margin-top: 40px; }
        .valuation { text-align: center; font-size: 3em; color: #ff4d4d; font-weight: bold; margin: 10px 0; text-shadow: 0 0 15px #ff0000; }
        
        .protocol-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 20px; }
        .protocol-card { background: rgba(20, 20, 20, 0.9); border: 1px solid #333; padding: 12px; font-size: 0.85em; border-{{ 'right' if lang == 'AR' else 'left' }}: 4px solid #d4af37; }
        .status { color: #00ff00; font-weight: bold; margin-{{ 'left' if lang == 'AR' else 'right' }}: 10px; }
        
        .alert-bar { background: #ff4d4d; color: black; padding: 8px; text-align: center; font-weight: bold; animation: blink 2s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.7; } 100% { opacity: 1; } }
    </style>
</head>
<body>
    <div class="dashboard">
        <a href="?key={{ key }}&lang={{ 'EN' if lang == 'AR' else 'AR' }}" class="lang-toggle">
            {{ 'English Version' if lang == 'AR' else 'النسخة العربية' }}
        </a>

        <div class="alert-bar">
            {{ "تنبيه سيادي: بروتوكولات الحماية من P11 إلى P15 نشطة" if lang == "AR" else "SOVEREIGN ALERT: P11-P15 PROTECTION PROTOCOLS ACTIVE" }}
        </div>
        
        <h1>IMPERIAL CYBER GENERAL</h1>
        
        <div class="radar-container"><div class="radar-sweep"></div></div>
        
        <div class="valuation">USD ${{ valuation }}</div>
        
        <div class="protocol-grid">
            {% for id, name in protocols %}
            <div class="protocol-card">
                <strong>{{ id }}:</strong> {{ name }} <span class="status">ACTIVE</span>
            </div>
            {% endfor %}
        </div>
        
        <div style="margin-top:40px; font-size:0.75em; text-align:center; color:#555; border-top: 1px solid #222; padding-top: 20px;">
            {{ "نظام الإمبراطورية v2.2 | تم التحقق من المفتاح الرئيسي | الدخول مسموح للجنرال" if lang == "AR" else "IMPERIAL SYSTEM v2.2 | MASTER KEY VALIDATED | ACCESS GRANTED TO GENERAL" }}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    key = request.args.get('key')
    lang = request.args.get('lang', 'AR').upper() # الافتراضي عربي بناءً على طلبك
    
    if key != CONFIG["master_key"]:
        return '<h1 style="background:black; color:red; text-align:center; padding-top:100px; height:100vh; margin:0;">ACCESS DENIED: SOVEREIGN PROTOCOL ACTIVE</h1>', 403
    
    protocols = PROTOCOLS_DATA.get(lang, PROTOCOLS_DATA["AR"])
    
    return render_template_string(HTML_TEMPLATE, valuation=CONFIG["valuation"], protocols=protocols, lang=lang, key=key)

if __name__ == '__main__':
    app.run()
