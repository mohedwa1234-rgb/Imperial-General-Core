// كود التبديل السيادي داخل الواجهة
let currentLang = 'ar';
function toggleLang() {
    const html = document.getElementById('mainHtml');
    const btn = document.getElementById('uiLangBtn');
    
    if (currentLang === 'ar') {
        html.dir = 'ltr'; // تحويل الواجهة للغة الإنجليزية (اليسار)
        btn.innerText = 'العربية';
        document.getElementById('title').innerText = 'STEALTH GENERAL: ACTIVE';
        document.getElementById('btn-destruct').innerText = 'ACTIVATE SELF-DESTRUCT';
        currentLang = 'en';
    } else {
        html.dir = 'rtl'; // العودة للسيادة العربية (اليمين)
        btn.innerText = 'ENGLISH';
        document.getElementById('title').innerText = 'الجنرال الشبحي: نشط';
        document.getElementById('btn-destruct').innerText = 'تفعيل التدمير الذاتي';
        currentLang = 'ar';
    }
}
