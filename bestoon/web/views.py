from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from web.models import Expense, Income, Token
from django.contrib.auth.models import User 
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import random
import string
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
@csrf_exempt
#@login_required
# Create your views here.
def submit_expense(request):
    if not request.GET.get('token') or not request.GET.get('amount'):
        return render(request, "expense.html")
    this_token = request.GET.get('token')
    this_user = User.objects.filter(token__token = this_token).get()
    #if not this_user:
     #   return render(request, "expense_error.html")

    if 'date' not in request.GET:
        now = timezone.now()
    Expense.objects.create(user = this_user, amount = request.GET.get('amount'), text = request.GET.get('text'), date = now)
    return render(request, "expnese_succes.html", {
    "amount": request.GET.get("amount"),
    "text": request.GET.get("text"),
    "date": now,
    })
def submit_income(request):
    if not request.GET.get('token') or not request.GET.get('amount'):
        return render(request, "income.html")
    this_token = request.GET.get('token')
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.GET:
        now = timezone.now()
    Income.objects.create(user = this_user, date=now, text = request.GET.get('text'), amount = request.GET.get('amount'))
    return render(request, 'income_succes.html', {
        "amount": request.GET.get('amount'),
        "text": request.GET.get("text"),
        "date": now
    })
def register(request):

    this_user = request.GET.get("user")
    password = request.GET.get("password")

    if not this_user or not password:
        return render(request, "register.html")

    # Check if user already exists
    if User.objects.filter(username=this_user).exists():
        return render(request, "register_failed.html")

    # Create user with hashed password
    new_user = User.objects.create_user(username=this_user, password=password)
    this_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
    Token.objects.create(text = str(new_user), user = new_user, token = this_token)
    return render(request, "register_succes.html", {
        'username':this_user,
        "token":this_token
    })

    
def generalstat(request):
    if not request.GET.get('token'):
        return render(request, 'login.html')
    this_token = request.GET.get('token')
    this_user = User.objects.filter(token__token = this_token).get()
    income_count = Income.objects.filter(user = this_user).count()
    total_income = Income.objects.filter(user = this_user).aggregate(total=Sum('amount'))['total'] or 0
    expense_count = Expense.objects.filter(user = this_user).count()
    total_expense = Expense.objects.filter(user = this_user).aggregate(total=Sum('amount'))['total'] or 0
    sood = total_income - total_expense
    return render(request, "generalstat.html", {
        "income_count":income_count,
        "total_income":total_income,
        'expense_count':expense_count,
        'total_expense':total_expense,
        "sood":sood

    })









def main(request):
    print("IM here")
    return render(request, "index.html")