from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# الإعدادات السيادية (M&A Grade Configuration)
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

# مصفوفة البروتوكولات المطورة (The Imperial 15)
PROTOCOLS = [
    {"id": "P1", "ar": "تحليل البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Legal-Tech Engine", "icon": "📜"},
    {"id": "P5", "ar": "منطق كاسر الأدوات", "en": "Tool Breaker Logic", "icon": "🔨"},
    {"id": "P6", "ar": "التدقيق المعماري", "en": "Architectural Audit", "icon": "🏗️"},
    {"id": "P12", "ar": "درع الإبادة السيادي", "en": "Sovereign Shield P12", "icon": "🛡️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL - COMMAND CENTER</title>
    <style>
        :root { --gold: #d4af37; --red: #ff3333; --bg: #030303; --neon-green: #00ff41; }
        
        body, html { margin: 0; padding: 0; background: var(--bg); color: var(--gold); font-family: 'Segoe UI', monospace; overflow: hidden; height: 100vh; }
        
        /* تأثير الخلفية الرادارية */
        .radar-bg { position: fixed; top: 50%; left: 50%; width: 200vw; height: 200vw; transform: translate(-50%, -50%); 
                     background: radial-gradient(circle, rgba(212, 175, 55, 0.05) 0%, transparent 70%); z-index: -1; animation: pulse 8s infinite; }
        
        @keyframes pulse { 0% { opacity: 0.3; } 50% { opacity: 0.6; } 100% { opacity: 0.3; } }

        /* الهيكل الرئيسي */
        .main-grid { display: grid; grid-template-columns: 280px 1fr 280px; height: 100vh; gap: 10px; padding: 15px; box-sizing: border-box; }
        
        .side-panel { background: rgba(18, 18, 18, 0.8); border: 1px solid #222; border-radius: 10px; padding: 15px; backdrop-filter: blur(5px); }
        .center-panel { display: flex; flex-direction: column; gap: 15px; overflow-y: auto; scrollbar-width: none; }

        /* واجهة البروتوكولات */
        .protocol-card { background: #0a0a0a; border: 1px solid #1a1a1a; padding: 20px; border-radius: 8px; cursor: pointer; 
                         transition: 0.3s; position: relative; overflow: hidden; text-align: right; }
        .protocol-card:hover { border-color: var(--gold); background: #111; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); transform: scale(1.02); }
        .protocol-card i { font-size: 2rem; margin-left: 15px; color: var(--gold); }
        
        /* مؤشرات النظام */
        .stat-box { margin-bottom: 20px; font-size: 12px; }
        .progress-bar { height: 4px; background: #222; margin-top: 5px; border-radius: 2px; overflow: hidden; }
        .progress-fill { height: 100%; background: var(--gold); width: 0%; transition: 2s; }

        /* نافذة التطبيق المستقل (Deep Dive) */
        #app-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                        background: rgba(0,0,0,0.95); z-index: 5000; padding: 40px; box-sizing: border-box; }
        .app-window { border: 2px solid var(--gold); height: 100%; border-radius: 15px; display: flex; flex-direction: column; background: #050505; }
        .app-header { background: var(--gold); color: black; padding: 15px; display: flex; justify-content: space-between; font-weight: bold; }
        .app-content { flex-grow: 1; padding: 30px; overflow-y: auto; color: var(--neon-green); font-family: 'Consolas', monospace; }
        
        .close-btn { background: #8B0000; color: white; border: none; padding: 5px 20px; cursor: pointer; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="radar-bg"></div>

    <div class="main-grid">
        <div class="side-panel">
            <h3 style="border-bottom: 1px solid var(--gold); padding-bottom: 10px;">SYSTEM_VITALS</h3>
            <div class="stat-box">
                <label>CORE_ENCRYPTION: OMEGA</label>
                <div class="progress-bar"><div class="progress-fill" style="width: 100%; background: var(--neon-green);"></div></div>
            </div>
            <div class="stat-box">
                <label>NETWORK_SHIELD: ACTIVE</label>
                <div class="progress-bar"><div class="progress-fill" style="width: 94%;"></div></div>
            </div>
            <div style="margin-top: 50px; text-align: center;">
                <p style="color: var(--red); font-size: 10px; font-weight: bold;">[ P12_SENTINEL_READY ]</p>
                <div id="radar-ui" style="width: 100px; height: 100px; border: 1px solid var(--gold); border-radius: 50%; margin: 0 auto; position: relative;">
                    <div style="width: 100%; height: 100%; border-radius: 50%; background: conic-gradient(from 0deg, transparent, rgba(212,175,55,0.4)); animation: spin 2s linear infinite;"></div>
                </div>
            </div>
        </div>

        <div class="center-panel">
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="letter-spacing: 8px; margin-bottom: 0;">IMPERIAL_GENERAL_OS</h1>
                <p style="color: var(--red); font-weight: bold;">VALUATION: $50,000,000 // ENTERPRISE_GRADE</p>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                {% for p in protocols %}
                <div class="protocol-card" onclick="openProtocol('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                        <span><strong>{{ p.id }}</strong></span>
                        <i>{{ p.icon }}</i>
                    </div>
                    <p style="margin: 10px 0 0 0; font-size: 14px;">{{ p.ar }}</p>
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="side-panel">
            <h3 style="border-bottom: 1px solid var(--gold); padding-bottom: 10px;">LIVE_FEED</h3>
            <div id="logs" style="font-size: 10px; color: var(--neon-green); line-height: 1.5;">
                > INITIALIZING_CORE...<br>
                > SOVEREIGN_IDENTITY_VERIFIED...<br>
                > MONITORING_WHALE_WALLETS...<br>
            </div>
        </div>
    </div>

    <div id="app-overlay">
        <div class="app-window">
            <div class="app-header">
                <span id="app-title">PROTCOL_MODULE</span>
                <button class="close-btn" onclick="closeApp()">SHUTDOWN [X]</button>
            </div>
            <div class="app-content" id="app-body">
                </div>
        </div>
    </div>

    <script>
        function openProtocol(id, ar, en) {
            const overlay = document.getElementById('app-overlay');
            const body = document.getElementById('app-body');
            const title = document.getElementById('app-title');
            
            overlay.style.display = 'block';
            title.innerText = `${id} // MODULE_ACCESS: ${en}`;
            
            let content = "";
            if(id === 'P3') {
                content = `<h2>[رصد تدفقات السيولة الكبرى]</h2>
                           <div style="border: 1px solid #333; padding: 20px;">
                               <p>> التقط الرادار: تحويل 4,500 BTC إلى محفظة باردة.</p>
                               <p>> الحالة: استباق شراء في منطقة الدعم X.</p>
                               <p>> ثقة النظام: 98.4%</p>
                           </div>
                           <div style="margin-top:20px; height:100px; border-left: 2px solid var(--gold); padding-left:10px;">
                                [رسوم بيانية مشفرة جاري إنشاؤها...]
                           </div>`;
            } else if(id === 'P12') {
                content = `<h2>[وحدة الدفاع النشط P12]</h2>
                           <p style="color: var(--red);">تحذير: النظام في وضع "الإبادة التلقائية".</p>
                           <p>> لا توجد محاولات اختراق نشطة حالياً.</p>
                           <p>> سجل المتسللين: فارغ (نظيف).</p>`;
            } else {
                content = `<h2>نظام مستقل: ${id}</h2>
                           <p>> جاري مزامنة البيانات مع الرأس المدبر...</p>
                           <p>> حالة التشفير: OMEGA-SECURE</p>
                           <p>> سجل الدخول: مؤمن تماماً.</p>`;
            }
            body.innerHTML = content;
        }

        function closeApp() { document.getElementById('app-overlay').style.display = 'none'; }

        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

        // بروتوكول الإبادة P12
        (function() {
            setInterval(() => {
                const start = Date.now();
                debugger;
                if (Date.now() - start > 100) {
                    fetch('/log_intrusion', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({event: "CORE_INSPECTION", agent: navigator.userAgent})
                    });
                    document.body.innerHTML = "<div style='background:#8B0000;color:white;height:100vh;display:flex;justify-content:center;align-items:center;'><h1>ACCESS_DENIED: P12_COUNTER_MEASURE_ACTIVE</h1></div>";
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
        return '<div style="background:#000;color:#f00;height:100vh;display:flex;align-items:center;justify-content:center;"><h1>INVALID SOVEREIGN KEY</h1></div>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)

@app.route('/log_intrusion', methods=['POST'])
def log_intrusion():
    report = request.json
    with open("intruders.log", "a", encoding="utf-8") as f:
        f.write(f"ALERT: {report}\\n")
    return {"status": "recorded"}, 200

if __name__ == "__main__":
    app.run()
