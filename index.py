from flask import Flask, request, render_template_string

app = Flask(__name__)

# الإعدادات السيادية الثابتة
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

# القائمة الكاملة (15 بروتوكول) لضمان "الهيبة"
PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Legal-Tech Engine", "icon": "📜"},
    {"id": "P5", "ar": "منطق كاسر الأدوات", "en": "Tool Breaker Logic", "icon": "🔨"},
    {"id": "P6", "ar": "التدقيق المعماري", "en": "Architectural Audit", "icon": "🏗️"},
    {"id": "P7", "ar": "النمذجة الشخصية", "en": "Persona Modeling", "icon": "👤"},
    {"id": "P8", "ar": "الأتمتة المنطقية", "en": "Logic Automation", "icon": "⚙️"},
    {"id": "P9", "ar": "التشفير اللغوي", "en": "Linguistic Encryption", "icon": "🔐"},
    {"id": "P10", "ar": "التحليل التنبؤي", "en": "Predictive Analysis", "icon": "🔮"},
    {"id": "P11", "ar": "محاكي الهجمات", "en": "Attack Simulator", "icon": "⚔️"},
    {"id": "P12", "ar": "درع الإبادة P12", "en": "Sovereign Shield", "icon": "🛡️"},
    {"id": "P13", "ar": "الربط السياقي", "en": "Contextual Linking", "icon": "🔗"},
    {"id": "P14", "ar": "التحليل الجنائي", "en": "Forensic Audit", "icon": "🔎"},
    {"id": "P15", "ar": "خارطة الطريق الاستراتيجية", "en": "Strategic Roadmap", "icon": "🗺️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="main-html">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL OS v4.0</title>
    <style>
        :root { --gold: #d4af37; --red: #ff3333; --bg: #020202; --neon: #00ff41; }
        body { background: var(--bg); color: var(--gold); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; overflow: hidden; height: 100vh; }
        
        .main-container { display: grid; grid-template-columns: 320px 1fr 320px; height: 100vh; gap: 10px; padding: 15px; box-sizing: border-box; }
        .panel { border: 1px solid #1a1a1a; background: rgba(5,5,5,0.95); border-radius: 12px; padding: 15px; position: relative; overflow: hidden; }
        
        /* الرادار المتحرك */
        .radar-box { width: 120px; height: 120px; border: 1px solid var(--gold); border-radius: 50%; margin: 10px auto; position: relative; overflow: hidden; }
        .radar-box::after { content: ""; position: absolute; width: 100%; height: 100%; background: conic-gradient(from 0deg, transparent 70%, rgba(212,175,55,0.3) 100%); animation: spin 4s linear infinite; }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

        /* شبكة البروتوكولات (15 زر) */
        .protocol-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; padding: 10px; height: 75vh; overflow-y: auto; scrollbar-width: none; }
        .card { background: #0a0a0a; border: 1px solid #222; padding: 15px; border-radius: 8px; text-align: center; cursor: pointer; transition: 0.3s; }
        .card:hover { border-color: var(--gold); box-shadow: 0 0 15px rgba(212,175,55,0.2); transform: translateY(-3px); }
        .card i { font-size: 1.5rem; display: block; margin-bottom: 5px; }
        .card span { font-size: 10px; display: block; height: 30px; }

        /* زر تبديل اللغة */
        .lang-toggle { position: absolute; top: 10px; right: 10px; background: var(--gold); color: #000; border: none; padding: 5px 15px; font-weight: bold; cursor: pointer; border-radius: 4px; z-index: 100; }

        #log-terminal { font-size: 9px; color: var(--neon); line-height: 1.4; font-family: 'Consolas', monospace; }
        .stat-line { margin-bottom: 10px; font-size: 11px; }
        .progress { height: 3px; background: #222; margin-top: 4px; border-radius: 2px; }
        .progress-fill { height: 100%; background: var(--gold); width: 0%; transition: 1s; }
        
        #app-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.98); z-index: 9999; }
        .app-window { width: 90%; height: 90%; margin: 2% auto; border: 1px solid var(--gold); background: #000; border-radius: 15px; display: flex; flex-direction: column; }
    </style>
</head>
<body>

<button class="lang-toggle" onclick="toggleLanguage()">English</button>

<div class="main-container">
    <div class="panel">
        <h4 style="text-align: center; border-bottom: 1px solid #222; padding-bottom: 5px;">LIVE_SECURITY_FEED</h4>
        <div id="log-terminal"></div>
    </div>

    <div class="panel" style="text-align: center;">
        <h1 id="header-val" style="color: var(--red); font-size: 1.2rem; margin: 0;">ASSET_VALUATION: $50,000,000</h1>
        <p style="font-size: 10px; letter-spacing: 3px;">IMPERIAL_GENERAL_OS_v4.0</p>
        
        <div class="protocol-grid">
            {% for p in protocols %}
            <div class="card" onclick="runProtocol('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                <i>{{ p.icon }}</i>
                <strong style="color: white;">{{ p.id }}</strong>
                <span class="p-name" data-ar="{{ p.ar }}" data-en="{{ p.en }}">{{ p.ar }}</span>
            </div>
            {% endfor %}
        </div>
    </div>

    <div class="panel">
        <h4 style="text-align: center; border-bottom: 1px solid #222; padding-bottom: 5px;">SYSTEM_VITALS</h4>
        <div class="radar-box"></div>
        <div class="stat-line">
            <label id="lbl-enc">CORE_ENCRYPTION: OMEGA</label>
            <div class="progress"><div class="progress-fill" style="width: 100%; background: var(--neon);"></div></div>
        </div>
        <div class="stat-line">
            <label id="lbl-load">NETWORK_TRAFFIC</label>
            <div class="progress"><div id="load-bar" class="progress-fill" style="width: 45%;"></div></div>
        </div>
        <div style="margin-top: 20px; color: var(--red); font-size: 11px; text-align: center;">
            [ P12_SENTINEL_ARMED ]
        </div>
    </div>
</div>

<div id="app-overlay">
    <div class="app-window">
        <div style="background: var(--gold); color: #000; padding: 10px 20px; display: flex; justify-content: space-between; font-weight: bold;">
            <span id="win-title">PROTOCOL_ACCESS</span>
            <button onclick="closeApp()" style="background: #800; color: #fff; border: none; cursor: pointer; padding: 2px 10px;">X</button>
        </div>
        <div id="win-body" style="padding: 30px; color: var(--neon); font-family: monospace; overflow-y: auto;"></div>
    </div>
</div>

<script>
    let currentLang = 'ar';

    function toggleLanguage() {
        currentLang = currentLang === 'ar' ? 'en' : 'ar';
        const btn = document.querySelector('.lang-toggle');
        const html = document.getElementById('main-html');
        
        btn.innerText = currentLang === 'ar' ? 'English' : 'العربية';
        html.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
        html.lang = currentLang === 'ar' ? 'ar' : 'en';

        // تحديث أسماء الأزرار
        document.querySelectorAll('.p-name').forEach(el => {
            el.innerText = currentLang === 'ar' ? el.getAttribute('data-ar') : el.getAttribute('data-en');
        });

        // تحديث العناوين
        document.getElementById('lbl-enc').innerText = currentLang === 'ar' ? 'تشفير النواة: OMEGA' : 'CORE_ENCRYPTION: OMEGA';
        document.getElementById('lbl-load').innerText = currentLang === 'ar' ? 'حركة الشبكة' : 'NETWORK_TRAFFIC';
    }

    // سجل حي (تفاعلي)
    const logs = ["> SCANNING...", "> P12_ACTIVE", "> WHALE_DETECTED", "> SYNC_OK", "> ENCRYPTING..."];
    setInterval(() => {
        const terminal = document.getElementById('log-terminal');
        const line = document.createElement('div');
        line.innerText = `[${new Date().toLocaleTimeString()}] ` + logs[Math.floor(Math.random() * logs.length)];
        terminal.prepend(line);
        if(terminal.childNodes.length > 25) terminal.removeChild(terminal.lastChild);
        
        document.getElementById('load-bar').style.width = (Math.random() * 60 + 20) + "%";
    }, 1500);

    function runProtocol(id, ar, en) {
        document.getElementById('app-overlay').style.display = 'block';
        const title = currentLang === 'ar' ? ar : en;
        document.getElementById('win-title').innerText = `EXECUTING: ${id} // ${title}`;
        document.getElementById('win-body').innerHTML = `
            <h2>Initializing Sovereign Module ${id}...</h2>
            <p>> Secure Connection: Established</p>
            <p>> Environment: Sandbox Zero-Day Protected</p>
            <p>> Master Key Status: <span style="color:white">VALIDATED</span></p>
            <hr style="border:1px solid #222">
            <p>> ${currentLang === 'ar' ? 'جاري سحب البيانات...' : 'Fetching Data Logs...'}</p>
        `;
    }

    function closeApp() { document.getElementById('app-overlay').style.display = 'none'; }

    // حماية P12 ضد "كين"
    setInterval(() => {
        const t = Date.now(); debugger;
        if(Date.now()-t > 100) document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>P12_COUNTER_MEASURE: ACCESS_REVOKED</h1>";
    }, 1000);
</script>
</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    if key != SOVEREIGN_CONFIG["master_key"]:
        return '<div style="background:#000;color:red;height:100vh;display:flex;align-items:center;justify-content:center;"><h1>INVALID KEY</h1></div>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)

if __name__ == "__main__":
    app.run()
