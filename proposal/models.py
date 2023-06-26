from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    address = models.CharField(verbose_name='Endereço', max_length=100)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Cliente', on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name='Valor', max_digits=8, decimal_places=2)
    approved = models.BooleanField(verbose_name='Aprovado', default=False)
    analyzed = models.BooleanField(verbose_name='Analisado?', default=False)

    def __str__(self):
        return f"{self.customer} - {self.value}"


@receiver(post_save, sender=Proposal, dispatch_uid="analyze_proposal_task")
def analyze_proposal(sender, instance, **kwargs):
    from .tasks import analyse_proposal
    analyse_proposal.apply_async()
