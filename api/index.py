from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

# الإعدادات السيادية [cite: 2026-02-04]
self_master_key = 'GENERAL_EYE_ONLY_VALIDATION_STRING'

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL | COMMAND</title>
    <style>
        :root { --gold: #d4af37; --bg: #050505; }
        body { background: var(--bg); color: #fff; font-family: sans-serif; margin: 0; padding: 10px; }
        .header { border-bottom: 2px solid var(--gold); text-align: center; padding: 10px; }
        .valuation { color: var(--gold); font-size: 1.8rem; font-weight: bold; margin: 10px 0; }
        .lang-toggle { background: var(--gold); color: #000; border: none; padding: 5px 10px; cursor: pointer; font-weight: bold; margin-bottom: 10px; }
        .panel { border: 1px solid var(--gold); padding: 15px; background: rgba(20,20,20,0.9); margin-top: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(60px, 1fr)); gap: 5px; margin-top: 15px; }
        .p-btn { background: transparent; color: var(--gold); border: 1px solid var(--gold); padding: 10px; cursor: pointer; }
        #popup { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80%; background: #000; border: 3px solid var(--gold); z-index: 1000; padding: 20px; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <button class="lang-toggle" onclick="toggleLang()">LANGUAGE / لغة</button>
        <h1 id="main-title">IMPERIAL GENERAL</h1>
        <div class="valuation">$50,000,000.00</div>
    </div>
    <div class="panel">
        <h3 id="radar-title">STRATEGIC RADAR</h3>
        <div id="radar-feed" style="height: 150px; overflow-y: auto; font-family: monospace; font-size: 12px; color: #00ff41;"></div>
    </div>
    <div class="panel">
        <h3 id="modules-title">TACTICAL MODULES (P1-P70)</h3>
        <div class="grid" id="module-grid"></div>
    </div>
    <div id="popup">
        <h2 style="color: var(--gold)">ACQUISITION PROTOCOL</h2>
        <p id="popup-text"></p>
        <button onclick="closePopup()" style="background: var(--gold); border: none; padding: 10px 20px; cursor: pointer;">ACKNOWLEDGE</button>
    </div>
    <script>
        let currentLang = 'en';
        const texts = {
            en: { title: "IMPERIAL GENERAL", radar: "STRATEGIC RADAR", modules: "TACTICAL MODULES" },
            ar: { title: "الجنرال الإمبراطوري", radar: "رادار الرصد الاستراتيجي", modules: "الوحدات التكتيكية" }
        };
        function toggleLang() {
            currentLang = currentLang === 'en' ? 'ar' : 'en';
            document.getElementById('main-title').innerText = texts[currentLang].title;
            document.getElementById('radar-title').innerText = texts[currentLang].radar;
            document.getElementById('modules-title').innerText = texts[currentLang].modules;
        }
        function closePopup() { document.getElementById('popup').style.display = 'none'; }
        const grid = document.getElementById('module-grid');
        for(let i=1; i<=70; i++) {
            let b = document.createElement('button'); b.className = 'p-btn'; b.innerText = 'P' + i;
            b.onclick = () => execute(i); grid.appendChild(b);
        }
        async function execute(id) {
            const res = await fetch(`/api/general?code=P${id}&key=GENERAL_EYE_ONLY_VALIDATION_STRING`);
            const data = await res.json();
            const feed = document.getElementById('radar-feed');
            feed.innerHTML = `> ${data.msg}<br>` + feed.innerHTML;
            if(id === 70) {
                document.getElementById('popup-text').innerText = data.msg;
                document.getElementById('popup').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CONTENT)

@app.route('/api/general')
def logic():
    key = request.args.get('key')
    code = request.args.get('code', 'P1')
    if key != self_master_key: return jsonify({"msg": "ACCESS DENIED"})
    num = int(code[1:])
    if num == 70: return jsonify({"msg": "WHALE PROTOCOL: $50M ACQUISITION SECURED."})
    return jsonify({"msg": f"Module {code} operational."})

# التوجيه النهائي لـ Vercel بدون مسافات
app = app
