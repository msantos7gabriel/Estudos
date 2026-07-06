# from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         labels = {'username': 'Login', 'password': 'Senha'}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput)

    # Se eu precisar pegar dois campos ou mais ao mesmo tempo
    # utilizo a função  da seguinte maneira
    """    def clean(self):
            cleaned_data = super().clean()
            nome = cleaned_data.get('login')   
            senha = cleaned_data.get('senha')   

            VALIDAÇÃO
    """

    def clean_login(self):
        nome = self.cleaned_data['login']

        if not (nome.isalnum()):
            raise ValidationError(
                'O nome de Usuário não pode ter caractere especial')
        return nome
