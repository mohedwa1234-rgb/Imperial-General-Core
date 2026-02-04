from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# الإعدادات السيادية
SOVEREIGN_CONFIG = {"master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING"}

PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P6", "ar": "التدقيق المعماري", "en": "Architectural Audit", "icon": "🏗️"},
    {"id": "P12", "ar": "درع الإبادة P12", "en": "Sovereign Shield", "icon": "🛡️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL OS v5.0</title>
    <style>
        :root { --gold: #d4af37; --neon: #00ff41; --bg: #020202; --red: #ff3333; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
        
        .main-ui { display: grid; grid-template-columns: 300px 1fr; height: 100vh; padding: 10px; gap: 10px; }
        .panel { border: 1px solid #222; background: #050505; border-radius: 8px; padding: 15px; position: relative; }
        
        /* تأثيرات الحركة (النبض التفاعلي) */
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
        @keyframes blink { 50% { opacity: 0.3; } }

        .protocol-btn { background: #111; border: 1px solid #333; padding: 20px; margin-bottom: 10px; cursor: pointer; transition: 0.3s; text-align: right; width: 100%; color: var(--gold); }
        .protocol-btn:hover { border-color: var(--gold); box-shadow: 0 0 15px rgba(212,175,55,0.2); }

        /* نافذة التنفيذ (مملوءة بالبيانات) */
        #app-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 1000; padding: 30px; box-sizing: border-box; }
        .app-window { border: 2px solid var(--gold); height: 100%; background: #000; border-radius: 12px; display: flex; flex-direction: column; position: relative; overflow: hidden; }
        .app-window::after { content: ""; position: absolute; width: 100%; height: 2px; background: rgba(212,175,55,0.1); animation: scan 3s linear infinite; top: 0; }
        
        .data-stream { flex-grow: 1; padding: 20px; color: var(--neon); font-size: 13px; overflow-y: auto; scrollbar-width: none; }
        .visual-bars { display: flex; align-items: flex-end; gap: 5px; height: 100px; padding: 10px; border-bottom: 1px solid #222; }
        .bar { width: 15px; background: var(--gold); animation: grow 0.5s ease-in-out infinite alternate; }
        @keyframes grow { from { height: 10%; } to { height: 100%; } }
    </style>
</head>
<body>

<div class="main-ui">
    <div class="panel">
        <h3 style="text-align:center;">PROTOCOL_CONTROL</h3>
        {% for p in protocols %}
        <button class="protocol-btn" onclick="openApp('{{ p.id }}', '{{ p.ar }}')">
            <span>{{ p.icon }}</span> <strong>{{ p.id }}</strong><br>
            <small style="font-size: 9px;">{{ p.ar }}</small>
        </button>
        {% endfor %}
    </div>
    
    <div class="panel" style="display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="color:var(--red); font-size: 3rem; margin:0;">$50,000,000</h1>
        <p style="letter-spacing: 10px;">SYSTEM_ACTIVE</p>
        <div style="width:200px; height:200px; border:2px solid var(--gold); border-radius:50%; position:relative; overflow:hidden;">
            <div style="position:absolute; width:100%; height:100%; background:conic-gradient(from 0deg, transparent 70%, var(--gold) 100%); animation: spin 2s linear infinite; opacity: 0.3;"></div>
        </div>
    </div>
</div>

<div id="app-overlay">
    <div class="app-window">
        <div style="background:var(--gold); color:#000; padding:10px 20px; font-weight:bold; display:flex; justify-content:space-between;">
            <span id="win-title">EXECUTING_MODULE</span>
            <button onclick="closeApp()" style="background:var(--red); border:none; color:#fff; cursor:pointer;">CLOSE_SESSION [X]</button>
        </div>
        
        <div class="visual-bars" id="bars-container"></div>
        
        <div class="data-stream" id="stream-body"></div>
    </div>
</div>

<script>
    function openApp(id, name) {
        document.getElementById('app-overlay').style.display = 'block';
        document.getElementById('win-title').innerText = `MODULE: ${id} // ${name}`;
        
        const stream = document.getElementById('stream-body');
        const bars = document.getElementById('bars-container');
        stream.innerHTML = "> Initializing Sovereign Bridge...<br>> Connection: SECURE<br>> سحب البيانات الاستراتيجية...<br>";
        bars.innerHTML = "";

        // إنشاء أعمدة بيانية تتحرك (ملء الفراغ البصري)
        for(let i=0; i<30; i++) {
            let b = document.createElement('div');
            b.className = 'bar';
            b.style.animationDelay = (i * 0.1) + 's';
            bars.appendChild(b);
        }

        // محاكاة سحب بيانات لا تنتهي (ملء الفراغ النصي)
        const fakeData = [
            "> [TRACE] محاولة وصول من IP 192.168.1.1 - تم الحظر.",
            "> [DATA] تم فك تشفير حزمة البيانات رقم " + Math.random().toString(16).slice(2,8),
            "> [WHALE] محفظة حوت نشطة بقيمة 12.4M USD.",
            "> [SYNC] مزامنة النواة مع خادم Vercel... 100%",
            "> [P12] الدرع السيادي يعمل بكامل طاقته."
        ];

        window.dataInterval = setInterval(() => {
            let line = document.createElement('div');
            line.innerText = fakeData[Math.floor(Math.random() * fakeData.length)];
            stream.prepend(line);
        }, 800);
    }

    function closeApp() { 
        document.getElementById('app-overlay').style.display = 'none'; 
        clearInterval(window.dataInterval);
    }
</script>
<style> @keyframes spin { to { transform: rotate(360deg); } } </style>
</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    if key != SOVEREIGN_CONFIG["master_key"]:
        return '<h1 style="color:red; text-align:center;">ACCESS DENIED</h1>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)
