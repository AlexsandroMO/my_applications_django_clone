from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('name','cpf','cnpj','prod','agency','secure','conta','gerency','policy','amount_paid','tel1','tel2','cel1','cel2','email','comments','date_contract')



