from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

# ==========================================
# CONFIGURATION & SECURITY
# ==========================================
# مفتاح التحقق السيادي
MASTER_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING' [cite: 2026-02-04]

# ==========================================
# IMPERIAL FRONTEND (ALL-IN-ONE)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL | GLOBAL COMMAND</title>
    <style>
        :root { --gold: #d4af37; --bg: #050505; --green: #00ff41; }
        * { box-sizing: border-box; }
        body { 
            background: var(--bg); color: #fff; font-family: 'Segoe UI', serif; 
            margin: 0; padding: 10px; overflow-x: hidden;
            background-image: radial-gradient(circle at top, #1a1a1a 0%, #000 90%);
        }
        .header { border-bottom: 2px solid var(--gold); padding: 20px; text-align: center; }
        .valuation { color: var(--gold); font-size: 1.8rem; font-weight: bold; text-shadow: 0 0 15px rgba(212,175,55,0.4); }
        
        /* نظام اللغات */
        .lang-bar { display: flex; justify-content: center; gap: 10px; margin: 15px 0; flex-wrap: wrap; }
        .lang-btn { background: transparent; border: 1px solid var(--gold); color: var(--gold); cursor: pointer; padding: 5px 10px; font-size: 12px; transition: 0.3s; }
        .lang-btn:hover { background: var(--gold); color: #000; }

        .dashboard { display: grid; grid-template-columns: 1fr; gap: 15px; margin-top: 20px; }
        @media (min-width: 768px) { .dashboard { grid-template-columns: 2fr 1fr; } }

        .panel { background: rgba(10,10,10,0.9); border: 1px solid var(--gold); padding: 15px; position: relative; }
        .radar-log { height: 250px; overflow-y: auto; font-family: 'Courier New', monospace; font-size: 13px; border-top: 1px solid #222; margin-top: 10px; }
        
        .hex-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(70px, 1fr)); gap: 8px; margin-top: 20px; }
        .p-btn { background: transparent; color: var(--gold); border: 1px solid var(--gold); padding: 12px 0; cursor: pointer; transition: 0.4s; font-weight: bold; }
        .p-btn:hover { background: var(--gold); color: #000; box-shadow: 0 0 15px var(--gold); }

        #popup { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.98); z-index: 9999; align-items: center; justify-content: center; }
        .popup-box { border: 3px solid var(--gold); padding: 40px; text-align: center; max-width: 90%; background: #000; }
    </style>
</head>
<body>

<div class="header">
    <h1 id="title" style="margin:0; letter-spacing:5px;">IMPERIAL GENERAL</h1>
    <div class="valuation">$50,000,000.00</div>
    <div id="status" style="color: var(--green); font-size: 12px; margin-top: 5px;">SYSTEM ONLINE / السيادة نشطة</div>
    
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
        <div id="specs" style="font-size: 12px; color: #888;">
            > CORE: <span style="color:var(--green)">ACTIVE</span><br>
            > AUTH: VERIFIED<br>
            > NODES: 70 STABLE
        </div>
    </div>
</div>

<div class="panel" style="margin-top:20px;">
    <h3 id="label-modules">TACTICAL MODULES (P1-P70)</h3>
    <div class="hex-grid" id="grid"></div>
</div>

<div id="popup">
    <div class="popup-box">
        <h2 id="pop-title" style="color:var(--gold);">ACQUISITION ALERT</h2>
        <p id="pop-msg" style="font-size: 1.2rem;"></p>
        <button onclick="document.getElementById('popup').style.display='none'" style="background:var(--gold); border:none; padding:15px 40px; font-weight:bold; cursor:pointer;">CONFIRM</button>
    </div>
</div>

<script>
    const KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING';
    const TRANSLATIONS = {
        ar: { title: "الجنرال الإمبراطوري", radar: "رادار الرصد الاستراتيجي", specs: "سلامة النظام", modules: "الوحدات التكتيكية (P1-P70)", pop: "تنبيه الاستحواذ", status: "السيادة نشطة" },
        en: { title: "IMPERIAL GENERAL", radar: "STRATEGIC RADAR", specs: "SYSTEM INTEGRITY", modules: "TACTICAL MODULES (P1-P70)", pop: "ACQUISITION ALERT", status: "SOVEREIGNTY ACTIVE" },
        ru: { title: "ИМПЕРСКИЙ ГЕНЕРАЛ", radar: "СТРАТЕГИЧЕСКИЙ РАДАР", specs: "ЦЕЛОСТНОСТЬ СИСТЕМЫ", modules: "ТАКТИЧЕСКИЕ МОДУЛИ", pop: "СИГНАЛ ПОГЛОЩЕНИЯ", status: "СУВЕРЕНИТЕТ АКТИВЕН" },
        zh: { title: "帝国将军", radar: "战略雷达", specs: "系统完整性", modules: "战术模块", pop: "收购警报", status: "主权激活" },
        ja: { title: "帝国将軍", radar: "戦略レーダー", specs: "システム整合性", modules: "戦術モジュール", pop: "買収アラート", status: "主権発動" }
    };

    function setLang(l) {
        const t = TRANSLATIONS[l];
        document.getElementById('title').innerText = t.title;
        document.getElementById('label-radar').innerText = t.radar;
        document.getElementById('label-specs').innerText = t.specs;
        document.getElementById('label-modules').innerText = t.modules;
        document.getElementById('pop-title').innerText = t.pop;
        document.getElementById('status').innerText = t.status;
    }

    const grid = document.getElementById('grid');
    for(let i=1; i<=70; i++) {
        let b = document.createElement('button');
        b.className = 'p-btn'; b.innerText = 'P' + i;
        b.onclick = () => execute(i);
        grid.appendChild(b);
    }

    async function execute(id) {
        const res = await fetch(`/api/general?code=P${id}&key=${KEY}`);
        const data = await res.json();
        const entry = document.createElement('div');
        entry.style.padding = "5px 0";
        entry.innerHTML = `<span style="color:var(--gold)">[${new Date().toLocaleTimeString()}]</span> > ${data.msg}`;
        document.getElementById('radar').prepend(entry);
        if(id === 70) {
            document.getElementById('pop-msg').innerText = data.msg;
            document.getElementById('popup').style.display = 'flex';
        }
    }
</script>
</body>
</html>
"""

# ==========================================
# BACKEND LOGIC (STRATEGIC ENGINE)
# ==========================================
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/general')
def api_logic():
    code = request.args.get('code', 'P1')
    key = request.args.get('key', '')
    
    if key != MASTER_KEY:
        return jsonify({"msg": "UNAUTHORIZED ACCESS."})

    num = int(code[1:])
    
    # تفصيل منطق الوحدات (P2 - P69) [cite: 2026-02-01]
    if num == 70:
        return jsonify({"msg": "GOLDEN PROTOCOL: $50,000,000 ACQUISITION CONFIRMED / تم تأكيد الاستحواذ"})
    elif 1 <= num <= 10:
        return jsonify({"msg": f"Unit {code}: Predictive Analysis - Market Shift {random.randint(1,5)}% detected."})
    elif 11 <= num <= 30:
        return jsonify({"msg": f"Unit {code}: Cyber Defense Grid - Shielding Level {random.randint(90,99)}%."})
    elif 31 <= num <= 50:
        return jsonify({"msg": f"Unit {code}: Whale Logic Engagement - Profiling Enterprise Acquirer..."})
    elif 51 <= num <= 69:
        return jsonify({"msg": f"Unit {code}: Cross-Platform Synchronization - Logic Automation ACTIVE."})
    
    return jsonify({"msg": f"Module {code} operational."})

if __name__ == '__main__':
    app.run()
