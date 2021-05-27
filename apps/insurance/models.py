from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model): #Títulos de projeto

    name_product = models.CharField(max_length=255, verbose_name='TIPOS DE PRODUTO')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_product


class Agency(models.Model): #Títulos de projeto

    name_agency = models.CharField(max_length=255, verbose_name='ANGÊNCIAS')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_agency

class Secure(models.Model): #Títulos de projeto

    name_secure = models.CharField(max_length=255, verbose_name='TIPOS DE SEGUROS')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_secure


class Cliente(models.Model): #Títulos de projeto

    name = models.CharField(max_length=255, verbose_name='NOME DO CLIENTE')
    cpf = models.CharField(max_length=11, blank=True, null=False, verbose_name='CPF')
    cnpj = models.CharField(max_length=14, blank=True, null=False, verbose_name='CNPJ')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUTO')
    agency =models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name='AGÊNCIA')
    conta = models.CharField(max_length=20, blank=True, null=False, verbose_name='NÚMERO DA CONTA')
    gerency = models.CharField(max_length=255, blank=True, null=False, verbose_name='NOME DO GERENTE')
    secure = models.ForeignKey(Secure, on_delete=models.CASCADE, verbose_name='SEGURO')
    policy = models.CharField(max_length=30, verbose_name='NÚMERO DA APOLICE')
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='VALOR PAGO') #default_currency='BRA'
    tel1 = models.CharField(max_length=10, blank=True, null=False, verbose_name='TELEFONE OPÇÃO 1')
    tel2 = models.CharField(max_length=10, blank=True, null=False, verbose_name='TELEFONE OPÇÃO 2')
    cel1 = models.CharField(max_length=11, blank=True, null=False, verbose_name='CELULAR OPÇÃO 1')
    cel2 = models.CharField(max_length=11, blank=True, null=False, verbose_name='CELULAR OPÇÃO 2')
    email= models.CharField(max_length=255, blank=True, null=False, verbose_name='E-MAIL')
    comments = models.TextField(blank=True, null=False, verbose_name='OBS')
    date_contract = models.DateField(blank=True, null=True, verbose_name='DATA SEGURO')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
