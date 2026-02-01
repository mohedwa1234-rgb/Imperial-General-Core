from flask import Flask, render_template_string
import random

app = Flask(__name__)

# قاعدة بيانات الوحش السيبراني (مستقاة من مصفوفة الألف ميزة)
CYBER_BEAST_METRICS = {
    "Satellite_Link": "IMPERIAL-SAT-01 (ACTIVE)",
    "Scanning_Radius": "100 MILES",
    "Threat_Level": "LOW",
    "Shield_Capacity": "100%",
    "Active_Protocols": ["Ghost Mode", "Zero-Day Analysis", "Orbital Shield"]
}

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>IMPERIAL CYBER-BEAST | الوحش السيبراني</title>
        <style>
            :root { --main: #00ff00; --danger: #ff0000; --bg: #000; }
            body { background-color: var(--bg); color: var(--main); font-family: 'Courier New', Courier, monospace; margin: 0; overflow: hidden; }
            
            /* خلفية مصفوفة البيانات */
            #matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.2; }

            /* الواجهة المركزية */
            .beast-core { position: relative; width: 100vw; height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; }
            
            /* الرادار المداري */
            .radar { width: 300px; height: 300px; border: 2px solid var(--main); border-radius: 50%; position: relative; box-shadow: 0 0 50px rgba(0,255,0,0.2); }
            .radar::after { content: ''; position: absolute; top: 50%; left: 50%; width: 150px; height: 2px; background: var(--main); transform-origin: left; animation: scan 4s linear infinite; }
            
            /* لوحة القيادة السيادية */
            .dashboard { position: absolute; top: 20px; left: 20px; border: 1px solid var(--main); padding: 15px; background: rgba(0,15,0,0.9); width: 300px; }
            .features-grid { position: absolute; bottom: 20px; right: 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
            
            .btn { background: none; border: 1px solid var(--main); color: var(--main); padding: 10px; cursor: crosshair; transition: 0.3s; text-align: right; font-size: 0.8em; }
            .btn:hover { background: var(--main); color: #000; box-shadow: 0 0 20px var(--main); }

            .alert-monitor { position: absolute; bottom: 20px; left: 20px; width: 350px; border-left: 5px solid var(--main); padding-left: 10px; background: rgba(0,5,0,0.8); }

            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            .glitch { animation: glitch-text 2s infinite; font-weight: bold; font-size: 1.5em; }
            @keyframes glitch-text { 0% { transform: skew(0deg); } 20% { transform: skew(3deg); } 40% { transform: skew(-3deg); } 100% { transform: skew(0deg); } }
            .shield-up { box-shadow: 0 0 100px var(--main) !important; animation: pulse 0.5s infinite; }
            @keyframes pulse { 50% { opacity: 0.5; } }
        </style>
    </head>
    <body>
        <canvas id="matrix-bg"></canvas>

        <div class="beast-core">
            <div class="glitch">SYSTEM: CYBER-BEAST v1.0 [ACTIVE]</div>
            <div class="radar" id="radar"></div>

            <div class="dashboard">
                <h3>[ حالة القمر الصناعي ]</h3>
                <p>الرابط الفضائي: {{ data['Satellite_Link'] }}</p>
                <p>نطاق الرصد: {{ data['Scanning_Radius'] }}</p>
                <p>طاقة الدرع: <span id="shield-pct">{{ data['Shield_Capacity'] }}</span></p>
                <hr>
                <p>بروتوكولات نشطة: <br> - {{ data['Active_Protocols'] | join('<br> - ') }}</p>
            </div>

            <div class="features-grid">
                <button class="btn" onclick="triggerAction('Zero-Day')">تحليل ثغرات اليوم الصفر</button>
                <button class="btn" onclick="triggerAction('Forensic')">التدقيق الجنائي اللغوي</button>
                <button class="btn" onclick="triggerAction('Negotiation')">هندسة نفسية المفاوض</button>
                <button class="btn" onclick="triggerAction('GameTheory')">محاكاة نظرية الألعاب</button>
            </div>

            <div class="alert-monitor" id="monitor">
                > الوحش في وضع السكون.. المسح المداري مستمر.
            </div>
        </div>

        <script>
            // محرك الخلفية
            const canvas = document.getElementById('matrix-bg');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            const chars = "01"; const fontSize = 14; const columns = canvas.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);
            function drawMatrix() {
                ctx.fillStyle = "rgba(0,0,0,0.05)"; ctx.fillRect(0,0,canvas.width,canvas.height);
                ctx.fillStyle = "#0f0"; ctx.font = fontSize + "px monospace";
                drops.forEach((y, i) => {
                    const text = chars[Math.floor(Math.random()*chars.length)];
                    ctx.fillText(text, i*fontSize, y*fontSize);
                    if (y*fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                });
            }
            setInterval(drawMatrix, 50);

            // محرك كشف الهجوم والدرع
            function triggerAction(type) {
                const monitor = document.getElementById('monitor');
                const radar = document.getElementById('radar');
                monitor.style.color = "#0f0";
                monitor.innerText = `> جاري تنفيذ بروتوكول: ${type}... تم الحقن سيادياً.`;
                
                // محاكاة رصد هجوم عند الضغط
                if(Math.random() > 0.5) {
                    setTimeout(() => {
                        monitor.style.color = "#f00";
                        monitor.innerText = `⚠️ تم رصد محاولة اختراق في محيط 100 ميل! نوع الهجوم: استخباراتي سيبري.`;
                        radar.classList.add('shield-up');
                        setTimeout(() => {
                            monitor.style.color = "#0f0";
                            monitor.innerText = `🛡️ تم تفعيل الدرع الوقائي الفضائي.. تم سحق المهاجم.`;
                            radar.classList.remove('shield-up');
                        }, 3000);
                    }, 1000);
                }
            }
        </script>
    </body>
    </html>
    ''', data=CYBER_BEAST_METRICS)

if __name__ == "__main__":
    app.run()
