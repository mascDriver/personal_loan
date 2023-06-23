from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True)
    address = models.CharField(verbose_name='Endereço', max_length=100)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    client = models.ForeignKey(Client, verbose_name='Cliente', on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='Valor', max_digits=8, decimal_places=2)
    approved = models.BooleanField(verbose_name='Aprovado', default=False)
    analyzed = models.BooleanField(verbose_name='Analisado?', default=False)

    def __str__(self):
        return f"{self.client} - {self.value}"
