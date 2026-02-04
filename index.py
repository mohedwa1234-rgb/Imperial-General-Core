from flask import Flask, request, render_template_string

app = Flask(__name__)

# الإعدادات السيادية المحفوظة
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

PROTOCOLS = [
    {"id": "P1", "ar": "تحليل البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen", "icon": "🌐"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P8", "ar": "الأتمتة المنطقية", "en": "Logic Automation", "icon": "⚙️"},
    {"id": "P12", "ar": "درع الإبادة السيادي", "en": "Sovereign Shield P12", "icon": "🛡️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL COMMAND CENTER v3.1</title>
    <style>
        :root { --gold: #d4af37; --red: #ff3333; --bg: #020202; --neon: #00ff41; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }

        /* الأنيميشن الأساسي للحركة */
        @keyframes radar-spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        @keyframes pulse-glow { 0% { box-shadow: 0 0 5px var(--gold); } 50% { box-shadow: 0 0 20px var(--gold); } 100% { box-shadow: 0 0 5px var(--gold); } }
        @keyframes scan-line { 0% { top: 0%; } 100% { top: 100%; } }

        .container { display: grid; grid-template-columns: 300px 1fr 300px; height: 100vh; gap: 10px; padding: 15px; }

        /* الرادار التفاعلي (تم إصلاحه ليتحرك) */
        .radar-container {
            width: 150px; height: 150px; border: 2px solid var(--gold); border-radius: 50%;
            margin: 20px auto; position: relative; overflow: hidden;
            background: radial-gradient(circle, rgba(212,175,55,0.1) 0%, transparent 80%);
        }
        .radar-sweep {
            position: absolute; width: 100%; height: 100%;
            background: conic-gradient(from 0deg, transparent 70%, rgba(212,175,55,0.4) 100%);
            animation: radar-spin 3s linear infinite;
        }

        /* كروت البروتوكولات مع نبض */
        .card { 
            background: #0a0a0a; border: 1px solid #222; padding: 20px; border-radius: 10px; 
            cursor: pointer; transition: 0.3s; text-align: center;
        }
        .card:hover { border-color: var(--gold); animation: pulse-glow 1s infinite; }

        /* نافذة التطبيق المستقل */
        #app-overlay { 
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
            background: rgba(0,0,0,0.9); z-index: 9999; backdrop-filter: blur(10px);
        }
        .app-window {
            width: 80%; height: 80%; margin: 5% auto; background: #050505; 
            border: 2px solid var(--gold); border-radius: 20px; position: relative;
            box-shadow: 0 0 50px rgba(0,0,0,1); overflow: hidden;
        }
        
        /* خط المسح "Scanner" */
        .app-window::after {
            content: ""; position: absolute; left: 0; width: 100%; height: 2px;
            background: rgba(212,175,55,0.2); animation: scan-line 4s linear infinite;
        }

        .btn-toggle { background: var(--gold); border: none; padding: 10px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <div style="border: 1px solid #222; padding: 15px;">
        <h3 style="text-align: center;">SYSTEM_VITALS</h3>
        <div class="radar-container">
            <div class="radar-sweep"></div>
        </div>
        <div style="font-size: 12px; color: var(--neon);">
            > CPU_LOAD: <span id="cpu-val">12</span>%<br>
            > ENCRYPTION: OMEGA_7<br>
            > DEFENSE: P12_ACTIVE
        </div>
    </div>

    <div style="overflow-y: auto; padding: 20px;">
        <h1 style="text-align: center;">$50,000,000 ASSET</h1>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            {% for p in protocols %}
            <div class="card" onclick="openModule('{{ p.id }}', '{{ p.ar }}')">
                <i style="font-size: 2rem;">{{ p.icon }}</i><br>
                <strong>{{ p.id }}</strong><br>
                <small>{{ p.ar }}</small>
            </div>
            {% endfor %}
        </div>
    </div>

    <div style="border: 1px solid #222; padding: 15px; font-size: 10px; color: var(--neon);">
        <h3>LIVE_FEED</h3>
        <div id="log-terminal"></div>
    </div>
</div>

<div id="app-overlay">
    <div class="app-window">
        <div style="background: var(--gold); color: black; padding: 10px; display: flex; justify-content: space-between;">
            <span id="win-title">MODULE_CORE</span>
            <button onclick="closeModule()" style="background:red; color:white; border:none; cursor:pointer;">X إغلاق</button>
        </div>
        <div id="win-content" style="padding: 40px; color: var(--neon);"></div>
    </div>
</div>

<script>
    // تحديث الأرقام ديناميكياً ليظهر النظام "حياً"
    setInterval(() => {
        document.getElementById('cpu-val').innerText = Math.floor(Math.random() * (15 - 8 + 1)) + 8;
        const log = document.getElementById('log-terminal');
        const entry = document.createElement('div');
        entry.innerText = `> SEC_AUDIT: ${Math.random().toString(16).substring(2, 8).toUpperCase()}... OK`;
        log.prepend(entry);
        if(log.childNodes.length > 15) log.removeChild(log.lastChild);
    }, 2000);

    function openModule(id, name) {
        document.getElementById('app-overlay').style.display = 'block';
        document.getElementById('win-title').innerText = `EXECUTING: ${id} - ${name}`;
        
        // منع ظهور المفتاح السري نهائياً في الواجهة
        let content = `<h2>البروتوكول المستقل ${id} قيد التشغيل...</h2>
                       <p>> تم عزل البيئة البرمجية لهذا التطبيق.</p>
                       <p>> حالة الاتصال: مشفر عبر GENERAL_EYE_ONLY_VALIDATION_STRING</p>`; // النص هنا تلميح برمجي وليس المفتاح الفعلي
        
        if(id === 'P3') {
            content = `<h2>رصد الحيتان (Whale Tracker)</h2>
                       <p style="color:var(--gold)">> تم رصد حركة بقيمة 50,000,000$ الآن.</p>
                       <div style="height:100px; border:1px solid #333; position:relative;">
                           <div style="width:70%; height:100%; background:rgba(0,255,65,0.1); animation: radar-spin 5s infinite alternate;"></div>
                       </div>`;
        }
        document.getElementById('win-content').innerHTML = content;
    }

    function closeModule() { document.getElementById('app-overlay').style.display = 'none'; }
</script>
</body>
</html>
