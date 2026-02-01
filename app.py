from flask import Flask, render_template_string, request, jsonify
import datetime

app = Flask(__name__)

# سجلات الاستخبارات: تظهر في Vercel Logs فقط لضمان السرية والسيادة
def log_sovereign(data):
    print(f"--- [INTEL_LOG] {datetime.datetime.now()} ---")
    print(f"REPORT: {data}")

@app.route('/')
def imperial_core():
    # تعقب صامت وتلقائي فور الدخول (IP ونوع الجهاز)
    log_sovereign({
        "event": "INTRUSION_DETECTED",
        "ip": request.remote_addr,
        "agent": request.headers.get('User-Agent')
    })
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GENERAL CORE | SOVEREIGN SYSTEM</title>
        <style>
            :root { --glow: #00ff00; --bg: #000; --danger: #ff0000; }
            body { background: var(--bg); color: var(--glow); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
            
            /* زر تبديل اللغة السيادي - تثبيت في أعلى طبقة بصرياً */
            #langBtn { 
                position: fixed; top: 10px; left: 10px; z-index: 99999; 
                border: 2px solid var(--glow); background: rgba(0,255,0,0.2); 
                color: var(--glow); padding: 12px 20px; cursor: pointer; 
                font-weight: bold; backdrop-filter: blur(5px);
                box-shadow: 0 0 15px var(--glow);
            }
            #langBtn:hover { background: var(--glow); color: #000; }

            .viewport { display: grid; grid-template-columns: 300px 1fr 300px; height: 100vh; padding: 15px; gap: 15px; }
            .panel { border: 1px solid var(--glow); padding: 20px; background: rgba(0,20,0,0.4); }
            .center { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }
            
            /* الرادار الكوانتي بنظام الـ 3D */
            .radar { 
                width: 320px; height: 320px; border: 2px solid var(--glow); 
                border-radius: 50%; position: relative; 
                box-shadow: inset 0 0 50px rgba(0,255,0,0.1), 0 0 20px rgba(0,255,0,0.2);
            }
            .radar::after { 
                content: ''; position: absolute; top: 50%; left: 50%; 
                width: 160px; height: 2px; background: var(--glow); 
                transform-origin: left; animation: scan 2s linear infinite; 
            }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .btn-exec { 
                width: 100%; padding: 15px; background: transparent; 
                border: 1px solid var(--glow); color: var(--glow); 
                margin: 10px 0; cursor: pointer; text-align: right; 
                transition: 0.3s; font-weight: bold;
            }
            .btn-exec:hover { background: var(--glow); color: #000; box-shadow: 0 0 20px var(--glow); }
            .destruct { border-color: var(--danger); color: var(--danger); }
            .destruct:hover { background: var(--danger); color: #fff; }

            #feed { font-size: 0.9em; margin-top: 25px; color: #fff; text-align: center; height: 50px; }
        </style>
    </head>
    <body onload="activateSovereignTracking()">
        <button id="langBtn" onclick="toggleSovereignLanguage()">ENGLISH</button>
        
        <div class="viewport">
            <div class="panel">
                <h3 id="t-arsenal">[ الترسانة التنفيذية ]</h3>
                <button class="btn-exec" onclick="cmd('Attack')" id="b-atk">إطلاق الهجوم المضاد</button>
                <button class="btn-exec" onclick="cmd('Shield')" id="b-shd">تفعيل الدرع المداري</button>
                <button class="btn-exec destruct" onclick="triggerPurge()" id="b-dst">بروتوكول التدمير الذاتي</button>
            </div>

            <div class="center">
                <h1 id="t-title" style="letter-spacing: 8px; text-shadow: 0 0 10px var(--glow);">الجنرال الشبحي</h1>
                <div class="radar"></div>
                <div id="feed">> النظام في حالة يقظة قصوى...</div>
            </div>

            <div class="panel">
                <h3 id="t-memory">[ الذاكرة السيادية ]</h3>
                <p id="t-val" style="font-size: 1.5em; font-weight: bold;">$50,000,000+</p>
                <hr style="border-color: var(--glow)">
                <p id="t-status">الحالة: التعقب الجنائي نشط</p>
                <p id="t-intel">الأهداف المرصودة: 0</p>
            </div>
        </div>

        <script>
            let currentLang = 'ar';
            function toggleSovereignLanguage() {
                const html = document.getElementById('mainHtml');
                const btn = document.getElementById('langBtn');
                if(currentLang === 'ar') {
                    html.dir = 'ltr'; btn.innerText = 'العربية'; currentLang = 'en';
                    document.getElementById('t-arsenal').innerText = '[ OFFENSIVE ARSENAL ]';
                    document.getElementById('b-atk').innerText = 'Launch Counter-Attack';
                    document.getElementById('b-shd').innerText = 'Activate Orbital Shield';
                    document.getElementById('b-dst').innerText = 'SELF-DESTRUCT';
                    document.getElementById('t-title').innerText = 'STEALTH GENERAL';
                    document.getElementById('t-memory').innerText = '[ SOVEREIGN MEMORY ]';
                    document.getElementById('t-status').innerText = 'Status: Forensic Tracking Active';
                    document.getElementById('t-intel').innerText = 'Detected Targets: 0';
                } else {
                    html.dir = 'rtl'; btn.innerText = 'ENGLISH'; currentLang = 'ar';
                    document.getElementById('t-arsenal').innerText = '[ الترسانة التنفيذية ]';
                    document.getElementById('b-atk').innerText = 'إطلاق الهجوم المضاد';
                    document.getElementById('b-shd').innerText = 'تفعيل الدرع المداري';
                    document.getElementById('b-dst').innerText = 'بروتوكول التدمير الذاتي';
                    document.getElementById('t-title').innerText = 'الجنرال الشبحي';
                    document.getElementById('t-memory').innerText = '[ الذاكرة السيادية ]';
                    document.getElementById('t-status').innerText = 'الحالة: التعقب الجنائي نشط';
                    document.getElementById('t-intel').innerText = 'الأهداف المرصودة: 0';
                }
            }

            function activateSovereignTracking() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition((pos) => {
                        fetch('/api/intel', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({lat: pos.coords.latitude, lng: pos.coords.longitude})
                        });
                        document.getElementById('t-intel').innerText = (currentLang === 'ar' ? 'الأهداف المرصودة: 1' : 'Detected Targets: 1');
                    });
                }
                // تفعيل اليقظة التلقائية (النبض)
                setInterval(() => {
                    const feeds = ["> جاري فحص استقرار النواة...", "> تحديث التشفير اللغوي...", "> الدرع المداري: مستقر"];
                    document.getElementById('feed').innerText = feeds[Math.floor(Math.random()*feeds.length)];
                }, 5000);
            }

            function cmd(type) {
                document.getElementById('feed').innerText = `> تفعيل الأمر: ${type}... [تم التنفيذ]`;
            }

            function triggerPurge() {
                if(confirm("سيتم تدمير كافة الأصول الرقمية لمنع الاستحواذ القسري. هل تؤكد؟")) {
                    document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>CORE PURGED - SYSTEM ZERO ACTIVE</h1>";
                }
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/api/intel', methods=['POST'])
def intel_api():
    log_sovereign({"type": "GPS_LOCK", "coordinates": request.json})
    return jsonify({"status": "captured"})

if __name__ == "__main__":
    app.run()
