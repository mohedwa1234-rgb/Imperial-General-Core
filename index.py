from flask import Flask, request, render_template_string

app = Flask(__name__)

# الإعدادات السيادية (مخفية عن الواجهة)
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Intelligence", "icon": "📊"},
    {"id": "P3", "ar": "رصد تحركات الحيتان", "en": "Whale Flow Tracker", "icon": "🐋"},
    {"id": "P8", "ar": "الأتمتة المنطقية", "en": "Logic Automation", "icon": "⚙️"},
    {"id": "P12", "ar": "درع الإبادة P12", "en": "Sovereign Shield", "icon": "🛡️"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL OS - LIVE MODULE</title>
    <style>
        :root { --gold: #d4af37; --red: #ff3333; --bg: #050505; --neon: #00ff41; }
        body { background: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
        
        /* الرادار المتحرك فعلياً */
        .radar {
            width: 150px; height: 150px; border: 2px solid var(--gold); border-radius: 50%;
            position: relative; margin: 20px auto; overflow: hidden;
        }
        .radar::after {
            content: ""; position: absolute; width: 100%; height: 100%;
            background: conic-gradient(from 0deg, transparent 70%, rgba(212,175,55,0.4) 100%);
            animation: spin 3s linear infinite;
        }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

        /* شريط الحالة النابض */
        .pulse-bar { height: 4px; background: #222; width: 100%; border-radius: 2px; overflow: hidden; }
        .pulse-fill { height: 100%; background: var(--neon); width: 0%; transition: width 0.5s; }

        .container { display: grid; grid-template-columns: 300px 1fr 300px; height: 100vh; gap: 10px; padding: 15px; }
        .panel { border: 1px solid #222; padding: 15px; background: rgba(10,10,10,0.9); border-radius: 10px; }
        
        /* تأثير "الهاكر" لسجل العمليات */
        #log-feed { font-size: 10px; color: var(--neon); height: 300px; overflow: hidden; line-height: 1.5; }
        
        .card { background: #111; border: 1px solid #333; padding: 15px; text-align: center; cursor: pointer; transition: 0.3s; }
        .card:hover { border-color: var(--gold); transform: translateY(-5px); box-shadow: 0 0 15px var(--gold); }

        #app-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 10000; padding: 50px; }
        .app-box { border: 2px solid var(--gold); height: 100%; background: #000; border-radius: 20px; padding: 30px; position: relative; }
    </style>
</head>
<body>

<div class="container">
    <div class="panel">
        <h3 style="text-align: center; border-bottom: 1px solid #333;">SYSTEM_VITALS</h3>
        <div class="radar"></div>
        <div style="margin-top: 20px;">
            <label>CORE_LOAD: <span id="load-val">0</span>%</label>
            <div class="pulse-bar"><div id="load-fill" class="pulse-fill"></div></div>
        </div>
        <div style="margin-top: 20px; font-size: 11px;">
            STATUS: <span style="color: var(--neon); animation: blink 1s infinite;">[ ONLINE ]</span><br>
            ENCRYPTION: AES-512-OMEGA
        </div>
    </div>

    <div class="panel" style="overflow-y: auto;">
        <h2 style="text-align: center; color: var(--red);">$50,000,000 ASSET</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            {% for p in protocols %}
            <div class="card" onclick="launchApp('{{ p.id }}', '{{ p.ar }}')">
                <i style="font-size: 2rem;">{{ p.icon }}</i><br>
                <strong>{{ p.id }}</strong><br>
                <small>{{ p.ar }}</small>
            </div>
            {% endfor %}
        </div>
    </div>

    <div class="panel">
        <h3 style="text-align: center; border-bottom: 1px solid #333;">LIVE_SECURITY_FEED</h3>
        <div id="log-feed"></div>
    </div>
</div>

<div id="app-overlay">
    <div class="app-box">
        <button onclick="closeApp()" style="position: absolute; top: 20px; left: 20px; background: var(--red); color: #fff; border: none; padding: 10px 20px; cursor: pointer;">إغلاق Session X</button>
        <div id="app-body" style="color: var(--neon); font-family: monospace; margin-top: 50px;"></div>
    </div>
</div>

<script>
    // 1. محاكي سجل العمليات الحي
    const logFeed = document.getElementById('log-feed');
    const logs = [
        "> INITIALIZING_QUANTUM_BRIDGE...",
        "> SCANNING_NETWORK_FOR_INTRUSIONS...",
        "> WHALE_WALLET_DETECTED: 0x71...F2",
        "> SYNCING_WITH_SOVEREIGN_CORE...",
        "> P12_SHIELD_STATUS: STABLE",
        "> ENCRYPTING_SESSION_DATA..."
    ];

    setInterval(() => {
        const line = document.createElement('div');
        line.innerText = logs[Math.floor(Math.random() * logs.length)];
        logFeed.prepend(line);
        if(logFeed.childNodes.length > 20) logFeed.removeChild(logFeed.lastChild);
        
        // تحديث العدادات
        const load = Math.floor(Math.random() * 20) + 10;
        document.getElementById('load-val').innerText = load;
        document.getElementById('load-fill').style.width = load + "%";
    }, 2000);

    // 2. تشغيل التطبيقات المستقلة بهيبة
    function launchApp(id, name) {
        document.getElementById('app-overlay').style.display = 'block';
        const body = document.getElementById('app-body');
        body.innerHTML = `<h2>جاري تشغيل تطبيق: ${name} (${id})</h2>
                          <hr style='border: 1px solid #222;'>
                          <p>> تم إنشاء بيئة معزولة (Sandbox).</p>
                          <p>> حالة البروتوكول: <span style='color:white'>نشط وسري</span></p>
                          <p>> المراقبة: تعمل بنظام التشفير السيادي المحفوظ.</p>`;
    }

    function closeApp() { document.getElementById('app-overlay').style.display = 'none'; }

    // 3. حماية P12 (الهجوم المضاد) - تم إصلاحها لتعمل دون تجميد المتصفح
    setInterval(() => {
        const start = Date.now();
        debugger; 
        if (Date.now() - start > 100) {
            document.body.innerHTML = "<div style='background:red; color:white; height:100vh; display:flex; align-items:center; justify-content:center;'><h1>تم اكتشاف محاولة اختراق! بروتوكول P12 فعال.</h1></div>";
        }
    }, 1000);
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

if __name__ == "__main__":
    app.run()
