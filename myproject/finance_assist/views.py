from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import ActionForm, FilterForm
from .models import Action


def index(request):
    records = Action.objects.all()
    context = {'records': records}
    return render(request, 'finance_assist/index.html', context)



def action(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)

        if form.is_valid():
            action_name = form.cleaned_data['action_name']
            category_name = form.cleaned_data['category_name']
            action_date = form.cleaned_data['action_date']
            action_count = form.cleaned_data['action_count']
            record = Action(action_name=action_name, category_name=category_name, action_date=action_date, action_count=action_count)
            record.save()
            return HttpResponseRedirect(reverse(detail, args=[record.id]))
        else:
            return HttpResponseRedirect(reverse(action))
    else:
        form = ActionForm()

    return render(request, 'finance_assist/action.html', {'form': form})


def detail(request, action_id):
    record = Action.objects.get(id=action_id)
    return render(request, 'finance_assist/detail.html', {'record': record})


def report(request):
    profit = float(0)
    expence = float(0)
    currency = 'UAH'
    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start = form.data['start']
            finish = form.data['finish']
            records = Action.objects.filter(action_date__range=(start, finish))
            for rec in records:
                if rec.action_name_id == 1:
                    profit += rec.action_count
                else:
                    expence -= rec.action_count
    else:
        form = FilterForm()
        records = Action.objects.all()
        for rec in records:
            if rec.action_name_id == 1:
                profit += rec.action_count
            else:
                expence -= rec.action_count
    
    context = {'records': records, 'form': form, 'profit': profit, 'expence': expence, 'currency': currency}
    return render(request, 'finance_assist/report.html', context)

    