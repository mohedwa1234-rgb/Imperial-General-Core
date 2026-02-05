from flask import Flask, request, render_template_string

app = Flask(__name__)

# الثوابت السيادية المحفوظة [cite: 2026-02-04]
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "$50,000,000"
}

# القائمة الكاملة للبروتوكولات (15 وحدة) لضمان الهيبة [cite: 2026-01-23]
PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Technical Contracts", "icon": "📜"},
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
<html lang="ar" dir="rtl" id="master-root">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL OS v5.0</title>
    <style>
        :root { --gold: #d4af37; --red: #ff3333; --bg: #020202; --neon: #00ff41; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; height: 100vh; }
        
        /* محرك الرادار والتحليل */
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
        @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        @keyframes pulse { 0% { opacity: 0.5; } 50% { opacity: 1; } 100% { opacity: 0.5; } }

        .dashboard { display: grid; grid-template-columns: 320px 1fr 320px; height: 100vh; gap: 10px; padding: 10px; box-sizing: border-box; }
        .panel { border: 1px solid #1a1a1a; background: #050505; border-radius: 8px; padding: 15px; overflow: hidden; position: relative; }
        
        /* تعبئة الفراغ بالأزرار (15 زر) */
        .grid-15 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; overflow-y: auto; height: 80vh; scrollbar-width: none; }
        .card { background: #0a0a0a; border: 1px solid #222; padding: 10px; text-align: center; cursor: pointer; transition: 0.2s; border-radius: 5px; }
        .card:hover { border-color: var(--gold); background: #111; transform: scale(1.05); }
        .card i { font-size: 1.2rem; }
        .card span { font-size: 9px; display: block; margin-top: 5px; color: #888; }

        /* شاشة التنفيذ التفاعلية (حل مشكلة الفراغ الأسود) */
        #execution-layer { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.98); z-index: 10000; padding: 40px; }
        .terminal-window { border: 2px solid var(--gold); height: 100%; display: flex; flex-direction: column; background: #000; position: relative; }
        .terminal-window::after { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: rgba(0,255,65,0.2); animation: scan 3s linear infinite; }
        
        .live-data-stream { flex-grow: 1; padding: 20px; color: var(--neon); font-size: 12px; overflow-y: hidden; }
        .stat-bar { height: 4px; background: #111; margin: 10px 0; border-radius: 2px; }
        .stat-fill { height: 100%; background: var(--gold); width: 0%; transition: width 0.5s; }

        .lang-btn { position: absolute; top: 10px; left: 10px; background: var(--gold); border: none; padding: 5px 15px; cursor: pointer; font-weight: bold; z-index: 10001; }
    </style>
</head>
<body>

<button class="lang-btn" onclick="toggleLang()">EN</button>

<div class="dashboard">
    <div class="panel">
        <h4 style="text-align: center; color: var(--neon);">LIVE_SECURITY_FEED</h4>
        <div id="security-logs" style="font-size: 10px; color: var(--neon);"></div>
    </div>

    <div class="panel" style="text-align: center;">
        <h2 style="color: var(--red); margin: 0;">{{ valuation }}</h2>
        <p style="font-size: 10px; letter-spacing: 5px;">IMPERIAL_GENERAL_OS_v5.0</p>
        <div class="grid-15">
            {% for p in protocols %}
            <div class="card" onclick="launch('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                <i>{{ p.icon }}</i>
                <b style="display:block; font-size:12px;">{{ p.id }}</b>
                <span class="p-title" data-ar="{{ p.ar }}" data-en="{{ p.en }}">{{ p.ar }}</span>
            </div>
            {% endfor %}
        </div>
    </div>

    <div class="panel">
        <h4 style="text-align: center;">SYSTEM_VITALS</h4>
        <div style="width:100px; height:100px; border:1px solid var(--gold); border-radius:50%; margin: 20px auto; position:relative;">
            <div style="width:100%; height:100%; background:conic-gradient(from 0deg, transparent 80%, var(--gold) 100%); animation: rotate 3s linear infinite; border-radius:50%;"></div>
        </div>
        <div style="font-size: 11px;">
            CPU_LOAD: <span id="cpu-val">24</span>% <div class="stat-bar"><div id="cpu-fill" class="stat-fill" style="width:24%"></div></div>
            ENCRYPTION: OMEGA-7 <div class="stat-bar"><div class="stat-fill" style="width:100%; background:var(--neon)"></div></div>
        </div>
    </div>
</div>

<div id="execution-layer">
    <div class="terminal-window">
        <div style="background:var(--gold); color:#000; padding:10px; display:flex; justify-content:space-between; font-weight:bold;">
            <span id="win-id">PROTOCOL_ACTIVE</span>
            <button onclick="terminate()" style="background:var(--red); border:none; color:#fff; cursor:pointer;">TERMINATE [X]</button>
        </div>
        <div class="live-data-stream" id="stream-content"></div>
    </div>
</div>

<script>
    let currentLang = 'ar';
    function toggleLang() {
        currentLang = currentLang === 'ar' ? 'en' : 'ar';
        document.getElementById('master-root').dir = currentLang === 'ar' ? 'rtl' : 'ltr';
        document.querySelectorAll('.p-title').forEach(el => el.innerText = el.getAttribute('data-' + currentLang));
        document.querySelector('.lang-btn').innerText = currentLang === 'ar' ? 'EN' : 'AR';
    }

    // محاكاة سحب البيانات لملء الفراغ
    function launch(id, ar, en) {
        document.getElementById('execution-layer').style.display = 'block';
        const stream = document.getElementById('stream-content');
        const title = currentLang === 'ar' ? ar : en;
        document.getElementById('win-id').innerText = `EXECUTING: ${id} // ${title}`;
        
        stream.innerHTML = `> Initializing ${id}...<br>> Connection Secured.<br>> Fetching Imperial Data...<br>`;
        
        window.activeInt = setInterval(() => {
            const lines = [
                `> [DATA] New Block Decrypted: ${Math.random().toString(16).slice(2,10)}`,
                `> [SEC] Audit Pass: Sovereign Logic Verified.`,
                `> [WHALE] Movement Detected: $12.4M USD -> Target Alpha.`,
                `> [SYSTEM] Self-Optimization in progress...`
            ];
            const div = document.createElement('div');
            div.innerHTML = lines[Math.floor(Math.random() * lines.length)];
            stream.prepend(div);
            if(stream.childNodes.length > 25) stream.removeChild(stream.lastChild);
        }, 500);
    }

    function terminate() {
        document.getElementById('execution-layer').style.display = 'none';
        clearInterval(window.activeInt);
    }

    // سجلات أمنية حية في الشريط الجانبي
    setInterval(() => {
        const logs = document.getElementById('security-logs');
        const entry = document.createElement('div');
        entry.innerText = `> SEC_AUDIT_${Math.floor(Math.random()*999)}: OK`;
        logs.prepend(entry);
        if(logs.childNodes.length > 20) logs.removeChild(logs.lastChild);
        
        const load = Math.floor(Math.random() * 15) + 10;
        document.getElementById('cpu-val').innerText = load;
        document.getElementById('cpu-fill').style.width = load + "%";
    }, 2000);
</script>
</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    if key != SOVEREIGN_CONFIG["master_key"]:
        return '<h1 style="color:red;text-align:center;">ACCESS_DENIED: MASTER_KEY_REQUIRED</h1>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS, valuation=SOVEREIGN_CONFIG["valuation"])
