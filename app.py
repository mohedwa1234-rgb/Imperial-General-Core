from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!doctype html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ghost General v3.5 - Sovereign Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        imperial: '#1e293b'
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-gray-950 text-gray-100 min-h-screen font-sans antialiased">
    <div class="container mx-auto px-4 py-8 max-w-4xl">
        <header class="text-center mb-10">
            <h1 class="text-4xl font-bold text-blue-400 mb-2">Ghost General v{{ version }}</h1>
            <p class="text-xl text-gray-400">Sovereign Asset Simulator</p>
            <div class="mt-4 inline-block bg-gray-800 px-6 py-3 rounded-full shadow-lg">
                <span class="font-mono text-green-400">Valuation: ${{ "{:,}".format(price) }}</span>
            </div>
        </header>
        <main class="space-y-8">
            <section class="bg-gray-900 p-6 rounded-xl shadow-xl border border-gray-700">
                <h2 class="text-2xl font-semibold mb-4 text-blue-300">Execute</h2>
                <!-- أضف هنا المحتوى الإضافي إذا كان موجود، مثل أزرار أو فورم -->
            </section>
            <!-- أضف sections أخرى إذا لزم الأمر -->
        </main>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    version = "3.5"  # غيرها حسب الحاجة
    price = 1250000   # مثال: 1,250,000
    return render_template_string(html, version=version, price=price)

# للـ Vercel: لا تضيف app.run()، Vercel يتعامل مع الـ server