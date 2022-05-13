from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea, SelectDateWidget, DateInput, PasswordInput
from django import forms

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    
    class Meta:
        model = get_user_model()
        fields = ['organization_title',
                'first_name', 
                'last_name', 
                'fathers_name',
                'email', 
				'address',
				'position',
				'phone_number',
				'personal_phone_number',]
    
    organization_title = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Наименование организаций")
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Адрес")
    first_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Имя")
    last_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Фамилия")
    fathers_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Отчество")
    position = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px', 'rows': 1,'cols': 40}), label="Должность")
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','style':'max_width: 300px', 'maxlength': 12}), label="Номер телефона")
    personal_phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','style':'max_width: 300px', 'maxlength': 12}), label="Личный номер телефона")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'max_width: 300px'}), label="Почта")

    