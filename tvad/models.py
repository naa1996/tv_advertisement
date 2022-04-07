from django.db import models


class Customer(models.Model):
    """
    Заказчик
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    contract_number = models.CharField(max_length=100, verbose_name='Номер договора')
    bank_details = models.CharField(max_length=200, verbose_name='Банковские реквизиты')
    contact_person = models.CharField(max_length=100, verbose_name='Контактное лицо')
    telephone = models.CharField(max_length=12, verbose_name='Номер телефона')
    money = models.IntegerField(verbose_name='Кошелек')

    def __str__(self):
        return self.name


class Status(models.Model):
    """
    Статус
    """
    status_name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.status_name


class Advertisement(models.Model):
    """
    Реклама
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Краткое описание')
    duration = models.FloatField(verbose_name='Продолжительность')
    day_week = models.IntegerField(verbose_name='День недели')
    number_repetitions = models.IntegerField(verbose_name='Количество повторов')
    cost = models.FloatField(blank=True, verbose_name='Стоимость')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name='Заказчик')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус рекламы')
    # broadcast = models.ManyToOneRel(Broadcast, on_delete=models.DO_NOTHING)
    # broadcast = models.ManyToManyField(Broadcast, verbose_name='Рекомендуемая передача')

    def __str__(self):
        return self.name


class Broadcast(models.Model):
    """
    Передача
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Краткое описание')
    duration = models.IntegerField(verbose_name='Продолжительность')
    cost_program = models.FloatField(blank=True, verbose_name='Стоимость')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING, verbose_name='Реклама')

    def __str__(self):
        return self.name


class Rating(models.Model):
    """
    Рейтинг программ
    """
    broadcast = models.ForeignKey(Broadcast, on_delete=models.DO_NOTHING, verbose_name='Передача')
    rating = models.FloatField(blank=True, verbose_name='Рейтинг')
    data = models.DateTimeField(blank=True)
    # advertisement = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING, verbose_name='Реклама')
    # advertisement2 = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING, verbose_name='Реклама')
    # advertisement3 = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING, verbose_name='Реклама')
