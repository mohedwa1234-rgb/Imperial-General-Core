from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl" id="mainHtml">
    <head>
        <meta charset="UTF-8">
        <title>IMPERIAL CYBER-BEAST | الوحش السيبراني</title>
        <style>
            :root { --main: #00ff00; --bg: #000; }
            body { background-color: var(--bg); color: var(--main); font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
            
            /* زر تبديل اللغة السيادي */
            .lang-toggle { position: fixed; top: 20px; left: 20px; z-index: 1000; border: 1px solid var(--main); background: rgba(0,20,0,0.8); color: var(--main); padding: 5px 15px; cursor: pointer; font-weight: bold; transition: 0.3s; }
            .lang-toggle:hover { background: var(--main); color: #000; box-shadow: 0 0 15px var(--main); }

            .beast-core { width: 100vw; height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
            .radar { width: 250px; height: 250px; border: 2px solid var(--main); border-radius: 50%; position: relative; margin: 20px; }
            .radar::after { content: ''; position: absolute; top: 50%; left: 50%; width: 125px; height: 2px; background: var(--main); transform-origin: left; animation: scan 4s linear infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            
            .dashboard { border: 1px solid var(--main); padding: 15px; background: rgba(0,10,0,0.9); width: 300px; font-size: 0.8em; }
            .glitch { font-size: 1.5em; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <button class="lang-toggle" onclick="toggleLanguage()" id="langBtn">English</button>

        <div class="beast-core">
            <div class="glitch" id="title">نظام: الوحش السيبراني v1.0 [نشط]</div>
            <div class="radar"></div>
            <div class="dashboard" id="dash">
                <h3 id="satTitle">[ حالة القمر الصناعي ]</h3>
                <p id="satLink">الرابط الفضائي: IMPERIAL-SAT-01</p>
                <p id="scanRange">نطاق الرصد: 100 ميل</p>
                <p id="shieldStatus">الدرع الوقائي: جاهز</p>
            </div>
        </div>

        <script>
            let currentLang = 'ar';
            function toggleLanguage() {
                const html = document.getElementById('mainHtml');
                const btn = document.getElementById('langBtn');
                const title = document.getElementById('title');
                const satTitle = document.getElementById('satTitle');
                const satLink = document.getElementById('satLink');
                const scanRange = document.getElementById('scanRange');
                const shieldStatus = document.getElementById('shieldStatus');

                if (currentLang === 'ar') {
                    // التحويل للإنجليزية
                    html.dir = 'ltr';
                    html.lang = 'en';
                    btn.innerText = 'العربية';
                    title.innerText = 'SYSTEM: CYBER-BEAST v1.0 [ACTIVE]';
                    satTitle.innerText = '[ SATELLITE STATUS ]';
                    satLink.innerText = 'Satellite Link: IMPERIAL-SAT-01';
                    scanRange.innerText = 'Scanning Radius: 100 Miles';
                    shieldStatus.innerText = 'Shield Status: READY';
                    currentLang = 'en';
                } else {
                    // العودة للعربية
                    html.dir = 'rtl';
                    html.lang = 'ar';
                    btn.innerText = 'English';
                    title.innerText = 'نظام: الوحش السيبراني v1.0 [نشط]';
                    satTitle.innerText = '[ حالة القمر الصناعي ]';
                    satLink.innerText = 'الرابط الفضائي: IMPERIAL-SAT-01';
                    scanRange.innerText = 'نطاق الرصد: 100 ميل';
                    shieldStatus.innerText = 'الدرع الوقائي: جاهز';
                    currentLang = 'ar';
                }
            }
        </script>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()
