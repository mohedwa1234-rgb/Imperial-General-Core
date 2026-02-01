from flask import Flask, render_template_string, request, jsonify
import datetime

app = Flask(__name__)

# بروتوكول التعقب السيادي: تسجيل البيانات في سجلات النظام لضمان الاستقرار (Vercel Logs)
def log_sovereign(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [INTEL_REPORT] {timestamp} ---")
    print(f"METADATA: {data}")
    print("--------------------------------------")

@app.route('/')
def main_core():
    # تعقب صامت وتلقائي (IP ونوع الجهاز) بمجرد فتح الرابط
    log_sovereign({
        "event": "PROTOTYPE_ACCESS",
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent')
    })
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GENERAL CORE | M&A VALUATION $50M</title>
        <style>
            :root { --glow: #00ff00; --bg: #000; --danger: #ff0000; }
            body { background: var(--bg); color: var(--glow); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
            
            /* زر تبديل اللغة السيادي - تثبيت قسري لضمان الظهور */
            #langBtn { 
                position: fixed; top: 20px; left: 20px; z-index: 999999 !important; 
                border: 2px solid var(--glow); background: rgba(0,20,0,0.9); 
                color: var(--glow); padding: 12px 24px; cursor: pointer; 
                font-weight: bold; box-shadow: 0 0 20px var(--glow);
                border-radius: 5px; text-transform: uppercase;
            }
            #langBtn:hover { background: var(--glow); color: #000; }

            .viewport { display: grid; grid-template-columns: 300px 1fr 300px; height: 100vh; padding: 20px; gap: 20px; }
            .panel { border: 1px solid var(--glow); padding: 20px; background: rgba(0,30,0,0.3); backdrop-filter: blur(10px); }
            .center { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }
            
            /* الرادار الكوانتي - نبض تلقائي */
            .radar { 
                width: 300px; height: 300px; border: 2px solid var(--glow); 
                border-radius: 50%; position: relative; 
                box-shadow: 0 0 30px rgba(0,255,0,0.2);
            }
            .radar::after { 
                content: ''; position: absolute; top: 50%; left: 50%; 
                width: 150px; height: 2px; background: var(--glow); 
                transform-origin: left; animation: scan 3s linear infinite; 
            }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .btn-exec { 
                width: 100%; padding: 15px; background: transparent; 
                border: 1px solid var(--glow); color: var(--glow); 
                margin: 10px 0; cursor: pointer; text-align: right; 
                font-weight: bold; transition: 0.3s;
            }
            .btn-exec:hover { background: var(--glow); color: #000; }
            .destruct { border-color: var(--danger); color: var(--danger); }
            .destruct:hover { background: var(--danger); color: #fff; box-shadow: 0 0 20px var(--danger); }

            #live-feed { font-size: 0.85em; margin-top: 30px; color: #fff; text-align: center; height: 40px; }
        </style>
    </head>
    <body onload="initSovereignOps()">
        <button id="langBtn" onclick="toggleSovereignLang()">ENGLISH</button>
        
        <div class="viewport">
            <div class="panel">
                <h3 id="h-arsenal">[ الترسانة التنفيذية ]</h3>
                <button class="btn-exec" onclick="act('ATK')" id="b-atk">إطلاق الهجوم المضاد</button>
                <button class="btn-exec" onclick="act('SHD')" id="b-shd">تفعيل الدرع المداري</button>
                <button class="btn-exec destruct" onclick="purge()" id="b-dst">التدمير الذاتي</button>
            </div>

            <div class="center">
                <h1 id="h-title" style="letter-spacing: 10px;">الجنرال الشبحي</h1>
                <div class="radar"></div>
                <div id="live-feed">> جاري فحص استقرار النواة السيادية...</div>
            </div>

            <div class="panel">
                <h3 id="h-memory">[ الذاكرة السيادية ]</h3>
                <p id="h-val" style="font-size: 1.4em; color: #fff;">VALUATION: $50,000,000</p>
                <hr style="border-color: var(--glow)">
                <p id="h-status">التعقب: نشط</p>
                <p id="h-target">الأهداف: مرصودة</p>
            </div>
        </div>

        <script>
            let currentLang = 'ar';
            function toggleSovereignLang() {
                const html = document.getElementById('mainHtml');
                const btn = document.getElementById('langBtn');
                if(currentLang === 'ar') {
                    html.dir = 'ltr'; btn.innerText = 'العربية'; currentLang = 'en';
                    document.getElementById('h-arsenal').innerText = '[ EXECUTION ARSENAL ]';
                    document.getElementById('b-atk').innerText = 'Counter-Attack';
                    document.getElementById('b-shd').innerText = 'Orbital Shield';
                    document.getElementById('b-dst').innerText = 'SELF-DESTRUCT';
                    document.getElementById('h-title').innerText = 'STEALTH GENERAL';
                    document.getElementById('h-memory').innerText = '[ SOVEREIGN MEMORY ]';
                    document.getElementById('h-status').innerText = 'Tracking: Active';
                    document.getElementById('h-target').innerText = 'Targets: Locked';
                } else {
                    html.dir = 'rtl'; btn.innerText = 'ENGLISH'; currentLang = 'ar';
                    document.getElementById('h-arsenal').innerText = '[ الترسانة التنفيذية ]';
                    document.getElementById('b-atk').innerText = 'إطلاق الهجوم المضاد';
                    document.getElementById('b-shd').innerText = 'تفعيل الدرع المداري';
                    document.getElementById('b-dst').innerText = 'التدمير الذاتي';
                    document.getElementById('h-title').innerText = 'الجنرال الشبحي';
                    document.getElementById('h-memory').innerText = '[ الذاكرة السيادية ]';
                    document.getElementById('h-status').innerText = 'التعقب: نشط';
                    document.getElementById('h-target').innerText = 'الأهداف: مرصودة';
                }
            }

            function initSovereignOps() {
                // تفعيل تعقب الـ GPS
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition((pos) => {
                        fetch('/api/track', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({lat: pos.coords.latitude, lng: pos.coords.longitude})
                        });
                    });
                }
                // اليقظة التلقائية: الأوامر تعمل حتى بدون ضغط
                setInterval(() => {
                    const logs = ["> فحص الأنظمة...", "> تحديث الدرع المداري...", "> تعقب IP مشبوه...", "> النواة مستقرة"];
                    document.getElementById('live-feed').innerText = logs[Math.floor(Math.random()*logs.length)];
                }, 4000);
            }

            function act(type) {
                document.getElementById('live-feed').innerText = `> تفعيل: ${type} [تم بنجاح]`;
            }

            function purge() {
                if(confirm("تحذير: سيتم مسح المنظومة بالكامل. هل أنت متأكد؟")) {
                    document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>CORE PURGED - SECURE EXIT</h1>";
                }
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/api/track', methods=['POST'])
def track_api():
    log_sovereign({"type": "GPS_CAPTURE", "data": request.json})
    return jsonify({"status": "captured"})

if __name__ == "__main__":
    app.run()
