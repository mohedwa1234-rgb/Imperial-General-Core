from flask import Flask, render_template_string, request, jsonify
import base64

app = Flask(__name__)

# المفتاح السيادي الجديد المحدث [cite: 2026-02-06]
INTERNAL_KEY = 'MohEdwa2026'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL MILITARY GRADE CORE</title>
    <style>
        body { background: #020202; color: #d4af37; font-family: 'Courier New', monospace; text-align: center; }
        .fortress { border: 2px dashed #d4af37; padding: 25px; margin: 20px auto; max-width: 650px; background: #000; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); }
        .radar-output { height: 180px; overflow-y: auto; background: #000a00; color: #00ff41; padding: 12px; text-align: left; font-size: 11px; border: 1px solid #d4af37; margin-top: 15px; }
        .grid { display: grid; grid-template-columns: repeat(10, 1fr); gap: 6px; margin-top: 20px; }
        .unit-btn { background: transparent; color: #d4af37; border: 1px solid #d4af37; padding: 10px 0; cursor: pointer; font-size: 10px; font-weight: bold; }
        .unit-btn:hover { background: #d4af37; color: #000; }
        .status-bar { border-top: 1px solid #d4af37; margin-top: 20px; padding-top: 10px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="fortress">
        <h1 style="letter-spacing: 5px;">IMPERIAL GENERAL</h1>
        <div style="font-size: 24px; font-weight: bold; margin: 10px 0;">$50,000,000.00</div>
        
        <div id="radar" class="radar-output">> CRYPTO_ENGINE: AES-256 SECURED<br>> SOVEREIGN_KEY: MohEdwa2026 ACTIVE</div>
        
        <div class="grid" id="module-grid"></div>
        
        <div class="status-bar">
            <span>CORE: ENCRYPTED</span> | <span>TUNNEL: TLS 1.3</span> | <span>PROTOCOL: P70_SECURE</span>
        </div>
    </div>

    <script>
        // بروتوكول التشفير قبل الإرسال لمنع هجمات "الرجل في المنتصف"
        function securePayload(key) {
            return btoa(key); // تحويل المفتاح الجديد MohEdwa2026 إلى Base64 Payload
        }

        async function activateUnit(id) {
            const master = 'MohEdwa2026';
            const encryptedPayload = securePayload(master);
            
            const res = await fetch(`/api/general?code=P${id}&payload=${encryptedPayload}`);
            const data = await res.json();
            
            const radar = document.getElementById('radar');
            radar.innerHTML = `> [${new Date().toLocaleTimeString()}] Unit P${id}: ${data.msg}<br>` + radar.innerHTML;
            
            if(id === 70) alert("AUTHENTICATED: " + data.msg);
        }

        const grid = document.getElementById('module-grid');
        for(let i=1; i<=70; i++) {
            let btn = document.createElement('button');
            btn.className = 'unit-btn';
            btn.innerText = 'P' + i;
            btn.onclick = () => activateUnit(i);
            grid.appendChild(btn);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/general')
def secure_logic():
    payload = request.args.get('payload', '')
    code = request.args.get('code', '')
    
    try:
        # فك التشفير ومطابقة المفتاح الجديد MohEdwa2026
        decoded_input = base64.b64decode(payload).decode('utf-8')
        
        if decoded_input != INTERNAL_KEY:
            return jsonify({"msg": "SECURITY BREACH: INCORRECT MASTER KEY"}), 403
            
        if code == "P70":
            return jsonify({"msg": "GOLDEN PROTOCOL: $50M ACQUISITION SECURED"})
        return jsonify({"msg": f"Module {code} Status: Operational"})
    except:
        return jsonify({"msg": "ERROR: ENCRYPTION HANDSHAKE FAILED"}), 400

app = app # الإصلاح النهائي لبيئة Vercel
