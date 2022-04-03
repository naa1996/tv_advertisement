from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Customer, Status, Advertisement, Broadcast, Rating
from django.shortcuts import get_object_or_404
import datetime
import getpass

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
        name_c = Customer.objects.filter(name=name)
        tel_c = Customer.objects.filter(telephone=telephone)
        if (name != '') & (number != '') & (contact_person != '') & (telephone != '') & (money != ''):
            if telephone.isnumeric():
                if len(telephone) == 11:
                    if not name_c:
                        if not tel_c:
                                if money.isnumeric():
                                    Customer.objects.create(
                                        name=name,
                                        contract_number=number,
                                        contact_person=contact_person,
                                        telephone=telephone,
                                        money=money,
                                    )
                                    print('Клиент успешно добавлен+')
                                    messages.error(request, 'Клиент успешно добавлен', extra_tags='saveCU')
                                    return redirect('customer')
                                else:
                                    print('Не удалось добавить информацию. Неверный формат записи суммы')
                                    messages.error(request, 'Не удалось добавить информацию. Неверный формат записи суммы',
                                                   extra_tags='saveCU')
                                    return redirect('customer')
                        else:
                            print('Клиент c таким номером телефона уже существует+')
                            messages.error(request, 'Клиент c таким номером телефона уже существует', extra_tags='saveCU')
                            return redirect('customer')
                    else:
                        print('Клиент c таким именем уже существует+')
                        messages.error(request, 'Клиент c таким именем уже существует', extra_tags='saveCU')
                        return redirect('customer')
                else:
                    print('Не удалось добавить информацию. Неверный формат номера+')
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат номера', extra_tags='saveCU')
                    return redirect('customer')
            else:
                print('Не удалось добавить информацию. Неверный формат записи телефона+')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат записи телефона',
                               extra_tags='saveCU')
                return redirect('customer')
        else:
            print(1)
            return redirect('customer')
    else:
        return redirect('customer')


def customer(request):
    customer_all = Customer.objects.all()
    return render(request, 'customer.html', {
        'title': 'Клиенты',
        'customer_all': customer_all
    })


def updateStatusAdv(request):
    if request.method == 'POST':
        id_adv = request.POST['id_adv']
        status = request.POST['status']
        print(id_adv, status)
        id_a = Advertisement.objects.get(id=id_adv).id
        print(id_a)
        id_s = Status.objects.get(id=status).id
        print(id_s)
        Advertisement.objects.filter(id=id_a).update(
            status = status
        )
        return redirect('advertisement')
    else:
        return redirect('advertisement')


