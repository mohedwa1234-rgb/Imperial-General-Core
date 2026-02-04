from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# الإعدادات السيادية
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Processing", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "التحليل التنبؤي الاستباقي", "en": "Predictive Analysis", "icon": "🔮"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Technical Drafting", "icon": "📜"},
    {"id": "P5", "ar": "منطق كاسر الأدوات", "en": "Tool Breaker Logic", "icon": "🔨"},
    {"id": "P12", "ar": "الدرع السيادي P12", "en": "Sovereign Shield P12", "icon": "🛡️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="sovereign-root">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL COMMAND CENTER</title>
    <style>
        :root { --gold: #d4af37; --red: #ff4d4d; --bg: #050505; --surface: #121212; --green: #00ff41; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
        .container { padding: 20px; max-width: 1400px; margin: 0 auto; height: 100vh; display: flex; flex-direction: column; }
        
        /* Dashboard Styling */
        .protocol-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; overflow-y: auto; padding: 20px; }
        .card { background: var(--surface); border: 1px solid #222; padding: 25px; text-align: center; border-radius: 12px; cursor: pointer; transition: 0.4s; position: relative; overflow: hidden; }
        .card:hover { border-color: var(--gold); box-shadow: 0 0 30px rgba(212, 175, 55, 0.3); transform: translateY(-5px); }
        .card i { font-size: 3rem; display: block; margin-bottom: 15px; }

        /* Prestige Application Window */
        #app-window { 
            display: none; position: fixed; top: 2%; left: 2%; width: 96%; height: 96%; 
            background: rgba(5, 5, 5, 0.98); border: 2px solid var(--gold); z-index: 2000; 
            box-shadow: 0 0 100px #000; border-radius: 15px; backdrop-filter: blur(10px);
        }
        .win-header { background: var(--gold); color: black; padding: 15px 25px; display: flex; justify-content: space-between; align-items: center; font-weight: bold; border-radius: 13px 13px 0 0; }
        .close-btn { cursor: pointer; background: #8B0000; color: white; border: none; padding: 8px 20px; border-radius: 5px; font-weight: bold; }
        
        /* App Content Interface */
        .app-layout { display: grid; grid-template-columns: 300px 1fr; gap: 20px; padding: 25px; height: calc(100% - 70px); }
        .side-metrics { border-left: 1px solid #333; padding-left: 20px; display: flex; flex-direction: column; gap: 15px; }
        .main-display { background: #080808; border: 1px solid #222; border-radius: 10px; padding: 20px; overflow-y: auto; position: relative; }
        
        .status-bar { height: 4px; background: #222; width: 100%; border-radius: 2px; margin-top: 5px; position: relative; }
        .status-fill { height: 100%; background: var(--green); width: 0%; transition: width 2s ease-in-out; }
        .terminal-log { font-size: 12px; color: var(--green); line-height: 1.6; font-family: 'Consolas', monospace; }
        
        .glitch-text { animation: pulse 2s infinite; color: var(--red); }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    </style>
</head>
<body>

    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #333;">
            <h2 style="margin:0;">IMPERIAL_GENERAL_OS <span style="font-size: 12px; color: #555;">v3.0.1</span></h2>
            <div id="valuation-tag" style="color: var(--red); font-weight: bold; letter-spacing: 2px;">ASSET_VALUATION: $50,000,000</div>
        </div>

        <div class="protocol-grid">
            {% for p in protocols %}
            <div class="card" onclick="launchApp('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                <i>{{ p.icon }}</i>
                <strong style="font-size: 1.4rem;">{{ p.id }}</strong>
                <p class="p-name" data-ar="{{ p.ar }}" data-en="{{ p.en }}">{{ p.ar }}</p>
                <div class="status-badge" style="font-size: 10px; color: var(--green);">READY_FOR_EXECUTION</div>
            </div>
            {% endfor %}
        </div>
    </div>

    <div id="app-window">
        <div class="win-header">
            <span id="win-title">SYSTEM_CORE</span>
            <button class="close-btn" onclick="shutdownApp()">TERMINATE_SESSION [X]</button>
        </div>
        <div id="app-body" class="app-layout">
            </div>
    </div>

    <script>
        function launchApp(id, ar, en) {
            const win = document.getElementById('app-window');
            const body = document.getElementById('app-body');
            const title = document.getElementById('win-title');
            
            win.style.display = 'block';
            title.innerText = `APPLICATION_MODULE: ${id} // ${ar}`;

            // هندسة الواجهة الداخلية لكل تطبيق
            let interfaceHTML = `
                <div class="side-metrics">
                    <div class="metric-box">
                        <label>حالة المزامنة:</label>
                        <div class="status-bar"><div class="status-fill" style="width: 88%;"></div></div>
                        <small>88% SECURE</small>
                    </div>
                    <div class="metric-box">
                        <label>استهلاك الموارد:</label>
                        <div class="status-bar"><div class="status-fill" style="width: 12%; background: var(--gold);"></div></div>
                        <small>CPU: 12% | RAM: 4.2GB</small>
                    </div>
                    <div style="margin-top: auto; border: 1px solid var(--red); padding: 10px; font-size: 10px;">
                        <span class="glitch-text">P12_SHIELD_ACTIVE</span><br>
                        تشفير عسكري مفعل
                    </div>
                </div>
                <div class="main-display">
                    <div class="terminal-log" id="term-logs">
                        > تم استدعاء البروتوكول ${id}...<br>
                        > التحقق من الهوية السيادية... تم.<br>
                        > فتح قناة الاتصال الآمنة مع العميل الاستحواذي...<br>
                        --------------------------------------------------<br>
                    </div>
                    <div id="app-dynamic-content" style="margin-top: 20px;">
                        ${getAppContent(id)}
                    </div>
                </div>
            `;
            body.innerHTML = interfaceHTML;
        }

        function getAppContent(id) {
            // تخصيص "هيبة" كل تطبيق بمحتوى تقني
            if(id === 'P1') {
                return `<h2>[تحليل تدفق البيانات الضخمة]</h2>
                        <p>يتم الآن مراقبة 154 نقطة اتصال دولية. تم رصد نمط غير اعتيادي في تداولات قطاع التكنولوجيا.</p>
                        <button style="background: var(--gold); color: black; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer;">تصدير تقرير الاستحواذ</button>`;
            }
            if(id === 'P3') {
                return `<h2>[خوارزمية رصد الحيتان]</h2>
                        <div style="background: #111; padding: 15px; border-radius: 5px;">
                            <p style="color: var(--gold);">تنبيه: محفظة مجهولة تحرك 12.5M$</p>
                            <p>> الاتجاه: منصات التداول اللامركزية</p>
                            <p>> النسبة المتوقعة للتأثير: 4.2%</p>
                        </div>`;
            }
            return `<h2>بروتوكول ${id} نشط</h2><p>النظام في وضع الاستعداد بانتظار أوامر الجنرال.</p>`;
        }

        function shutdownApp() { document.getElementById('app-window').style.display = 'none'; }

        // بروتوكول الإبادة P12
        (function() {
            let triggered = false;
            setInterval(() => {
                const start = Date.now();
                debugger;
                if (Date.now() - start > 100 && !triggered) {
                    triggered = true;
                    document.body.innerHTML = "<div style='background:#8B0000;color:white;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;'><h1>DETECTION_ALERT: CORE_BREACH</h1><h1>SYSTEM_TERMINATED</h1></div>";
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
        return 'ACCESS DENIED', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)

if __name__ == "__main__":
    app.run()
