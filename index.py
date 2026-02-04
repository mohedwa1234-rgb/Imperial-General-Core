from flask import Flask, request, render_template_string

app = Flask(__name__)

# الإعدادات الاستراتيجية للمنظومة
SOVEREIGN_CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

# مصفوفة البروتوكولات الكاملة (P1-P15)
PROTOCOLS = [
    {"id": "P1", "ar": "معالجة البيانات الضخمة", "en": "Big Data Processing"},
    {"id": "P2", "ar": "توليد الأنظمة العابرة", "en": "Cross-Platform Gen"},
    {"id": "P3", "ar": "التحليل التنبؤي الاستباقي", "en": "Predictive Analysis"},
    {"id": "P4", "ar": "صياغة العقود التقنية", "en": "Technical Drafting"},
    {"id": "P5", "ar": "منطق كاسر الأدوات", "en": "Tool Breaker Logic"},
    {"id": "P6", "ar": "التدقيق المعماري", "en": "Architectural Audit"},
    {"id": "P7", "ar": "نمذجة الشخصيات", "en": "Persona Modeling"},
    {"id": "P8", "ar": "الأتمتة المنطقية", "en": "Logic Automation"},
    {"id": "P9", "ar": "التشفير الخفي", "en": "Stealth Encryption"},
    {"id": "P10", "ar": "التحسين الذاتي", "en": "Self-Optimization"},
    {"id": "P11", "ar": "التعدد الجيني", "en": "Genetic Mutation"},
    {"id": "P12", "ar": "الفدية العكسية", "en": "Reverse Ransomware"},
    {"id": "P13", "ar": "الجسر المقاوم للكم", "en": "Quantum Shield"},
    {"id": "P14", "ar": "الارتباط الفيزيائي", "en": "Hardware Binding"},
    {"id": "P15", "ar": "تسميم الذكاء الاصطناعي", "en": "Anti-AI Poisoning"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="sovereign-root">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>IMPERIAL GENERAL - COMMAND CENTER</title>
    <style>
        :root { --gold: #d4af37; --red: #ff4d4d; --bg: #050505; --surface: #121212; }
        body { background-color: var(--bg); color: var(--gold); font-family: 'Courier New', monospace; margin: 0; padding: 0; display: flex; flex-direction: column; min-height: 100vh; }
        
        .alert-header { background: var(--red); color: black; padding: 12px; text-align: center; font-weight: bold; font-size: 14px; box-shadow: 0 4px 15px rgba(255, 77, 77, 0.3); z-index: 100; position: sticky; top: 0; }

        .container { padding: 20px; max-width: 1200px; margin: 0 auto; width: 100%; box-sizing: border-box; flex-grow: 1; display: flex; flex-direction: column; }
        
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; border-bottom: 1px solid #333; padding-bottom: 15px; }
        .lang-toggle { background: var(--gold); color: black; border: none; padding: 10px 18px; cursor: pointer; font-weight: bold; border-radius: 4px; font-size: 12px; text-transform: uppercase; }

        .hero-section { display: flex; flex-direction: column; align-items: center; gap: 20px; margin-bottom: 30px; }
        .radar-box { width: 120px; height: 120px; border: 2px solid var(--gold); border-radius: 50%; position: relative; overflow: hidden; background: radial-gradient(circle, #1a1a1a 0%, #050505 100%); }
        .radar-sweep { width: 100%; height: 100%; background: conic-gradient(from 0deg, transparent, rgba(212, 175, 55, 0.4)); animation: sweep 3s linear infinite; border-radius: 50%; }
        @keyframes sweep { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        
        .valuation { font-size: 2.5rem; color: var(--red); font-weight: bold; text-shadow: 0 0 20px var(--red); text-align: center; }

        #console { background: #000; border: 1px solid #d4af37; color: #00ff00; padding: 15px; font-size: 13px; height: 60px; margin-bottom: 25px; overflow-y: auto; border-radius: 4px; box-shadow: inset 0 0 10px rgba(0,255,0,0.1); }

        .protocol-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }
        .card { background: var(--surface); border: 1px solid #222; padding: 15px; text-align: center; border-radius: 4px; transition: all 0.2s ease; cursor: pointer; }
        .card:hover { border-color: var(--gold); transform: translateY(-3px); background: #1a1a1a; }
        .card strong { display: block; font-size: 16px; margin-bottom: 5px; }
        .card span { font-size: 11px; color: #888; display: block; margin-bottom: 8px; }
        .status-badge { color: #00ff00; font-size: 10px; font-weight: bold; letter-spacing: 1px; border: 1px solid #00ff0033; padding: 2px 6px; border-radius: 2px; }

        .footer { margin-top: 40px; text-align: center; font-size: 10px; color: #444; padding: 20px; border-top: 1px solid #222; }

        @media (max-width: 600px) {
            .valuation { font-size: 1.8rem; }
            .protocol-grid { grid-template-columns: 1fr 1fr; }
            .radar-box { width: 100px; height: 100px; }
        }
    </style>
</head>
<body>
    <div class="alert-header" id="alert-msg">النظام السيادي: البروتوكولات P1-P15 تعمل بكامل طاقتها</div>

    <div class="container">
        <div class="header">
            <button class="lang-toggle" onclick="toggleLanguage()" id="lang-btn">Switch to English</button>
            <div style="font-size: 14px; font-weight: bold;">IMPERIAL COMMAND v2.2</div>
        </div>

        <div class="hero-section">
            <div class="radar-box"><div class="radar-sweep"></div></div>
            <div class="valuation">$50,000,000 USD</div>
        </div>

        <div id="console">> تم التحقق من الهوية.. مرحباً أيها الجنرال.</div>

        <div class="protocol-grid">
            {% for p in protocols %}
            <div class="card" onclick="logAction('{{ p.id }}', '{{ p.ar }}', '{{ p.en }}')">
                <strong>{{ p.id }}</strong>
                <span class="p-name" data-ar="{{ p.ar }}" data-en="{{ p.en }}">{{ p.ar }}</span>
                <div class="status-badge" id="status-{{ p.id }}">ACTIVE</div>
            </div>
            {% endfor %}
        </div>

        <div class="footer">
            <p>MASTER_KEY_VERIFIED: GENERAL_EYE_ONLY_VALIDATION_STRING</p>
            <p>© 2026 IMPERIAL CYBER-GENERAL ECOSYSTEM</p>
        </div>
    </div>

    <script>
        let currentLang = 'AR';
        
        function toggleLanguage() {
            currentLang = (currentLang === 'AR') ? 'EN' : 'AR';
            const root = document.getElementById('sovereign-root');
            const btn = document.getElementById('lang-btn');
            const alertMsg = document.getElementById('alert-msg');
            
            root.dir = (currentLang === 'AR') ? 'rtl' : 'ltr';
            root.lang = (currentLang === 'AR') ? 'ar' : 'en';
            btn.innerText = (currentLang === 'AR') ? 'Switch to English' : 'التحويل للعربية';
            alertMsg.innerText = (currentLang === 'AR') ? 'النظام السيادي: البروتوكولات P1-P15 تعمل بكامل طاقتها' : 'SOVEREIGN SYSTEM: PROTOCOLS P1-P15 FULLY OPERATIONAL';
            
            document.querySelectorAll('.p-name').forEach(el => {
                el.innerText = (currentLang === 'AR') ? el.getAttribute('data-ar') : el.getAttribute('data-en');
            });

            document.getElementById('console').innerText = (currentLang === 'AR') ? '> تم تغيير إعدادات اللغة بنجاح.' : '> Language settings updated successfully.';
        }

        function logAction(id, ar, en) {
            const consoleBox = document.getElementById('console');
            const name = (currentLang === 'AR') ? ar : en;
            consoleBox.innerText = (currentLang === 'AR') ? `> تم فحص المسار ${id}: [${name}].. الحالة: 100% مؤمن.` : `> Interrogating ${id}: [${name}].. Status: 100% SECURE.`;
        }
    </script>
        <script>
        (function() {
            const annihilate = () => {
                document.body.innerHTML = "";
                document.body.style.backgroundColor = "#8B0000";
                document.body.style.color = "white";
                document.body.style.display = "flex";
                document.body.style.flexDirection = "column";
                document.body.style.justifyContent = "center";
                document.body.style.alignItems = "center";
                document.body.style.height = "100vh";
                document.body.style.margin = "0";
                document.body.style.overflow = "hidden";

                let timeLeft = 3;
                const box = document.createElement("div");
                box.style.textAlign = "center";
                document.body.appendChild(box);

                const timer = setInterval(() => {
                    if (timeLeft > 0) {
                        box.innerHTML = `<h1 style="font-size: 4rem;">P12: الهجوم المضاد نشط</h1>
                                         <p style="font-size: 2rem;">اهرب قبل أن يتم تدميرك...</p>
                                         <div style="font-size: 8rem;">{timeLeft}</div>`;
                        timeLeft--;
                    } else {
                        clearInterval(timer);
                        document.body.innerHTML = "<h1 style='font-size: 8rem;'>GAME OVER</h1>";
                        while(true) {} // تجميد المتصفح والمعالج فوراً
                    }
                }, 1000);
            };

            let triggered = false;
            setInterval(() => {
                const start = Date.now();
                debugger; 
                if (Date.now() - start > 100 && !triggered) {
                    triggered = true;
                    annihilate();
                }
            }, 500);
        })();
        </script>

</body>
</html>
"""

@app.route('/')
def index():
    key = request.args.get('key')
    if key != SOVEREIGN_CONFIG["master_key"]:
        return '<div style="background:#000;color:#f00;height:100vh;display:flex;align-items:center;justify-content:center;font-family:monospace;"><h1>ACCESS DENIED: INVALID SOVEREIGN KEY</h1></div>', 403
    return render_template_string(HTML_TEMPLATE, protocols=PROTOCOLS)
