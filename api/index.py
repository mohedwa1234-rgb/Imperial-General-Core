from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

# MASTER CONFIGURATION
MASTER_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING' [cite: 2026-02-04]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL | COMMAND CENTER</title>
    <style>
        :root { --gold: #d4af37; --bg: #050505; --green: #00ff41; }
        body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 10px; }
        .header { border-bottom: 2px solid var(--gold); padding: 15px; text-align: center; }
        .valuation { color: var(--gold); font-size: 1.5rem; font-weight: bold; margin: 10px 0; }
        .lang-bar { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
        .lang-btn { background: transparent; border: 1px solid var(--gold); color: var(--gold); cursor: pointer; padding: 5px 10px; font-size: 11px; }
        .panel { border: 1px solid var(--gold); padding: 12px; background: rgba(20,20,20,0.8); margin-bottom:10px; }
        .radar-log { height: 180px; overflow-y: auto; font-family: monospace; font-size: 12px; background: #000; padding: 5px; border: 1px solid #222; }
        .hex-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(55px, 1fr)); gap: 5px; }
        .p-btn { background: transparent; color: var(--gold); border: 1px solid var(--gold); padding: 8px 0; cursor: pointer; font-size: 11px; transition: 0.3s; }
        .p-btn:hover { background: var(--gold); color: #000; }
        #popup { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 999; align-items: center; justify-content: center; }
    </style>
</head>
<body>
<div class="header">
    <h1 id="title">IMPERIAL GENERAL</h1>
    <div class="valuation">$50,000,000.00</div>
    <div class="lang-bar">
        <button class="lang-btn" onclick="setLang('ar')">العربية</button>
        <button class="lang-btn" onclick="setLang('en')">English</button>
        <button class="lang-btn" onclick="setLang('ru')">Русский</button>
        <button class="lang-btn" onclick="setLang('zh')">中文</button>
        <button class="lang-btn" onclick="setLang('ja')">日本語</button>
    </div>
</div>
<div class="panel">
    <h3 id="label-radar">STRATEGIC RADAR</h3>
    <div id="radar" class="radar-log"></div>
</div>
<div class="panel">
    <h3 id="label-modules">TACTICAL MODULES (P1-P70)</h3>
    <div class="hex-grid" id="grid"></div>
</div>
<div id="popup"><div style="border:2px solid var(--gold); padding:30px; text-align:center; background:#000;">
    <h2 style="color:var(--gold);">ACQUISITION ALERT</h2>
    <p id="pop-msg"></p>
    <button onclick="document.getElementById('popup').style.display='none'" style="background:var(--gold); padding:10px 20px; border:none; cursor:pointer; font-weight:bold;">CONFIRM</button>
</div></div>
<script>
    const TRANSLATIONS = {
        ar: { title: "الجنرال الإمبراطوري", radar: "رادار الرصد الاستراتيجي", modules: "الوحدات التكتيكية" },
        en: { title: "IMPERIAL GENERAL", radar: "STRATEGIC RADAR", modules: "TACTICAL MODULES" },
        ru: { title: "ИМПЕРСКИЙ ГЕНЕРАЛ", radar: "СТРАТЕГИЧЕСКИЙ РАДАР", modules: "МОДУЛИ" },
        zh: { title: "帝国将军", radar: "战略雷达", modules: "战术模块" },
        ja: { title: "帝国将軍", radar: "戦略レーダー", modules: "戦術モジュール" }
    };
    function setLang(l) {
        document.getElementById('title').innerText = TRANSLATIONS[l].title;
        document.getElementById('label-radar').innerText = TRANSLATIONS[l].radar;
        document.getElementById('label-modules').innerText = TRANSLATIONS[l].modules;
    }
    const grid = document.getElementById('grid');
    for(let i=1; i<=70; i++) {
        let b = document.createElement('button'); b.className = 'p-btn'; b.innerText = 'P' + i;
        b.onclick = () => execute(i); grid.appendChild(b);
    }
    async function execute(id) {
        const res = await fetch(`/api/general?code=P${id}&key=GENERAL_EYE_ONLY_VALIDATION_STRING`);
        const data = await res.json();
        const entry = document.createElement('div');
        entry.innerHTML = `<span style="color:var(--gold)">[${new Date().toLocaleTimeString()}]</span> > ${data.msg}`;
        document.getElementById('radar').prepend(entry);
        if(id === 70) { document.getElementById('pop-msg').innerText = data.msg; document.getElementById('popup').style.display = 'flex'; }
    }
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/general')
def api_logic():
    code = request.args.get('code', 'P1')
    key = request.args.get('key', '')
    if key != MASTER_KEY: return jsonify({"msg": "UNAUTHORIZED."})
    num = int(code[1:])
    if num == 70: return jsonify({"msg": "GOLDEN PROTOCOL: $50,000,000 ACQUISITION CONFIRMED."})
    return jsonify({"msg": f"Module {code} operational. Analyzing whale data..."})

# لا تضف أي مسافات هنا، السطر القادم هو مفتاح التشغيل
app = app
