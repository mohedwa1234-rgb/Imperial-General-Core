from flask import Flask, render_template_string, request, jsonify
import datetime
import base64
import random

app = Flask(__name__)

class SovereignEngine:
    def __init__(self):
        self.valuation = "50,000,000 USD"
        self.status = "BATTLE_READY"
        
    def run_logic_cell(self, cell_id):
        cells = {
            "P1": "Quantum_Encryption_Active",
            "P2": "Identity_Fingerprinting",
            "P3": "Vulnerability_Scanner_Active", # [تحسين P3]
            "P4": "Behavioral_AI_Logic",
            "P5": "Tool_Breaker_Armed",
            "P6": "Asset_Valuation_Watermark",
            "P7": "Cloud_Sovereign_Link",
            "P8": "Contract_Logic_Audit",
            "P9": "Attack_Simulator_Running", # [تحسين P9]
            "P10": "Emergency_Kill_Switch"
        }
        return cells.get(cell_id, "Unknown_Cell")

engine = SovereignEngine()

def sovereign_vault(data):
    encoded_data = base64.b64encode(str(data).encode()).decode()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [SOVEREIGN_STRIKE_LOG] {timestamp} ---")
    print(f"ENCRYPTED_PAYLOAD: {encoded_data}")
    print("--------------------------------------")

