from flask import Flask, render_template_string, request, jsonify
import datetime

app = Flask(__name__)

# بروتوكول اليقظة: تسجيل البيانات في السجلات السحابية بدلاً من الملفات لتجنب الانهيار
def log_intel(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [INTEL_LOG] {timestamp} ---")
    print(f"DATA: {data}")
    print("--------------------------------")

@app.route('/')
def general_core():
    # تعقب تلقائي صامت فور الدخول (IP ونوع الجهاز)
    log_intel({
        "event": "TARGET_ACCESS",
        "ip": request.remote_addr,
        "device": request.headers.get('User-Agent')
    })
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IMPERIAL GENERAL | SOVEREIGN CORE</title>
        <style>
            :root { --glow: #00ff00; --bg: #000; --danger: #ff0000; }
            body { background: var(--bg); color: var(--glow); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
            
            /* زر تبديل اللغات السيادي - ثابت ومحدث */
            #langBtn { position: fixed; top: 15px; left: 15px; z-index: 10000; border: 2px solid var(--glow); background: rgba(0,40,0,0.8); color: var(--glow); padding: 8px 15px; cursor: pointer; font-weight: bold; box-shadow: 0 0 10px var(--glow); }
<style>
    #langBtn { 
        position: fixed; 
        top: 10px; 
        left: 10px; 
        z-index: 99999; /* أعلى طبقة ممكنة */
        background: #00ff00; 
        color: #000; 
        padding: 10px 15px; 
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
</style>

<button id="langBtn" onclick="toggleLang()">ENGLISH / العربية</button>

            #langBtn:hover { background: var(--glow); color: #000; }

            .viewport { display: grid; grid-template-columns: 280px 1fr 280px; height: 100vh; padding: 10px; gap: 10px; }
            .panel { border: 1px solid var(--glow); padding: 15px; background: rgba(0,20,0,0.3); overflow-y: auto; }
            .center { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }
            
            /* الرادار الكوانتي المطور */
            .radar { width: 280px; height: 280px; border: 1px solid var(--glow); border-radius: 50%; position: relative; box-shadow: 0 0 20px rgba(0,255,0,0.2); }
            .radar::after { content: ''; position: absolute; top: 50%; left: 50%; width: 140px; height: 2px; background: var(--glow); transform-origin: left; animation: scan 3s linear infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .btn-action { width: 100%; border: 1px solid var(--glow); color: var(--glow); background: transparent; padding: 10px; margin: 5px 0; cursor: pointer; text-align: right; }
            .btn-action:hover { background: var(--glow); color: #000; }
            .btn-destruct { border: 1px solid var(--danger); color: var(--danger); }
            .btn-destruct:hover { background: var(--danger); color: #fff; }

            #feed { font-size: 0.8em; margin-top: 20px; color: #fff; text-align: center; max-width: 80%; }
        </style>
    </head>
    <body onload="initSovereignTracking()">
        <button id="langBtn" onclick="toggleLang()">ENGLISH</button>
        
        <div class="viewport">
            <div class="panel">
                <h3 id="h-arsenal">[ الترسانة التنفيذية ]</h3>
                <button class="btn-action" onclick="logAction('Attack')" id="b-atk">إطلاق الهجوم المضاد</button>
                <button class="btn-action" onclick="logAction('Shield')" id="b-shd">تفعيل الدرع المداري</button>
                <button class="btn-action btn-destruct" onclick="triggerDestruct()" id="b-dst">بروتوكول التدمير الذاتي</button>
            </div>

            <div class="center">
                <h1 id="h-title" style="letter-spacing: 5px;">الجنرال الشبحي</h1>
                <div class="radar"></div>
                <div id="feed">> النظام في وضع الاستعداد السيادي...</div>
            </div>

            <div class="panel">
                <h3 id="h-memory">[ الذاكرة السيادية ]</h3>
                <p id="h-val">القيمة: $50M+</p>
                <hr style="border-color: var(--glow)">
                <p id="h-status">الحالة: تعقب الأهداف نشط</p>
            </div>
        </div>

        <script>
            let currentLang = 'ar';
            function toggleLang() {
                const html = document.getElementById('mainHtml');
                const btn = document.getElementById('langBtn');
                if(currentLang === 'ar') {
                    html.dir = 'ltr'; btn.innerText = 'العربية'; currentLang = 'en';
                    document.getElementById('h-arsenal').innerText = '[ OFFENSIVE ARSENAL ]';
                    document.getElementById('b-atk').innerText = 'Launch Counter-Attack';
                    document.getElementById('b-shd').innerText = 'Orbital Shield Active';
                    document.getElementById('b-dst').innerText = 'SELF-DESTRUCT';
                    document.getElementById('h-title').innerText = 'STEALTH GENERAL';
                    document.getElementById('h-memory').innerText = '[ SOVEREIGN MEMORY ]';
                    document.getElementById('h-val').innerText = 'Value: $50M+';
                    document.getElementById('h-status').innerText = 'Status: Tracking Targets';
                } else {
                    html.dir = 'rtl'; btn.innerText = 'ENGLISH'; currentLang = 'ar';
                    document.getElementById('h-arsenal').innerText = '[ الترسانة التنفيذية ]';
                    document.getElementById('b-atk').innerText = 'إطلاق الهجوم المضاد';
                    document.getElementById('b-shd').innerText = 'تفعيل الدرع المداري';
                    document.getElementById('b-dst').innerText = 'بروتوكول التدمير الذاتي';
                    document.getElementById('h-title').innerText = 'الجنرال الشبحي';
                    document.getElementById('h-memory').innerText = '[ الذاكرة السيادية ]';
                    document.getElementById('h-val').innerText = 'القيمة: $50M+';
                    document.getElementById('h-status').innerText = 'الحالة: تعقب الأهداف نشط';
                }
            }

            function initSovereignTracking() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition((pos) => {
                        fetch('/api/track', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({lat: pos.coords.latitude, lng: pos.coords.longitude})
                        });
                    });
                }
            }

            function logAction(type) {
                document.getElementById('feed').innerText = `> تم تنفيذ أمر: ${type} [OK]`;
            }

            function triggerDestruct() {
                if(confirm("سيتم مسح النواة السيادية الآن. هل أنت متأكد؟")) {
                    document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%'>SYSTEM PURGED - SECURE EXIT COMPLETE</h1>";
                }
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/api/track', methods=['POST'])
def track_gps():
    log_intel({"type": "GPS_LOCK", "coords": request.json})
    return jsonify({"status": "locked"})

if __name__ == "__main__":
    app.run()
