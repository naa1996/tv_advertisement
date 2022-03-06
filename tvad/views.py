from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Customer, Status, Advertisement, Broadcast, Rating

def index(request):
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def create_customer(request):
    #создание клиента
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        number = request.POST['number']
        print(number)
        contact_person = request.POST['cont']
        print(contact_person)
        telephone = request.POST['tel']
        print(telephone)
        money = request.POST['money']
        print(money)

        Customer.objects.create(
            name=name,
            contract_number=number,
            contact_person=contact_person,
            telephone=telephone,
            money=money,
        )
        print('Клиент успешно добавлен')
        messages.error(request, 'Клиент успешно добавлен', extra_tags='saveCU')
        return redirect('customer')
    else:
        return redirect('customer')


def customer(request):
    customer_all = Customer.objects.all()
    return render(request, 'customer.html', {
        'title': 'Клиенты',
        'customer_all': customer_all
    })


def advertisement(request):
    return render(request, 'advertisement.html', {
        'title': 'Реклама',
    })


def broadcast(request):
    return render(request, 'broadcast.html', {
        'title': 'Передачи',
    })


def rating(request):
    return render(request, 'rating.html', {
        'title': 'Рейтинг',
    })