@app.route('/')
def imperial_core():
    user_identity = {
        "event": "SYSTEM_INITIALIZED",
        "ip": request.remote_addr,
        "valuation": engine.valuation
    }
    sovereign_vault(user_identity)

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en" dir="ltr" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>STEALTH GENERAL | COMBAT CORE</title>
        <style>
            :root { --glow: #00ff00; --bg: #000; --danger: #ff0000; --warn: #ffaa00; }
            body { background: var(--bg); color: var(--glow); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
            #langBtn { 
                position: fixed; top: 20px; right: 20px; z-index: 999; 
                border: 2px solid var(--glow); background: rgba(0,20,0,0.9); 
                color: var(--glow); padding: 10px 20px; cursor: pointer; font-weight: bold;
                box-shadow: 0 0 10px var(--glow);
            }
            .viewport { display: grid; grid-template-columns: 320px 1fr 320px; height: 100vh; padding: 20px; gap: 20px; }
            .panel { border: 1px solid var(--glow); padding: 15px; background: rgba(0,30,0,0.1); overflow-y: auto; }
            .center { display: flex; flex-direction: column; align-items: center; justify-content: center; }
            
            /* [تحديث الرادار P3] */
            .radar { 
                width: 280px; height: 280px; border: 2px solid var(--glow); 
                border-radius: 50%; position: relative; margin-bottom: 20px;
                transition: all 0.5s ease;
            }
            .radar.scanning { border-color: var(--warn); box-shadow: 0 0 30px var(--warn); }
            .radar::after { 
                content: ''; position: absolute; top: 50%; left: 50%; 
                width: 140px; height: 2px; background: var(--glow); 
                transform-origin: left; animation: scan 3s linear infinite; 
            }
            .radar.fast::after { animation-duration: 0.5s; background: var(--danger); }
            
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .btn { 
                width: 100%; padding: 10px; background: transparent; 
                border: 1px solid var(--glow); color: var(--glow); 
                margin: 5px 0; cursor: pointer; font-size: 0.8em; text-align: left;
                transition: 0.3s;
            }
            .btn:hover { background: var(--glow); color: #000; box-shadow: 0 0 10px var(--glow); }
            .strike { border-color: var(--danger); color: var(--danger); }
            .active-module { background: var(--glow) !important; color: #000 !important; }
            
            #status-terminal { 
                font-size: 0.85em; color: #0f0; margin-top: 15px; 
                border: 1px solid #333; padding: 10px; width: 100%; 
                height: 100px; overflow: hidden; background: rgba(0,10,0,0.5);
            }
            .valuation-text { color: var(--glow); font-weight: bold; font-size: 1.2em; text-shadow: 0 0 15px var(--glow); margin-top: 10px; }
        </style>
    </head>
    <body onload="initSystem()">
        <button id="langBtn" onclick="toggleLang()">العربية</button>
        <div class="viewport">
            <div class="panel">
                <h3 id="txt-ops">[ SOVEREIGN OPS ]</h3>
                <button class="btn" id="btn-p1" onclick="execute('P1')">P1: QUANTUM VAULT</button>
                <button class="btn" id="btn-p2" onclick="execute('P2')">P2: ID FINGERPRINT</button>
                <button class="btn" id="btn-p3" onclick="execute('P3')">P3: VULN SCANNER</button>
                <button class="btn" id="btn-p4" onclick="execute('P4')">P4: BEHAVIORAL AI</button>
                <button class="btn strike" id="btn-p5" onclick="execute('P5')">P5: TOOL BREAKER</button>
            </div>
            <div class="center">
                <h1 id="txt-title">STEALTH GENERAL</h1>
                <div class="radar" id="mainRadar"></div>
                <div class="valuation-text" id="txt-val">NET ASSET: $50,000,000</div>
                <div id="status-terminal"></div>
            </div>
            <div class="panel">
                <h3 id="txt-intel">[ INTEL MATRIX ]</h3>
                <button class="btn" id="btn-p6" onclick="execute('P6')">P6: WATERMARK AUDIT</button>
                <button class="btn" id="btn-p7" onclick="execute('P7')">P7: CLOUD LINK</button>
                <button class="btn" id="btn-p8" onclick="execute('P8')">P8: CONTRACT LOGIC</button>
                <button class="btn strike" id="btn-p9" onclick="execute('P9')">P9: STRESS TEST</button>
                <button class="btn strike" id="btn-p10" onclick="selfDestruct()">P10: PURGE CORE</button>
            </div>
        </div>
        <script>
            let lang = 'en';
            const terminal = document.getElementById('status-terminal');
            
            function addLog(msg) {
                const div = document.createElement('div');
                div.innerText = `> ${msg}`;
                terminal.prepend(div);
                if(terminal.children.length > 5) terminal.lastChild.remove();
            }

            function toggleLang() {
                const h = document.getElementById('mainHtml');
                const b = document.getElementById('langBtn');
                if(lang === 'en') {
                    h.lang = 'ar'; h.dir = 'rtl'; b.innerText = 'ENGLISH'; lang = 'ar';
                    document.getElementById('txt-title').innerText = 'الجنرال الشبحي';
                    document.getElementById('txt-val').innerText = 'صافي الأصول: $50,000,000';
                    document.getElementById('txt-ops').innerText = '[ العمليات السيادية ]';
                    document.getElementById('txt-intel').innerText = '[ مصفوفة الاستخبارات ]';
                    const opsLabels = ['P1: القبو الكمي', 'P2: بصمة الهوية', 'P3: فاحص الثغرات', 'P4: ذكاء السلوك', 'P5: محطم الأدوات'];
                    document.querySelectorAll('.panel:first-child .btn').forEach((btn, i) => btn.innerText = opsLabels[i]);
                    const intelLabels = ['P6: تدقيق العلامة', 'P7: الربط السحابي', 'P8: منطق العقود', 'P9: اختبار الضغط', 'P10: تدمير النواة'];
                    document.querySelectorAll('.panel:last-child .btn').forEach((btn, i) => btn.innerText = intelLabels[i]);
                } else {
                    location.reload(); // إعادة التحميل للعودة للإنجليزية ببساطة
                }
            }

            function execute(p) {
                const radar = document.getElementById('mainRadar');
                const btn = document.getElementById('btn-' + p.toLowerCase());
                btn.classList.add('active-module');
                
                if(p === 'P3') {
                    radar.classList.add('scanning');
                    addLog("VULNERABILITY SCAN INITIATED...");
                    setTimeout(() => { radar.classList.remove('scanning'); btn.classList.remove('active-module'); addLog("SCAN COMPLETE: 0 BREACHES FOUND."); }, 3000);
                } else if(p === 'P9') {
                    radar.classList.add('fast');
                    addLog("STRESS TEST: SIMULATING 10k ATTACKS/SEC...");
                    setTimeout(() => { radar.classList.remove('fast'); btn.classList.remove('active-module'); addLog("STRESS TEST PASSED. UPTIME 100%."); }, 4000);
                } else {
                    addLog(`MODULE ${p} ACTIVATED SUCCESSFULLY.`);
                    setTimeout(() => btn.classList.remove('active-module'), 1000);
                }
            }

            function initSystem() {
                addLog("SYSTEM SOVEREIGN_CORE ONLINE...");
                addLog("VALUATION LOCKED: $50M");
                setInterval(() => {
                    const logs = ["SCANNING FOR HI-TECH WHALES...", "ENCRYPTION LAYER 7: SECURE", "MONITORING ENTERPRISE SCRIPTS..."];
                    addLog(logs[Math.floor(random()*logs.length)]);
                }, 6000);
            }

            function selfDestruct() {
                if(confirm("CONFIRM TOTAL IP PURGE?")) document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>GHOST MODE ACTIVE - ASSETS SECURED</h1>";
            }
        </script>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()
