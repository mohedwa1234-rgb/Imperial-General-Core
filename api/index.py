from flask import Flask, render_template_string, request, jsonify
import base64

app = Flask(__name__)

# المفتاح الذي أصبح للاطلاع فقط (Read-Only)
INSPECTION_KEY = 'MohEdwa2026' 
# مفتاح التنفيذ الحقيقي (لا يعرفه أحد غيرك)
EXECUTIVE_KEY = 'GENERAL_PRIVATE_ACCESS_2026'

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>IMPERIAL GENERAL | INSPECTION MODE</title>
    <style>
        body { background: #050505; color: #d4af37; font-family: 'Courier New', monospace; text-align: center; }
        .fortress { border: 2px solid #d4af37; padding: 20px; margin: 20px auto; max-width: 600px; }
        .log { height: 150px; overflow-y: auto; background: #000; color: #00ff41; padding: 10px; text-align: left; border: 1px solid #333; }
        .btn { background: transparent; color: #d4af37; border: 1px solid #d4af37; padding: 10px; cursor: pointer; width: 60px; margin: 2px; }
        .warning { color: #ff4444; font-weight: bold; margin-top: 10px; display: none; }
    </style>
</head>
<body>
    <div class="fortress">
        <h1>IMPERIAL CORE - AUDIT MODE</h1>
        <div id="log" class="log">> SYSTEM: STANDBY<br>> AUDIT_KEY: ACTIVE</div>
        <div id="warning" class="warning">ERROR: INSUFFICIENT PRIVILEGES FOR EXECUTION</div>
        <div style="margin-top: 20px;">
            <script>
                for(let i=1; i<=70; i++) document.write(`<button class="btn" onclick="run(${i})">P${i}</button>`);
            </script>
        </div>
    </div>
    <script>
        async function run(id) {
            const payload = btoa('MohEdwa2026'); // إرسال مفتاح الاطلاع
            const res = await fetch(`/api/general?code=P${id}&payload=${payload}`);
            const data = await res.json();
            
            const log = document.getElementById('log');
            const warn = document.getElementById('warning');
            
            log.innerHTML = `> [LOG] Unit P${id}: ${data.msg}<br>` + log.innerHTML;
            
            if(data.status === "restricted") {
                warn.style.display = 'block';
                setTimeout(() => { warn.style.display = 'none'; }, 2000);
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

@app.route('/api/general')
def logic():
    payload = request.args.get('payload', '')
    code = request.args.get('code', '')
    
    try:
        decoded_input = base64.b64decode(payload).decode('utf-8')
        
        # إذا استخدموا المفتاح الذي معك (MohEdwa2026)
        if decoded_input == INSPECTION_KEY:
            return jsonify({
                "msg": "VIEW ONLY MODE: Command Blocked by Sovereign Protocol.",
                "status": "restricted"
            })
            
        # فقط المفتاح السري الجديد يمكنه التنفيذ (Executive Access)
        elif decoded_input == EXECUTIVE_KEY:
            if code == "P70":
                return jsonify({"msg": "GOLDEN PROTOCOL: $50M SECURED", "status": "executed"})
            return jsonify({"msg": f"Unit {code} Operational", "status": "executed"})
            
        return jsonify({"msg": "UNAUTHORIZED"}), 403
    except:
        return jsonify({"msg": "ENCRYPTION ERROR"}), 400

app = app
