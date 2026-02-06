from flask import Flask, render_template_string, request, jsonify
import random
import datetime

app = Flask(__name__)

# ==========================================
# CONFIGURATION & SECURITY
# ==========================================
MASTER_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING'

# ==========================================
# IMPERIAL FRONTEND (HTML/CSS/JS)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL | SOVEREIGNTY</title>
    <style>
        :root {
            --gold: #d4af37;
            --gold-dim: rgba(212, 175, 55, 0.1);
            --bg: #050505;
            --glass: rgba(10, 10, 10, 0.9);
        }
        * { box-sizing: border-box; }
        body { 
            background: var(--bg); 
            color: #fff; 
            font-family: 'Segoe UI', serif; 
            margin: 0; 
            padding: 10px;
            overflow-x: hidden;
            background-image: radial-gradient(circle at top, #1a1a1a 0%, #000 80%);
        }

        /* HEADER SECTION */
        .imperial-header {
            border-bottom: 2px solid var(--gold);
            padding-bottom: 15px;
            margin-bottom: 20px;
            text-align: center;
        }
        .main-title {
            color: var(--gold);
            letter-spacing: 3px;
            font-size: 1.5rem;
            margin: 0;
            text-transform: uppercase;
        }
        .valuation {
            font-family: 'Courier New', monospace;
            font-size: 1.2rem;
            color: #fff;
            background: var(--gold-dim);
            border: 1px solid var(--gold);
            padding: 5px 10px;
            margin-top: 10px;
            display: inline-block;
        }
        .status-line {
            color: #00ff41;
            font-size: 0.8rem;
            margin-top: 5px;
            letter-spacing: 1px;
        }

        /* MAIN LAYOUT */
        .dashboard-grid {
            display: flex;
            flex-direction: column; /* Mobile First */
            gap: 15px;
        }
        
        @media (min-width: 768px) {
            .dashboard-grid {
                flex-direction: row;
            }
        }

        /* RADAR & INFO PANELS */
        .panel {
            background: var(--glass);
            border: 1px solid var(--gold);
            padding: 15px;
            border-radius: 4px;
            flex: 1;
        }
        
        .radar-log {
            height: 200px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            border-top: 1px solid #333;
            padding-top: 10px;
        }
        .log-entry { margin-bottom: 5px; border-bottom: 1px solid #111; padding-bottom: 2px; }
        .time-stamp { color: var(--gold); margin-right: 5px; }

        /* PROTOCOL GRID */
        .hex-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
            gap: 8px;
            margin-top: 20px;
        }
        .hex-btn {
            background: transparent;
            color: var(--gold);
            border: 1px solid var(--gold);
            padding: 10px 0;
            font-size: 10px;
            cursor: pointer;
            transition: 0.3s;
        }
        .hex-btn:hover {
            background: var(--gold);
            color: #000;
        }

        /* POPUP SYSTEM */
        #sov-popup {
            display: none;
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 9999;
            align-items: center; justify-content: center;
            flex-direction: column;
            text-align: center;
            padding: 20px;
        }
        .popup-box {
            border: 4px solid var(--gold);
            padding: 30px;
            background: #000;
            max-width: 90%;
            box-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
        }
    </style>
</head>
<body>

    <div class="imperial-header">
        <h1 class="main-title">Imperial General</h1>
        <div class="valuation">$50,000,000.00</div>
        <div class="status-line">SOVEREIGNTY ACTIVE / سيادة كاملة</div>
    </div>

    <div class="dashboard-grid">
        <div class="panel">
            <h3 style="color:var(--gold); margin-top:0;">STRATEGIC RADAR</h3>
            <div id="radar-feed" class="radar-log">
                <div class="log-entry">SYSTEM INITIALIZED...</div>
            </div>
        </div>

        <div class="panel" style="flex: 0.6;">
            <h3 style="color:var(--gold); margin-top:0;">SPECS</h3>
            <div style="font-size: 0.8rem; color: #ccc; line-height: 1.6;">
                > CORE: <span style="color:#00ff41">ONLINE</span><br>
                > KEY: PROTECTED<br>
                > WHALE_MODE: READY
            </div>
        </div>
    </div>

    <div class="panel" style="margin-top: 15px;">
        <h3 style="color:var(--gold); margin-top:0;">TACTICAL MODULES (P1-P70)</h3>
        <div class="hex-grid" id="modules-container"></div>
    </div>

    <div id="sov-popup">
        <div class="popup-box">
            <h2 style="color: var(--gold); font-size: 2rem; margin-bottom: 10px;">ACQUISITION ALERT</h2>
            <p id="popup-text" style="color: #fff; font-size: 1.2rem; margin-bottom: 20px;"></p>
            <button onclick="document.getElementById('sov-popup').style.display='none'" 
                    style="background:var(--gold); border:none; padding:15px 40px; font-weight:bold; cursor:pointer;">
                ACKNOWLEDGE
            </button>
        </div>
    </div>

    <script>
        const API_KEY = 'GENERAL_EYE_ONLY_VALIDATION_STRING';

        // Initialize Buttons
        const grid = document.getElementById('modules-container');
        for(let i=1; i<=70; i++) {
            let btn = document.createElement('button');
            btn.className = 'hex-btn';
            btn.innerText = 'P' + i;
            btn.onclick = () => execute(i);
            grid.appendChild(btn);
        }

        async function execute(id) {
            const feed = document.getElementById('radar-feed');
            
            // Optimistic UI Update (Instant Feedback)
            const loading = document.createElement('div');
            loading.className = 'log-entry';
            loading.innerHTML = `<span class="time-stamp">>></span> Executing P${id}...`;
            feed.prepend(loading);

            try {
                const res = await fetch(`/api/general?code=P${id}&key=${API_KEY}`);
                const data = await res.json();
                
                loading.innerHTML = `<span class="time-stamp">[${new Date().toLocaleTimeString()}]</span> ${data.msg}`;
                
                if(data.type === 'ALERT') {
                    document.getElementById('popup-text').innerText = data.msg;
                    document.getElementById('sov-popup').style.display = 'flex';
                }
            } catch (err) {
                loading.innerText = "CONNECTION LOST.";
                loading.style.color = "red";
            }
        }
    </script>
</body>
</html>
"""

# ==========================================
# BACKEND LOGIC (FLASK)
# ==========================================
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/general')
def api_logic():
    code = request.args.get('code', 'P1')
    key = request.args.get('key', '')
    
    # Security Check
    if key != MASTER_KEY:
        return jsonify({"type": "ERROR", "msg": "UNAUTHORIZED ACCESS DETECTED."})

    # Business Logic
    if code == 'P70':
        return jsonify({
            "type": "ALERT", 
            "msg": "SOVEREIGNTY ESTABLISHED. $50M ACQUISITION PROTOCOL READY."
        })
    
    elif code == 'P1':
        val = random.randint(10, 90)
        return jsonify({
            "type": "INFO", 
            "msg": f"Whale Flow Detected: ${val}M Capital Injection."
        })
        
    else:
        return jsonify({
            "type": "INFO", 
            "msg": f"Module {code} operational. Analyzing market data..."
        })

# Vercel requires the app to be exposed
if __name__ == '__main__':
    app.run()
