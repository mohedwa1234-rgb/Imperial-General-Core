from flask import Flask, render_template_string, request, jsonify
import datetime

app = Flask(__name__)

# بروتوكول التعقب والاشتباك السيادي
def log_strike(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [STRIKE_REPORT] {timestamp} ---")
    print(f"ACTION: {data}")
    print("--------------------------------------")

@app.route('/')
def imperial_core():
    # تعقب تلقائي صامت بمجرد الدخول
    log_strike({
        "event": "TARGET_LOCKED",
        "ip": request.remote_addr,
        "agent": request.headers.get('User-Agent')
    })
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en" dir="ltr" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>STEALTH GENERAL | SOVEREIGN DEFENSE</title>
        <style>
            :root { --glow: #00ff00; --bg: #000; --danger: #ff0000; --trap: #ffea00; }
            body { background: var(--bg); color: var(--glow); font-family: 'Courier New', monospace; margin: 0; overflow-x: hidden; }
            
            /* زر تبديل اللغة - ثابت في الأعلى */
            #langBtn { 
                position: fixed; top: 20px; right: 20px; z-index: 999999; 
                border: 2px solid var(--glow); background: rgba(0,20,0,0.9); 
                color: var(--glow); padding: 10px 20px; cursor: pointer; 
                font-weight: bold; box-shadow: 0 0 15px var(--glow);
            }

            .viewport { display: grid; grid-template-columns: 300px 1fr 300px; height: 100vh; padding: 20px; gap: 20px; }
            .panel { border: 1px solid var(--glow); padding: 20px; background: rgba(0,30,0,0.2); }
            .center { display: flex; flex-direction: column; align-items: center; justify-content: center; }
            
            /* الرادار النشط */
            .radar { 
                width: 250px; height: 250px; border: 2px solid var(--glow); 
                border-radius: 50%; position: relative; margin-bottom: 20px;
            }
            .radar::after { 
                content: ''; position: absolute; top: 50%; left: 50%; 
                width: 125px; height: 2px; background: var(--glow); 
                transform-origin: left; animation: scan 2s linear infinite; 
            }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .btn { 
                width: 100%; padding: 12px; background: transparent; 
                border: 1px solid var(--glow); color: var(--glow); 
                margin: 8px 0; cursor: pointer; font-weight: bold; 
            }
            .btn:hover { background: var(--glow); color: #000; }
            .strike { border-color: var(--danger); color: var(--danger); }
            .strike:hover { background: var(--danger); color: #fff; }
            
            /* الفخاخ البرمجية - Honeypot */
            .honeypot { display: none; } 
            
            #status-terminal { font-size: 0.8em; color: #0f0; margin-top: 20px; border-top: 1px solid #333; padding-top: 10px; width: 100%; }
        </style>
    </head>
    <body onload="initSystem()">
        <button id="langBtn" onclick="toggleLang()">العربية</button>
        
        <a href="/admin/config/leaked" class="honeypot" rel="nofollow">Admin Access</a>

        <div class="viewport">
            <div class="panel">
                <h3 id="txt-arsenal">[ ARSENAL OPS ]</h3>
                <button class="btn" onclick="execute('SHD')" id="btn-shd">Orbital Shield: ACTIVE</button>
                <button class="btn strike" onclick="execute('ATK')" id="btn-atk">Counter-Strike: READY</button>
                <button class="btn strike" onclick="selfDestruct()" id="btn-dst">PURGE CORE</button>
            </div>

            <div class="center">
                <h1 id="txt-title">STEALTH GENERAL</h1>
                <div class="radar"></div>
                <div id="status-terminal">> INITIALIZING DEFENSE LAYERS...</div>
            </div>

            <div class="panel">
                <h3 id="txt-intel">[ INTEL & VALUATION ]</h3>
                <p id="txt-val" style="font-size: 1.2em;">NET WORTH: $50,000,000</p>
                <p id="txt-tracking">Tracking: OMNIPRESENT</p>
                <p id="txt-counter">Tool Breaker: STANDBY</p>
            </div>
        </div>

        <script>
            let lang = 'en';
            function toggleLang() {
                const h = document.getElementById('mainHtml');
                const b = document.getElementById('langBtn');
                if(lang === 'en') {
                    h.lang = 'ar'; h.dir = 'rtl'; b.innerText = 'ENGLISH'; lang = 'ar';
                    document.getElementById('txt-arsenal').innerText = '[ عمليات الترسانة ]';
                    document.getElementById('btn-shd').innerText = 'الدرع المداري: نشط';
                    document.getElementById('btn-atk').innerText = 'هجوم مضاد: جاهز';
                    document.getElementById('btn-dst').innerText = 'تدمير النواة';
                    document.getElementById('txt-title').innerText = 'الجنرال الشبحي';
                    document.getElementById('txt-intel').innerText = '[ الاستخبارات والتقييم ]';
                    document.getElementById('txt-val').innerText = 'القيمة الصافية: $50,000,000';
                    document.getElementById('txt-tracking').innerText = 'التعقب: كلي الوجود';
                    document.getElementById('txt-counter').innerText = 'محطم الأدوات: انتظار';
                } else {
                    h.lang = 'en'; h.dir = 'ltr'; b.innerText = 'العربية'; lang = 'en';
                    document.getElementById('txt-arsenal').innerText = '[ ARSENAL OPS ]';
                    document.getElementById('btn-shd').innerText = 'Orbital Shield: ACTIVE';
                    document.getElementById('btn-atk').innerText = 'Counter-Strike: READY';
                    document.getElementById('btn-dst').innerText = 'PURGE CORE';
                    document.getElementById('txt-title').innerText = 'STEALTH GENERAL';
                    document.getElementById('txt-intel').innerText = '[ INTEL & VALUATION ]';
                    document.getElementById('txt-val').innerText = 'NET WORTH: $50,000,000';
                    document.getElementById('txt-tracking').innerText = 'Tracking: OMNIPRESENT';
                    document.getElementById('txt-counter').innerText = 'Tool Breaker: STANDBY';
                }
            }

            function initSystem() {
                setInterval(() => {
                    const msgs = ["> SCANNING FOR HI-TECH WHALES...", "> ENCRYPTING IP LOGS...", "> TOOL BREAKER ARMED", "> CORE STABLE"];
                    document.getElementById('status-terminal').innerText = msgs[Math.floor(Math.random()*msgs.length)];
                }, 3000);
            }

            function execute(type) {
                alert("PROTOCOL " + type + " INITIATED. MONITORING INTERCEPTORS.");
            }

            function selfDestruct() {
                if(confirm("FINAL WARNING: PURGE ALL DATA?")) {
                    document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>SYSTEM PURGED - GHOST MODE ACTIVE</h1>";
                }
            }
        </script>
    </body>
    </html>
    ''')

# مسار الفخ (Honeypot) - أي دخول هنا سيحطم أداة المهاجم
@app.route('/admin/config/leaked')
def trap():
    log_strike({"event": "TOOL_BREAKER_TRIGGERED", "ip": request.remote_addr})
    # إرسال "قنبلة نصية" لتحطيم برامج الفحص
    return "X" * 10000000, 200 # إرسال بيانات ضخمة فجائية

if __name__ == "__main__":
    app.run()
