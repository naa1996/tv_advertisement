from django.db import models


class Customer(models.Model):
    """
    Заказчик
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    contract_number = models.CharField(max_length=100, verbose_name='Номер договора')
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
    duration = models.IntegerField(verbose_name='Продолжительность')
    broadcast_name = models.CharField(max_length=150, verbose_name='Прередача')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name='Заказчик')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус рекламы')

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
    raring = models.FloatField(blank=True, verbose_name='Стоимость')
    data = models.DateTimeField(blank=True)