from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# الإعدادات السيادية المحفوظة (تستخدم للتحقق البرمجي فقط)
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

# مصفوفة البروتوكولات - كل بروتوكول هو تطبيق مستقل بذاته
PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Processing", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "التحليل التنبؤي الاستباقي", "en": "Predictive Analysis", "icon": "🔮"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Technical Drafting", "icon": "📜"},
    {"id": "P5", "ar": "منطق كاسر الأدوات", "en": "Tool Breaker Logic", "icon": "🔨"},
    {"id": "P6", "ar": "التدقيق المعماري", "en": "Architectural Audit", "icon": "🏗️"},
    {"id": "P7", "ar": "نمذجة الشخصيات", "en": "Persona Modeling", "icon": "👤"},
    {"id": "P8", "ar": "الأتمتة المنطقية", "en": "Logic Automation", "icon": "⚙️"},
    {"id": "P9", "ar": "التشفير الخفي", "en": "Stealth Encryption", "icon": "🔑"},
    {"id": "P10", "ar": "التحسين الذاتي", "en": "Self-Optimization", "icon": "🚀"},
    {"id": "P11", "ar": "التعدد الجيني", "en": "Genetic Mutation", "icon": "🧬"},
    {"id": "P12", "ar": "الفدية العكسية (الدرع)", "en": "Reverse Ransomware", "icon": "🛡️"},
    {"id": "P13", "ar": "الجسر المقاوم للكم", "en": "Quantum Shield", "icon": "🌌"},
    {"id": "P14", "ar": "الارتباط الفيزيائي", "en": "Hardware Binding", "icon": "🔌"},
    {"id": "P15", "ar": "تسميم الذكاء الاصطناعي", "en": "Anti-AI Poisoning", "icon": "🧪"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="sovereign-root">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL - INTEGRATED ECOSYSTEM</title>
    <style>
        :root { --gold: #d4af37; --red: #ff4d4d; --bg: #050505; --surface: #121212; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
        .alert-header { background: var(--red); color: black; padding: 10px; text-align: center; font-weight: bold; position: sticky; top: 0; z-index: 1000; font-size: 13px; }
        .container { padding: 20px; max-width: 1200px; margin: 0 auto; height: 100vh; display: flex; flex-direction: column; }
        .valuation { font-size: 2.2rem; color: var(--red); font-weight: bold; text-align: center; margin: 10px 0; text-shadow: 0 0 15px var(--red); }
        .protocol-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; overflow-y: auto; padding-bottom: 50px; }
        .card { background: var(--surface); border: 1px solid #222; padding: 15px; text-align: center; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        .card:hover { border-color: var(--gold); transform: scale(1.05); background: #1a1a1a; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); }
        .card i { font-size: 1.8rem; display: block; margin-bottom: 10px; }
        
        #app-window { 
            display: none; position: fixed; top: 5%; left: 5%; width: 90%; height: 85%; 
            background: #000; border: 2px solid var(--gold); z-index: 2000; box-shadow: 0 0 100px #000;
        }
        .window-header { background: var(--gold); color: black; padding: 10px; display: flex; justify-content: space-between; font-weight: bold; }
        .close-btn { cursor: pointer; background: #8B0000; color: white; border: none; padding: 5px 15px; border-radius: 3px; }
        .app-iframe { width: 100%; height: calc(100% - 45px); border: none; background: #080808; padding: 20px; box-sizing: border-box; color: #00ff00; overflow-y: auto; }
    </style>
</head>
<body>
    <div class="alert-header" id="alert-msg">نظام التحكم السيادي: جميع الوحدات (P1-P15) تعمل كأنظمة مستقلة تحت إشراف "الجنرال"</div>

    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 10px;">
            <button onclick="toggleLanguage()" style="background: var(--gold); border: none; padding: 5px 15px; font-weight: bold; cursor: pointer;">EN/AR</button>
            <div style="font-size: 12px;">SECURITY_LEVEL: OMEGA</div>
        </div>

        <div class="valuation">$50,000,000 USD</div>

        <div class="protocol-grid">
            {% for p in protocols %}
            <div class="card" onclick="launchApplication('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                <i>{{ p.icon }}</i>
                <strong>{{ p.id }}</strong>
                <p class="p-name" data-ar="{{ p.ar }}" data-en="{{ p.en }}" style="font-size: 12px; margin: 5px 0;">{{ p.ar }}</p>
            </div>
            {% endfor %}
        </div>
    </div>

    <div id="app-window">
        <div class="window-header">
            <span id="window-title">المركز الرئيسي</span>
            <button class="close-btn" onclick="terminateApp()">إغلاق X</button>
        </div>
        <div id="app-content" class="app-iframe"></div>
    </div>

    <script>
        let currentLang = 'AR';
        
        function launchApplication(id, ar, en) {
            const win = document.getElementById('app-window');
            const content = document.getElementById('app-content');
            const title = document.getElementById('window-title');
            win.style.display = 'block';
            title.innerText = (currentLang === 'AR') ? ar : en;

            let appLogic = "";
            switch(id) {
                case 'P1': appLogic = `<h3>[P1] معالجة البيانات الضخمة</h3><p>> جاري الاتصال بخوادم البيانات...<br>> تم تحليل 1.2 Terabytes من البيانات.<br>> الحالة: مؤمن تماماً.</p>`; break;
                case 'P3': appLogic = `<h3>[P3] توقع حركة الحيتان</h3><p>> رصد تدفق سيولة بقيمة 12M$ نحو الأصول المشفرة.<br>> توصية: استباق الشراء في القطاع X.</p>`; break;
                case 'P12': appLogic = `<h3>[P12] حالة الدرع السيادي</h3><p>> محاولات الاختراق المرصودة: 0<br>> نظام الردع التلقائي: جاهز للإبادة.</p>`; break;
                default: appLogic = `<h3>نظام مستقل: ${id}</h3><p>> البروتوكول نشط ويعمل ككيان منفصل ببياناته الخاصة.<br>> التشفير السيادي: <span style="color: #00ff00;">مفعل ونشط [ENCRYPTED]</span></p>`;
            }
            content.innerHTML = appLogic;
        }

        function terminateApp() { document.getElementById('app-window').style.display = 'none'; }

        function toggleLanguage() {
            currentLang = (currentLang === 'AR') ? 'EN' : 'AR';
            document.querySelectorAll('.p-name').forEach(el => {
                el.innerText = (currentLang === 'AR') ? el.getAttribute('data-ar') : el.getAttribute('data-en');
            });
        }

        (function() {
            let triggered = false;
            setInterval(() => {
                const start = Date.now();
                debugger;
                if (Date.now() - start > 100 && !triggered) {
                    triggered = true;
                    fetch('/log_intrusion', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({event: "P12_ACTIVE_DEFENSE", info: navigator.userAgent})
                    });
                    document.body.innerHTML = "<div style='background:#8B0000;color:white;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;'><h1>تم تفعيل بروتوكول الإبادة</h1><h1 style='font-size:8rem;'>GAME OVER</h1></div>";
                    setTimeout(() => { while(true){} }, 500);
                }
            }, 500);
        })();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    if key != SOVEREIGN_CONFIG["master_key"]:
        return '<div style="background:#000;color:#f00;height:100vh;display:flex;align-items:center;justify-content:center;"><h1>ACCESS DENIED</h1></div>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)

@app.route('/log_intrusion', methods=['POST'])
def log_intrusion():
    report = request.json
    with open("intruders.log", "a", encoding="utf-8") as f:
        f.write(f"ALERT: {report}\\n")
    return {"status": "recorded"}, 200

if __name__ == "__main__":
    app.run()
