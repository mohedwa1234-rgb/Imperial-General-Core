from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

# مفتاح السيادة المشفر
MASTER_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING' [cite: 2026-02-04]

# الواجهة العالمية (5 لغات) مدمجة لتقليل استهلاك الموارد [cite: 2026-02-05]
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL | GLOBAL COMMAND</title>
    <style>
        :root { --gold: #d4af37; --bg: #050505; --green: #00ff41; }
        body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 10px; }
        .header { border-bottom: 2px solid var(--gold); padding: 15px; text-align: center; }
        .valuation { color: var(--gold); font-size: 1.5rem; font-weight: bold; margin: 10px 0; }
        .lang-bar { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
        .lang-btn { background: transparent; border: 1px solid var(--gold); color: var(--gold); cursor: pointer; padding: 4px 8px; font-size: 11px; }
        .dashboard { display: grid; grid-template-columns: 1fr; gap: 10px; }
        @media (min-width: 768px) { .dashboard { grid-template-columns: 2fr 1fr; } }
        .panel { border: 1px solid var(--gold); padding: 12px; background: rgba(20,20,20,0.8); }
        .radar-log { height: 200px; overflow-y: auto; font-family: monospace; font-size: 12px; background: #000; padding: 5px; }
        .hex-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(60px, 1fr)); gap: 5px; margin-top: 15px; }
        .p-btn { background: transparent; color: var(--gold); border: 1px solid var(--gold); padding: 10px 0; cursor: pointer; font-size: 12px; }
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
<div class="dashboard">
    <div class="panel">
        <h3 id="label-radar">STRATEGIC RADAR</h3>
        <div id="radar" class="radar-log"></div>
    </div>
    <div class="panel">
        <h3 id="label-specs">SYSTEM INTEGRITY</h3>
        <div id="specs">> CORE: ONLINE<br>> KEY: PROTECTED<br>> NODES: 70</div>
    </div>
</div>
<div class="panel" style="margin-top:15px;">
    <h3 id="label-modules">TACTICAL MODULES (P1-P70)</h3>
    <div class="hex-grid" id="grid"></div>
</div>
<div id="popup"><div style="border:2px solid var(--gold); padding:30px; text-align:center;">
    <h2 style="color:var(--gold);">ACQUISITION ALERT</h2>
    <p id="pop-msg"></p>
    <button onclick="document.getElementById('popup').style.display='none'" style="background:var(--gold); padding:10px 20px; border:none; cursor:pointer;">CONFIRM</button>
</div></div>
<script>
    const TRANSLATIONS = {
        ar: { title: "الجنرال الإمبراطوري", radar: "رادار الرصد", specs: "سلامة النظام", modules: "الوحدات التكتيكية" },
        en: { title: "IMPERIAL GENERAL", radar: "STRATEGIC RADAR", specs: "SYSTEM INTEGRITY", modules: "TACTICAL MODULES" },
        ru: { title: "ИМПЕРСКИЙ ГЕНЕРАЛ", radar: "РАДАР", specs: "ЦЕЛОСТНОСТЬ", modules: "МОДУЛИ" },
        zh: { title: "帝国将军", radar: "战略雷达", specs: "系统完整性", modules: "战术模块" },
        ja: { title: "帝国将軍", radar: "戦略レーダー", specs: "システム整合性", modules: "戦術モジュール" }
    };
    function setLang(l) {
        document.getElementById('title').innerText = TRANSLATIONS[l].title;
        document.getElementById('label-radar').innerText = TRANSLATIONS[l].radar;
        document.getElementById('label-specs').innerText = TRANSLATIONS[l].specs;
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
    if key != MASTER_KEY: return jsonify({"msg": "UNAUTHORIZED ACCESS."})
    num = int(code[1:])
    if num == 70: return jsonify({"msg": "GOLDEN PROTOCOL: $50,000,000 CONFIRMED."})
    elif 1 <= num <= 10: return jsonify({"msg": f"Unit {code}: Predictive Analysis Shift {random.randint(1,5)}%."})
    elif 11 <= num <= 30: return jsonify({"msg": f"Unit {code}: Cyber Shielding Level {random.randint(90,99)}%."})
    elif 31 <= num <= 50: return jsonify({"msg": f"Unit {code}: Whale Logic Engagement Active."})
    elif 51 <= num <= 69: return jsonify({"msg": f"Unit {code}: Logic Automation SYNC."})
    return jsonify({"msg": f"Module {code} operational."})

app = app # الإصلاح النهائي لبيئة Vercel بدون مسافات زائدة
