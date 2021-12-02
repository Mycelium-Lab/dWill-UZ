from django.shortcuts import render
from Meta.web import get_balance
from .models import Wallet

def index(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'index.html')

def api(request):
    if request.method == 'POST':
        fr = request.POST.get('from_')
        to1 = request.POST.get('to_')
        date = request.POST.get('date')
