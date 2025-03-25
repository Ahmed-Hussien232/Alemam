from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Login, PrintOrder, Payments, Come_in

# دالة فحص تسجيل الدخول
def is_authenticated(request):
    return request.session.get('authenticated', False)

# الصفحة الرئيسية
def Al_emam(request):
    return render(request, 'pages/Al emam.html')

# تسجيل الدخول
def Page1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # حفظ بيانات الدخول بدون كلمة المرور (تحسين أمني)
        data = Login(username=username)
        data.save()

        if username == "admin" and password == "admin" and password2 == password:
            request.session.clear()  # مسح الجلسة السابقة
            request.session['authenticated'] = True
            return redirect("page2")

    return render(request, 'pages/page1.html')

# الصفحة الثانية بعد تسجيل الدخول
def Page2(request):
    if not is_authenticated(request):
        return redirect("page1")
    return render(request, 'pages/page2.html')

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from .models import PrintOrder

def Page3(request):
    if not request.session.get('authenticated'):
        return redirect("page1")

    if request.method == "POST":
        printing_type = request.POST.get("printing_type")
        paper_size = request.POST.get("paper_size")
        paper_number = int(request.POST.get("paper_number", 0))
        copy_number = int(request.POST.get("copy_number", 0))
        paper_price = float(request.POST.get("paper_price", 0))
        other = float(request.POST.get("other", 0))
        pay = request.POST.get("pay")

        total_price = paper_number * copy_number * paper_price

        order = PrintOrder(
            printing_type=printing_type,
            paper_size=paper_size,
            paper_number=paper_number,
            copy_number=copy_number,
            paper_price=paper_price,
            other=other,
            pay=pay,
            total_price=total_price,
            created_at=now()
        )
        order.save()

        return render(request, 'pages/page3.html', {'success': True})

    return render(request, 'pages/page3.html')

# صفحة عرض الطلبات
def Page4(request):
    if not is_authenticated(request):
        return redirect("page1")

    all_orders = PrintOrder.objects.all().order_by('-created_at')
    all_cash_out = Payments.objects.all().order_by('-created_at2')
    all_cash_in = Come_in.objects.all().order_by('-created_at3')

    context = {
        'cash_orders': all_orders.filter(pay="cash"),
        'vod_cash_orders': all_orders.filter(pay="vod-cash"),
        'Payments': all_cash_out,
        'Come_in': all_cash_in
    }

    return render(request, 'pages/page4.html', context)

# صفحة إخراج النقد
def Page5(request):
    if not request.session.get('authenticated'):
        return redirect("page1")

    if request.method == "POST":
        cash_out = request.POST.get('cash_out')
        notes = request.POST.get('notes')
        money_out = Payments(cash_out=cash_out, notes=notes, created_at2=now())
        money_out.save()

        return render(request, 'pages/page5.html', {'success': True})

    return render(request, 'pages/page5.html')

# صفحة إدخال النقد
def Page6(request):
    if not request.session.get('authenticated'):
        return redirect("page1")

    if request.method == "POST":
        cash_in = request.POST.get('cash_in')
        notes = request.POST.get('notes')
        money_in = Come_in(cash_in=cash_in, notes=notes, created_at3=now())
        money_in.save()

        return render(request, 'pages/page6.html', {'success': True})

    return render(request, 'pages/page6.html')