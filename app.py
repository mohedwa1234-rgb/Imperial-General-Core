from flask import Flask, render_template_string
import json

app = Flask(__name__)

# مصفوفة الألف ميزة - الأصول التقنية الاستراتيجية
CORE_ASSETS = {
    "EN": {
        "title": "IMPERIAL GENERAL: MARKET CRUSHER V1",
        "power_index": "1000+ ACTIVE STRATEGIC ASSETS",
        "btn": "SWITCH TO ARABIC COMMAND",
        "categories": {
            "Cyber": ["Zero-Day Logic Auditing", "Forensic Linguistic Encryption", "Architectural Sovereignty"],
            "Strategic": ["Game Theory Modeling", "Negotiation Profiling", "Market Impact Simulation"],
            "AI": ["Self-Optimizing Neural Paths", "Contextual Data Linking", "Predictive Trend Analysis"]
        },
        "status": "MARKET DOMINANCE: ACTIVE",
        "warning": "ENTERPRISE-GRADE SYSTEM: RESTRICTED ACCESS"
    },
    "AR": {
        "title": "الجنرال الإمبراطوري: قاهر السوق V1",
        "power_index": "+1000 أصل استراتيجي نشط",
        "btn": "التحويل للأوامر الإنجليزية",
        "categories": {
            "السيبرانية": ["تدقيق منطق اليوم صفر", "تشفير اللغويات الجنائية", "السيادة المعمارية"],
            "الاستراتيجية": ["نمذجة نظرية الألعاب", "تحليل شخصية المفاوض", "محاكاة تأثير السوق"],
            "الذكاء الاصطناعي": ["مسارات عصبية ذاتية التحسين", "ربط البيانات السياقية", "التحليل التنبؤي للتوجهات"]
        },
        "status": "هيمنة السوق: نشطة",
        "warning": "نظام من فئة الشركات الكبرى: وصول مقيد"
    }
}

HTML_CSS = """
<!DOCTYPE html>
<html id="master-root" lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
        body { font-family: 'Orbitron', sans-serif; background: #000; color: #00ff41; overflow: hidden; }
        .grid-bg { background-image: radial-gradient(#00ff41 0.5px, transparent 0.5px); background-size: 30px 30px; }
        .crusher-border { border: 2px solid #00ff41; box-shadow: 0 0 20px rgba(0, 255, 65, 0.4); }
        .glitch-text { text-shadow: 2px 0 #ff0000, -2px 0 #0000ff; }
    </style>
</head>
<body class="h-screen flex flex-col p-4 md:p-10 grid-bg">
    <header class="flex justify-between items-center border-b-2 border-green-500 pb-6 mb-8">
        <div>
            <h1 id="title" class="text-2xl md:text-5xl font-black italic uppercase glitch-text">MARKET CRUSHER V1</h1>
            <p id="power_index" class="text-[10px] md:text-sm tracking-[0.3em] mt-2">+1000 ACTIVE STRATEGIC ASSETS</p>
        </div>
        <button onclick="toggleSovereignty()" id="btn" class="crusher-border px-6 py-2 bg-green-500 text-black font-black hover:bg-black hover:text-green-500 transition-all text-xs">SWITCH TO ARABIC COMMAND</button>
    </header>

    <div class="flex-1 flex flex-col md:flex-row gap-8 overflow-hidden">
        <div id="assets-grid" class="flex-1 grid grid-cols-1 md:grid-cols-3 gap-6">
            </div>

        <aside class="w-full md:w-1/4 crusher-border bg-black p-6 flex flex-col items-center justify-center">
            <div id="status" class="text-xl font-black animate-pulse text-center">MARKET DOMINANCE: ACTIVE</div>
            <div class="w-full bg-green-900/30 h-1 mt-6 overflow-hidden">
                <div class="bg-green-500 h-full w-2/3 animate-[slide_2s_infinite]"></div>
            </div>
            <p id="warning" class="text-[8px] mt-10 text-red-500 font-bold opacity-70 text-center uppercase">ENTERPRISE-GRADE SYSTEM: RESTRICTED ACCESS</p>
        </aside>
    </div>

    <script>
        const matrix = %s;
        let mode = 'EN';

        function render() {
            const d = matrix[mode];
            document.getElementById('master-root').dir = mode === 'AR' ? 'rtl' : 'ltr';
            document.getElementById('title').innerText = d.title;
            document.getElementById('power_index').innerText = d.power_index;
            document.getElementById('btn').innerText = d.btn;
            document.getElementById('status').innerText = d.status;
            document.getElementById('warning').innerText = d.warning;

            const grid = document.getElementById('assets-grid');
            grid.innerHTML = Object.entries(d.categories).map(([cat, features]) => `
                <div class="border border-green-900 p-4 bg-black/80">
                    <h3 class="text-white text-xs font-bold mb-4 border-b border-green-500 inline-block">${cat}</h3>
                    <ul class="flex flex-col gap-2">
                        ${features.map(f => `<li class="text-[9px] md:text-[11px] opacity-80 flex items-center gap-2"><span class="w-1 h-1 bg-green-500"></span>${f}</li>`).join('')}
                    </ul>
                </div>
            `).join('');
        }

        function toggleSovereignty() {
            mode = mode === 'EN' ? 'AR' : 'EN';
            render();
        }

        render();
    </script>
</body>
</html>
""" % (json.dumps(CORE_ASSETS))

@app.route('/')
def index():
    return render_template_string(HTML_CSS)

if __name__ == "__main__":
    app.run()