def create_advertisement(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        desc = request.POST['desc']
        print(desc)
        dur = request.POST['dur']
        print(dur)
        day_week = request.POST['day_week']
        print(day_week)
        selected_customer = request.POST['selected_customer']
        print('id', selected_customer)
        status = request.POST['status']
        print('status', status)
        print('id', broadcast)
        customer0 = Customer.objects.get(id=selected_customer)
        status0 = Status.objects.get(id=status)
        name_a = Advertisement.objects.filter(name=name)
        desc_a = Advertisement.objects.filter(description=desc)
        dir90 = int(90)
        dir60= int(60)
        dir30= int(30)
        dir15= int(15)
        dir0 = int(0)
        if (name != '') & (desc != '') & (dur != '') & (day_week != '') & (selected_customer != ''):
            if dur.isnumeric():
                if day_week.isnumeric():
                    if str(day_week) in '123456789':
                        if not name_a:
                            if not desc_a:
                                Advertisement.objects.create(
                                    name=name,
                                    description=desc,
                                    duration=dur,
                                    day_week=day_week,
                                    customer=customer0,
                                    status=status0,
                                )
                                print('Реклама успешно добавлена+')
                                messages.error(request, 'Реклама успешно добавлена', extra_tags='saveAD')
                                return redirect('advertisement')
                            else:
                                print('Реклама c таким описанием уже существует+')
                                messages.error(request, 'Реклама c таким описанием уже существует', extra_tags='saveAD')
                                return redirect('advertisement')
                        else:
                            print('Реклама c таким именем уже существует+')
                            messages.error(request, 'Реклама c таким именем уже существует', extra_tags='saveAD')
                            return redirect('advertisement')
                    else:
                        print('Дни недели не по порядку+')
                        messages.error(request, 'Дни недели не по порядку', extra_tags='saveAD')
                        return redirect('advertisement')
                else:
                    print('Не удалось добавить информацию. Неверный формат записи дней недели+')
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат записи дней недели', extra_tags='saveAD')
                    return redirect('advertisement')
            else:
                print('Не удалось добавить информацию. Неверный формат записи продолжительности рекламы+')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат записи продолжительности рекламы', extra_tags='saveAD')
                return redirect('advertisement')
        else:
            return redirect('advertisement')
    else:
        return redirect('advertisement')


def advertisement(request):
    advertisement_all = Advertisement.objects.all()
    customer_all = Customer.objects.all()
    status = Advertisement.objects.all()
    # broadcast_all = Broadcast.objects.all()
    print(advertisement_all)
    return render(request, 'advertisement.html', {
        'title': 'Реклама',
        'advertisement_all': advertisement_all,
        'customer_all': customer_all,
        'status_all': status,
        # 'broadcast_all': broadcast_all,
    })


def create_broadcast(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        description = request.POST['desc']
        print(description)
        duration = request.POST['dur']
        print(duration)
        cost_program = request.POST['cost']
        print(cost_program)
        advertisement = Advertisement.objects.get(id=request.POST['advertisement'])
        print(advertisement)
        status_advertisment = Advertisement.objects.get(id=request.POST['advertisement']).status_id
        status_name = Status.objects.get(id=status_advertisment).status_name
        print(status_advertisment)
        print(status_name)
        name_broadcast = Broadcast.objects.filter(name=name)
        desc_broadcast = Broadcast.objects.filter(description=description)
        print(name_broadcast)
        if (name != '') & (description != '') & (duration != '') & (cost_program != ''):
            if not name_broadcast:
                if not desc_broadcast:
                    if status_advertisment == 1:
                        if duration.isnumeric():
                            if cost_program.isnumeric():
                                Broadcast.objects.create(
                                    name = name,
                                    description = description,
                                    duration = duration,
                                    cost_program = cost_program,
                                    advertisement = advertisement,
                                )
                                print('Передача успешно добавлена')
                                messages.error(request, 'Передача успешно добавлена', extra_tags='saveBR')
                                return redirect('broadcast')
                            else:
                                print('Не удалось добавить информацию. Неверный формат стоимости передачи')
                                messages.error(request, 'Не удалось добавить информацию. Неверный формат стоимости передачи', extra_tags='saveBR')
                                return redirect('broadcast')
                        else:
                            print('Не удалось добавить информацию. Неверный формат продолжительности передачи')
                            messages.error(request, 'Не удалось добавить информацию. Неверный формат продолжительности передачи', extra_tags='saveBR')
                            return redirect('broadcast')
                    else:
                        print('Реклама ещё не активирована')
                        messages.error(request, 'Реклама ещё не активирована', extra_tags='saveBR')
                        return redirect('broadcast')
                else:
                    print('Такое описание передачи уже существует')
                    messages.error(request, 'Такое описание передачи уже существует', extra_tags='saveBR')
                    return redirect('broadcast')
            else:
                print('Такая передача уже существует')
                messages.error(request, 'Такая передача уже существует', extra_tags='saveBR')
                return redirect('broadcast')
        else:
            return redirect('broadcast')
    else:
        return redirect('broadcast')


def broadcast(request):
    broadcast = Broadcast.objects.all()
    advertisement_all = Advertisement.objects.all()
    return render(request, 'broadcast.html', {
        'title': 'Передачи',
        'broadcast': broadcast,
        'advertisement_all': advertisement_all,
    })


def broadcast_view(request,  *args, **kwargs):
    broadcast = get_object_or_404(Broadcast, id=kwargs['id'])
    advertisement = Advertisement.objects.filter(broadcast=broadcast)

    return render(request, 'broadcast/index.html', {
        'title': 'Информация о передаче',
        'name': broadcast.name,
        'description': broadcast.description,
        'advertisment': advertisement,
        'cost_program': broadcast.cost_program,
        'duration': broadcast.duration,
    })


def create_rating(request):
    if request.method == 'POST':
        broadcast = request.POST['broadcast']
        print('broadcast', broadcast)
        rating = request.POST['rating']
        print('rating', rating)
        id_date = request.POST['dateR']
        print('id_date', id_date)
        broadcast_name = Broadcast.objects.get(id=broadcast).name
        print('broadcast_name', broadcast_name)
        rating_br_90 = request.POST['rating_br_90']
        rating_br_60 = request.POST['rating_br_60']
        rating_br_30 = request.POST['rating_br_30']
        rating_br_15 = request.POST['rating_br_15']
        cost_90 = request.POST['cost_90']
        cost_60 = request.POST['cost_60']
        cost_30 = request.POST['cost_30']
        cost_15 = request.POST['cost_15']
        id_broadcast = Broadcast.objects.get(id=broadcast)
        adv = Broadcast.objects.get(name=broadcast_name).advertisement
        print(adv)
        if (broadcast != '') & (rating != '') & (id_date != '') & (rating_br_90 != '') & (rating_br_60 != '') & (rating_br_30 != '') & (rating_br_15 != '') & (cost_90 != '') & (cost_60 != '') & (cost_30 != '') & (cost_15 != ''):
            if rating.isnumeric():
                if (rating_br_90.isnumeric()) & (rating_br_60.isnumeric()) & (rating_br_30.isnumeric()) & (rating_br_15.isnumeric()) & (cost_90.isnumeric()) & (cost_60.isnumeric()) & (cost_30.isnumeric()) & (cost_15.isnumeric()):
                    # Advertisement.objects.filter(broadcast__advertisement=broadcast):
                    Rating.objects.create(
                        broadcast=id_broadcast,
                        rating=rating,
                        data=formatDateForPython(id_date),
                    )
                    # вычисление стоимости рекламы
                    #нахождение времени рекламы
                    duration = Advertisement.objects.get(broadcast=broadcast).duration
                    #нахождение название рекламы
                    duration_name = Advertisement.objects.get(broadcast=broadcast).name
                    #нахождение заказчика рекламы
                    duration_customer = Advertisement.objects.get(broadcast=broadcast).customer.id
                    duration_customer_name = Advertisement.objects.get(broadcast=broadcast).customer.name
                    # нахождение времени передачи
                    time_broadcast = Broadcast.objects.get(id=broadcast).duration
                    print('название рекламы: ', duration_name)
                    print('время рекламы: ', duration)
                    print('название передачи: ', broadcast)
                    print('заказчик: ', duration_customer_name)
                    print('время передачи: ', time_broadcast)
                    if(duration >=90):
                        if(time_broadcast>=90):
                            print(1)
                            cost = float(rating) * float(cost_90) * float(rating_br_90)
                            print(00, cost)
                            #внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'4000'+'*'+'7' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif(time_broadcast>=60):
                            print(2)
                            cost = float(rating) * float(cost_90) * float(rating_br_60)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'4000'+'*'+'5' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif(time_broadcast>=30):
                            print(3)
                            cost = float(rating) * float(cost_90) * float(rating_br_30)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'4000'+'*'+'2' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 15):
                            print(4)
                            cost = float(rating) * float(cost_90) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '4000' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast < 15):
                            print(5)
                            cost = float(rating) * float(cost_90/2) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '4000' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                    elif(duration>=60):
                        if (time_broadcast >= 90):
                            print(6)
                            cost = float(rating) * float(cost_60) * float(rating_br_90)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'2000'+'*'+'7' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 60):
                            print(7)
                            cost = float(rating) * float(cost_60) * float(rating_br_60)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'2000'+'*'+'5' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 30):
                            print(8)
                            cost = float(rating) * float(cost_60) * float(rating_br_30)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'2000'+'*'+'2' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 15):
                            print(9)
                            cost = float(rating) * float(cost_60) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '2000' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast < 15):
                            print(10)
                            cost = float(rating) * float(cost_60/2) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '2000' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                    elif (duration >= 30):
                        if (time_broadcast >= 90):
                            print(11)
                            cost = float(rating) * float(cost_30) * float(rating_br_90)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/'+getpass.getuser()+'/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'1000'+'*'+'7' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 60):
                            print(12)
                            cost = float(rating) * float(cost_30) * float(rating_br_60)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'1000'+'*'+'5' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 30):
                            print(13)
                            cost = float(rating) * float(cost_30) * float(rating_br_30)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'1000'+'*'+'2' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 15):
                            print(14)
                            cost = float(rating) * float(cost_30) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '1000' + '*' + '1' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast < 15):
                            print(15)
                            cost = float(rating) * float(cost_30/2) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '1000' + '*' + '1' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                    elif (duration >= 15):
                        # время передачи
                        if (time_broadcast >= 90):
                            print(16)
                            cost = float(rating) * float(cost_15) * float(rating_br_90)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'500'+'*'+'7' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 60):
                            print(17)
                            cost = float(rating) * float(cost_15) * float(rating_br_60)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'500'+'*'+'5' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 30):
                            cost = float(rating) * float(cost_15) * float(rating_br_30)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write('Счёт-квитанция на оплату услуг телекомпании от '+id_date+'\n'+'\n'+'Название передачи: ' + broadcast_name +'\n' +
                                    'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(duration) + '\n' + 'Заказчик: ' +
                                    duration_customer_name + '\n' + 'Время передачи (мин): ' + str(time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                    '\n' + 'Расчёт: ' + str(float(rating))+'*'+'500'+'*'+'2' + '\n' + 'Стоимость (руб): ' +
                                    str(cost)+'\n''\n'+ 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast >= 15):
                            cost = float(rating) * float(cost_15) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '500' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                        elif (time_broadcast < 15):
                            cost = float(rating) * float(cost_15/2) * float(rating_br_15)
                            print(00, cost)
                            # внесение данных о заработанных средствах
                            costs = Customer.objects.get(id=int(duration_customer))
                            costs.money -= cost
                            costs.save()
                            f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                            f.write(
                                'Счёт-квитанция на оплату услуг телекомпании от ' + id_date + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                                'Название рекламы: ' + duration_name + '\n' + 'Время рекламы (сек): ' + str(
                                    duration) + '\n' + 'Заказчик: ' +
                                duration_customer_name + '\n' + 'Время передачи (мин): ' + str(
                                    time_broadcast) + '\n' + 'Рейтинг: ' + str(rating) +
                                '\n' + 'Расчёт: ' + str(
                                    float(rating)) + '*' + '500' + '*' + '2' + '\n' + 'Стоимость (руб): ' +
                                str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                            f.close()
                    print('Данные о рейтинге успешно добавлены')
                    messages.error(request, 'Данные о рейтинге успешно добавлены', extra_tags='saveR')
                    return redirect('rating')
                else:
                    print('Не удалось добавить информацию. Неверный формат расчетных данных')
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат расчетных данных', extra_tags='saveR')
                    return redirect('rating')
            else:
                print('Не удалось добавить информацию. Неверный формат рейтинга передачи')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат продолжительности передачи', extra_tags='saveR')
                return redirect('rating')
        else:
            return redirect('rating')
    else:
        return redirect('rating')

def rating(request):
    rating = Rating.objects.all()
    broadcast = Broadcast.objects.all()

    return render(request, 'rating.html', {
        'title': 'Рейтинг',
        'rating': rating,
        'broadcast': broadcast,
    })


def formatDateForPython(date_in):
    date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
    date_processing = [int(v) for v in date_processing]
    date_out = datetime.datetime(*date_processing)
    return str(date_out)