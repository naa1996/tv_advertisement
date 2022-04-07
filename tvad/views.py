from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
from django.contrib import messages
from .models import Customer, Status, Advertisement, Broadcast, Rating
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
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
        bank_details = request.POST['bank_details']
        print(bank_details)
        contact_person = request.POST['cont']
        print(contact_person)
        telephone = request.POST['tel']
        print(telephone)
        money = request.POST['money']
        print(money)
        name_c = Customer.objects.filter(name=name)
        tel_c = Customer.objects.filter(telephone=telephone)
        if (name != '') & (number != '') & (bank_details != '') & (contact_person != '') & (telephone != '') & (money != ''):
            if telephone.isnumeric():
                if len(telephone) == 11:
                    if not name_c:
                        if not tel_c:
                            if not bank_details.isalpha():
                                if money.isnumeric():
                                    if(int(money)!=0)&(int(money)>0):
                                        Customer.objects.create(
                                            name=name,
                                            contract_number=number,
                                            contact_person=contact_person,
                                            telephone=telephone,
                                            money=money,
                                        )
                                        print('Клиент успешно добавлен+')
                                        messages.error(request, 'Клиент успешно добавлен', extra_tags='saveCU')
                                        return redirect('calculation')
                                    else:
                                        print('Не удалось добавить информацию. Неверный формат записи суммы. Сумма должна быть больше нуля')
                                        messages.error(request,
                                                       'Не удалось добавить информацию. Неверный формат записи суммы',
                                                       extra_tags='saveCU')
                                        return redirect('calculation')
                                else:
                                    print('Не удалось добавить информацию. Неверный формат записи суммы')
                                    messages.error(request, 'Не удалось добавить информацию. Неверный формат записи суммы',
                                                   extra_tags='saveCU')
                                    return redirect('calculation')
                            else:
                                print('Не удалось добавить информацию. Неверный формат записи реквизитов')
                                messages.error(request, 'Не удалось добавить информацию. Неверный формат записи реквизитов',
                                               extra_tags='saveCU')
                                return redirect('calculation')
                        else:
                            print('Клиент c таким номером телефона уже существует+')
                            messages.error(request, 'Клиент c таким номером телефона уже существует', extra_tags='saveCU')
                            return redirect('calculation')
                    else:
                        print('Клиент c таким именем уже существует+')
                        messages.error(request, 'Клиент c таким именем уже существует', extra_tags='saveCU')
                        return redirect('calculation')
                else:
                    print('Не удалось добавить информацию. Неверный формат номера+')
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат номера', extra_tags='saveCU')
                    return redirect('calculation')
            else:
                print('Не удалось добавить информацию. Неверный формат записи телефона+')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат записи телефона',
                               extra_tags='saveCU')
                return redirect('calculation')
        else:
            print(1)
            return redirect('calculation')
    else:
        return redirect('calculation')


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
        number_repetitions = request.POST['number_repetitions_r']
        print(number_repetitions)
        cost_r = request.POST['cost_r']
        print(cost_r)
        customer0 = Customer.objects.get(id=selected_customer)
        status0 = Status.objects.get(id=status)
        name_a = Advertisement.objects.filter(name=name)
        desc_a = Advertisement.objects.filter(description=desc)
        if (name != '') & (desc != '') & (dur != '') & (day_week != '') & (selected_customer != '')& (number_repetitions != '') & (cost_r != ''):
            if dur.isnumeric():
                if day_week.isnumeric():
                    if str(day_week) in '123456789':
                        if number_repetitions.isnumeric():
                            if (int(number_repetitions) != 0) & (int(number_repetitions) > 0):
                                if cost_r.isnumeric():
                                    if (int(cost_r) !=0) & (int(cost_r)>0):
                                        if not name_a:
                                            if not desc_a:
                                                Advertisement.objects.create(
                                                    name=name,
                                                    description=desc,
                                                    duration=dur,
                                                    day_week=day_week,
                                                    number_repetitions=number_repetitions,
                                                    cost=cost_r,
                                                    customer=customer0,
                                                    status=status0,

                                                )
                                                print('Реклама успешно добавлена+')
                                                messages.error(request, 'Реклама успешно добавлена', extra_tags='saveCU')
                                                return redirect('calculation')
                                            else:
                                                print('Реклама c таким описанием уже существует+')
                                                messages.error(request, 'Реклама c таким описанием уже существует', extra_tags='saveCU')
                                                return redirect('calculation')
                                        else:
                                            print('Реклама c таким названием уже существует')
                                            messages.error(request,
                                                           'Реклама c таким названием уже существует',
                                                           extra_tags='saveCU')
                                            return redirect('calculation')
                                    else:
                                        print('Не удалось добавить информацию. Неверный формат стоимости')
                                        messages.error(request, 'Не удалось добавить информацию. Неверный формат стоимости',
                                                       extra_tags='saveCU')
                                        return redirect('calculation')
                                else:
                                    print('Не удалось добавить информацию. Неверный формат стоимости')
                                    messages.error(request, 'Не удалось добавить информацию. Неверный формат стоимости',
                                                   extra_tags='saveCU')
                                    return redirect('calculation')
                            else:
                                print('Не удалось добавить информацию. Неверный формат количества повторов')
                                messages.error(request, 'Не удалось добавить информацию. Неверный формат количества повторов',
                                               extra_tags='saveCU')
                                return redirect('calculation')
                        else:
                            print('Не удалось добавить информацию. Неверный формат количества повторов')
                            messages.error(request, 'Не удалось добавить информацию. Неверный формат количества повторов', extra_tags='saveCU')
                            return redirect('calculation')
                    else:
                        print('Дни недели не по порядку+')
                        messages.error(request, 'Дни недели не по порядку', extra_tags='saveCU')
                        return redirect('calculation')
                else:
                    print('Не удалось добавить информацию. Неверный формат записи дней недели+')
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат записи дней недели', extra_tags='saveCU')
                    return redirect('calculation')
            else:
                print('Не удалось добавить информацию. Неверный формат записи продолжительности рекламы+')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат записи продолжительности рекламы', extra_tags='saveCU')
                return redirect('calculation')
        else:
            return redirect('calculation')
    else:
        return redirect('calculation')


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
        id_broadcast = Broadcast.objects.get(id=broadcast)
        adv = Broadcast.objects.get(name=broadcast_name).advertisement
        print(adv)
        if (broadcast != '') & (rating != '') & (id_date != ''):
            if rating.isnumeric():

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

                    number = Advertisement.objects.get(name=duration_name).number_repetitions
                    cost_1 = Advertisement.objects.get(name=duration_name).cost
                    print(number)
                    print(cost_1)
                    # exit()
                    print(1)
                    cost = float(rating) * float(cost_1) * float(number)
                    print(00, cost)
                    #внесение данных о заработанных средствах
                    costs = Customer.objects.get(id=int(duration_customer))
                    costs.money -= cost
                    costs.save()
                    f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_.doc', 'w')
                    f.write(
                        'Расчетная Счёт-квитанция на оплату услуг телекомпании' + '\n' + '\n' + 'Название передачи: ' + broadcast_name + '\n' +
                        'Название рекламы: ' '\n' + 'Время рекламы (сек): ' + str(
                            duration) + '\n' + 'Заказчик: ' + '\n' + 'Время передачи (мин): ' + str(
                            time_broadcast) + '\n' + 'Рейтинг (последней передачи): ' + str(rating) +
                        '\n' + 'Стоимость за 1 передачу: ' + str(cost_1) +
                        '\n' + 'Расчёт: ' + str(
                            float(rating)) + '*' + str(cost_1) + '*' + str(
                            number) + '\n' + 'Стоимость (руб): ' +
                        str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                    f.close()
                    print('Данные о рейтинге успешно добавлены')
                    messages.error(request, 'Данные о рейтинге успешно добавлены', extra_tags='saveR')
                    return redirect('rating')
            else:
                print('Не удалось добавить информацию. Неверный формат рейтинга передачи')
                messages.error(request, 'Не удалось добавить информацию. Неверный формат рейтинга передачи', extra_tags='saveR')
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


def calculate_cost(request):
    if request.method == 'POST':
        duration = request.POST['duration']
        print('Время рекламы', duration)
        selected_broadcast = request.POST['selected_broadcast']
        print('Передача', selected_broadcast)
        number_repetitions = request.POST['number_repetitions']
        print('количество повторов', number_repetitions)
        cost_1 = request.POST['cost']
        print('стоимость', cost_1)
        # print(selected_broadcast.charAt(selected_broadcast[0].length()-1))
        # exit()
        if (duration != '') & (selected_broadcast != '') & (number_repetitions != '') & (cost_1 != ''):
            if (selected_broadcast[-1]) == "d":
                print(len(selected_broadcast))
                Str = selected_broadcast
                l = len(Str)
                selected_broadcast = Str[:l-1]
                print(selected_broadcast)
                name = Broadcast.objects.get(id=selected_broadcast).name
                print(name)
                time_broadcast = Broadcast.objects.get(name=name).duration
                print('время передачи', time_broadcast)
                print(111)
                if duration.isnumeric():
                    if (int(duration) != 0) & (int(duration) > 0):
                        if number_repetitions.isnumeric():
                            if (int(number_repetitions) != 0) & (int(number_repetitions) > 0):
                                if cost_1.isnumeric():
                                    print(111)
                                    if (int(cost_1) != 0) & (int(cost_1) > 0):
                                        col = Rating.objects.filter(broadcast=selected_broadcast).count()
                                        print('количество записей:', col)
                                        rating_id = Rating.objects.filter(broadcast=selected_broadcast).all()
                                        print('записи с такой передачей', rating_id)
                                        rating_0 = Rating.objects.filter(broadcast=selected_broadcast).last()
                                        print('рейтинг первый', rating_0)
                                        # rating_00 = Rating.objects.filter(broadcast=selected_broadcast).aggregate(Avg('rating'))
                                        # print('рейтинг средний', rating_00)
                                        rating_0.id
                                        rating_ind = Rating.objects.get(id = rating_0.id).rating
                                        print('показатель рейтинга', rating_ind)
                                        cost = float(rating_ind) * float(cost_1) * float(number_repetitions)
                                        print(00, cost)
                                        # внесение данных о заработанных средствах
                                        # costs = Customer.objects.get(id=int(duration_customer))
                                        # costs.money -= cost
                                        # costs.save()
                                        f = open('c:/users/' + getpass.getuser() + '/Desktop/rating_cost.doc', 'w')
                                        f.write(
                                            'Расчетная Счёт-квитанция на оплату услуг телекомпании' + '\n' + '\n' + 'Название передачи: ' + name + '\n' + 'Время рекламы (сек): ' + str(
                                                duration) + '\n' + 'Время передачи (мин): ' + str(
                                                time_broadcast) + '\n' + 'Рейтинг (последней передачи): ' + str(rating_ind) +
                                            '\n' + 'Стоимость за 1 передачу: ' + str(cost_1) +
                                            '\n' + 'Расчёт: ' + str(
                                                float(rating_ind)) + '*' + str(cost_1) + '*' + str(number_repetitions) + '\n' + 'Стоимость (руб): ' +
                                            str(cost) + '\n''\n' + 'Специалист по рейтингу          Ульянов Н.А.')
                                        f.close()
                                        #название программы
                                        request.session['name_broadcast'] = name
                                        #время рекламы
                                        request.session['time_adv'] = duration
                                        #время передачи
                                        request.session['time_br'] = str(time_broadcast)
                                        #количество повторов
                                        request.session['number_repetitions'] = number_repetitions
                                        # рейтинг последней передачи
                                        request.session['rating'] = str(rating_ind)
                                        # стоимость одной передачи
                                        request.session['cost'] = cost_1
                                        #итоговая стоимость рекламы за 1 передачу
                                        request.session['cost_end'] = cost
                                        return redirect('calculation')
                                        print('Расчёт добавлен')
                                        messages.error(request,
                                                   'Расчёт добавлен',
                                                   extra_tags='saveCU_с')
                                        return redirect('calculation')
                                    else:
                                        print('Не удалось добавить информацию. Стоимость не является положительной')
                                        messages.error(request,
                                            'Не удалось добавить информацию. Стоимость не является положительной',
                                                extra_tags='saveCU_с')
                                        return redirect('calculation')
                                else:
                                    print('Не удалось добавить информацию. Неверный формат стоимости')
                                    messages.error(request, 'Не удалось добавить информацию. Неверный формат стоимости',
                                                   extra_tags='saveCU_с')
                                    return redirect('calculation')
                            else:
                                print('Не удалось добавить информацию. Количество повторов не является положительным')
                                messages.error(request,
                                               'Не удалось добавить информацию. Количество повторов не является положительным',
                                               extra_tags='saveCU_с')
                                return redirect('calculation')
                        else:
                            print('Не удалось добавить информацию. Неверный формат количества повторов')
                            messages.error(request, 'Не удалось добавить информацию. Неверный формат количества повторов',
                                           extra_tags='saveCU_с')
                            return redirect('calculation')
                    else:
                        print('Не удалось добавить информацию. Время рекламы не является положительным')
                        messages.error(request,
                                       'Не удалось добавить информацию. Время рекламы не является положительным',
                                       extra_tags='saveCU_с')
                        return redirect('calculation')
                else:
                    messages.error(request, 'Не удалось добавить информацию. Неверный формат времени рекламы',
                                   extra_tags='saveCU_с')
                    return redirect('calculation')
            else:
                messages.error(request, 'Не удалось добавить информацию. Выбрана не 2 копия передачи',
                               extra_tags='saveCU_с')
                return redirect('calculation')
        else:
            return redirect('calculation')
    else:
        return redirect('calculation')


def clear_session(request):
    request.session.clear()
    return redirect(calculation)


def calculation(request):
    customer_all = Customer.objects.all()
    broadcast_all = Broadcast.objects.all()
    name_broadcast = request.session.get('name_broadcast')
    time_adv = request.session.get('time_adv')
    time_br = request.session.get('time_br')
    number_repetitions = request.session.get('number_repetitions')
    rating = request.session.get('rating')
    cost = request.session.get('cost')
    cost_end = request.session.get('cost_end')
    if(name_broadcast != '') & (time_adv != '') & (time_br != '') & (number_repetitions != '') & (rating != '') & (cost != '') & (cost_end != ''):
        return render(request, 'calculation.html', {
            'title': 'Расчёт',
            'customer_all': customer_all,
            'broadcast_all': broadcast_all,

            'name_broadcast': name_broadcast,
            'time_adv': time_adv,
            'time_br': time_br,
            'number_repetitions': number_repetitions,
            'rating': rating,
            'cost': cost,
            'cost_end': cost_end,
        })
    else:
        return render(request, 'calculation.html', {
            'title': 'Расчёт',
            'customer_all': customer_all,
            'broadcast_all': broadcast_all,
        })


def formatDateForPython(date_in):
    date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
    date_processing = [int(v) for v in date_processing]
    date_out = datetime.datetime(*date_processing)
    return str(date_out)

