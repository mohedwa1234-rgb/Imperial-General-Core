from flask import Flask, request, render_template_string

app = Flask(__name__)

# الإعدادات السيادية
CONFIG = {
    "master_key": "GENERAL_EYE_ONLY_VALIDATION_STRING",
    "valuation": "50,000,000",
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl" id="main-html">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMPERIAL GENERAL - COMMAND CENTER</title>
    <style>
        :root { --gold: #d4af37; --red: #ff4d4d; --bg: #050505; }
        body { background-color: var(--bg); color: var(--gold); font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; overflow-x: hidden; }
        
        /* شريط التحذير العلوي */
        .status-header { background: var(--red); color: black; padding: 10px; text-align: center; font-weight: bold; font-size: 0.9em; box-shadow: 0 0 15px var(--red); width: 100%; position: sticky; top: 0; z-index: 1000; }

        .dashboard { display: flex; flex-direction: column; min-height: 100vh; padding: 15px; box-sizing: border-box; }
        
        .top-nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px; }
        .lang-btn { background: var(--gold); color: black; border: none; padding: 8px 20px; cursor: pointer; font-weight: bold; border-radius: 4px; font-size: 0.8em; }

        .radar-section { display: flex; flex-direction: column; align-items: center; gap: 15px; margin-bottom: 20px; }
        .radar { width: 100px; height: 100px; border: 2px solid var(--gold); border-radius: 50%; position: relative; overflow: hidden; }
        .sweep { width: 100%; height: 100%; background: conic-gradient(from 0deg, transparent, rgba(212, 175, 55, 0.4)); animation: rotate 3s linear infinite; border-radius: 50%; }
        @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

        .valuation { font-size: 2.2em; color: var(--red); text-shadow: 0 0 15px var(--red); font-weight: bold; text-align: center; }

        /* منطقة التفاعل - الكونسول */
        #console-output { background: #111; border: 1px solid #333; padding: 12px; min-height: 60px; margin: 15px 0; font-family: 'Courier New'; color: #00ff00; font-size: 0.85em; border-right: 4px solid var(--gold); word-wrap: break-word; }

        /* شبكة البروتوكولات - متجاوبة للجوال واللابتوب */
        .protocol-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; width: 100%; }
        .protocol-card { background: #1a1a1a; border: 1px solid #333; padding: 12px; text-align: center; cursor: pointer; transition: 0.2s; position: relative; }
        .protocol-card:active { transform: scale(0.95); background: #222; }
        .protocol-card span { display: block; font-size: 0.75em; margin-top: 5px; color: #888; }
        .active-tag { color: #00ff00 !important; font-weight: bold; font-size: 0.7em !important; }

        .footer { margin-top: auto; text-align: center; font-size: 0.7em; color: #444; padding: 20px 0; border-top: 1px solid #222; }

        @media (min-width: 768px) {
            .valuation { font-size: 3.5em; }
            .radar-section { flex-direction: row; justify-content: center; gap: 50px; }
            .status-header { font-size: 1.1em; }
        }
    </style>
</head>
<body>
    <div class="status-header" id="alert-text">كامل البروتوكولات السيادية من 1 إلى 15 نشطة وتعمل تحت إشراف "الجنرال"</div>

    <div class="dashboard">
        <div class="top-nav">
            <button class="lang-btn" onclick="toggleLang()" id="lang-btn">Switch to English</button>
            <div style="letter-spacing: 2px; font-size: 0.9em;">IMPERIAL GENERAL CORE</div>
        </div>

        <div class="radar-section">
            <div class="radar"><div class="sweep"></div></div>
            <div class="valuation" id="val-text">$50,000,000 USD</div>
        </div>

        <div id="console-output">> نظام الجنرال مستعد... البروتوكولات الـ 15 مؤمنة بالكامل.</div>

        <div class="protocol-grid" id="grid">
            </div>

        <div class="footer">
            <span id="footer-text">نظام الإمبراطورية v2.2 | تم التحقق من الهوية السيادية</span><br>
            MASTER_KEY: GENERAL_EYE_ONLY_VALIDATION_STRING
        </div>
    </div>

    <script>
        const protocols = [
            {id: "P1", ar: "البيانات الضخمة", en: "Big Data"}, {id: "P2", ar: "توليد المنصات", en: "Platform Gen"},
            {id: "P3", ar: "التحليل التنبؤي", en: "Predictive"}, {id: "P4", ar: "العقود التقنية", en: "Contracts"},
            {id: "P5", ar: "كاسر الأدوات", en: "Tool Breaker"}, {id: "P6", ar: "التدقيق المعماري", en: "Audit"},
            {id: "P7", ar: "نمذجة الشخصيات", en: "Persona"}, {id: "P8", ar: "الأتمتة", en: "Automation"},
            {id: "P9", ar: "التشفير الخفي", en: "Encryption"}, {id: "P10", ar: "التحسين الذاتي", en: "Self-Opt"},
            {id: "P11", ar: "التعدد الجيني", en: "Genetic"}, {id: "P12", ar: "الفدية العكسية", en: "Reverse Payload"},
            {id: "P13", ar: "الجسر الكمي", en: "Quantum Bridge"}, {id: "P14", ar: "الارتباط المادي", en: "Hardware Lock"},
            {id: "P15", ar: "تسميم الذكاء", en: "AI Poisoning"}
        ];

        let currentLang = 'AR';

        function renderGrid() {
            const grid = document.getElementById('grid');
            grid.innerHTML = '';
            protocols.forEach(p => {
                const card = document.createElement('div');
                card.className = 'protocol-card';
                card.innerHTML = `<strong>${p.id}</strong><span>${currentLang === 'AR' ? p.ar : p.en}</span>
                                  <span class="active-tag">${currentLang === 'AR' ? 'نشط' : 'ACTIVE'}</span>`;
                card.onclick = () => interact(p.id, currentLang === 'AR' ? p.ar : p.en);
                grid.appendChild(card);
            });
        }

        function interact(id, name) {
            const out = document.getElementById('console-output');
            out.innerText = currentLang === 'AR' ? `> تم فحص [${id} - ${name}]: الحالة 100% نشط.` : `> Interrogating [${id} - ${name}]: Status 100% ACTIVE.`;
            out.style.color = '#fff';
            setTimeout(() => { out.style.color = '#00ff00'; }, 150);
        }

        function toggleLang() {
            currentLang = currentLang === 'AR' ? 'EN' : 'AR';
            const html = document.getElementById('main-html');
            html.dir = currentLang === 'AR' ? 'rtl' : 'ltr';
            
            document.getElementById('lang-btn').innerText = currentLang === 'AR' ? 'Switch to English' : 'التحويل للعربية';
            document.getElementById('alert-text').innerText = currentLang === 'AR' ? 'كامل البروتوكولات السيادية من 1 إلى 15 نشطة وتعمل تحت إشراف "الجنرال"' : 'SOVEREIGN PROTOCOLS P1-P15: FULLY ACTIVE AND OPERATIONAL';
            document.getElementById('footer-text').innerText = currentLang === 'AR' ? 'نظام الإمبراطورية v2.2 | تم التحقق من الهوية السيادية' : 'IMPERIAL SYSTEM v2.2 | SOVEREIGN IDENTITY VERIFIED';
            
            renderGrid();
        }

        renderGrid();
    </script>
</body>
</html>
