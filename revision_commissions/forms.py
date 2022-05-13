from django import forms
from django.db.models.fields import BigIntegerField, IntegerField
from django.forms import ModelForm, Textarea, SelectDateWidget, DateInput, PasswordInput
from django.forms.widgets import TextInput
from .models import Organization_GU, Organization_KVAZI


inputField_attrs = {
				'class':'form-control',
				'style':'max_width: 300px',
				}


class OrganizationGuForm(forms.ModelForm):
	class Meta:
		model = Organization_GU
		fields = ['name',
				'annualFunding',
				'finPrePeriod',
				'finCurPeriod',
				'finEndYear',
				'cashExpense',
				'dateLastCheck',
				'dateReport',
				'finViolations',
				'volRecoverFin',
				'volReceivableCurrent',
				'volReceivablePrevious',
				'payableCurrent',
				'payablePrevious',
				'illegalActions',
				'disciplineSanctions',
				'materialEthics',
				'employeeEthics',
				'administrativeMeasures',
				'disciplineMeasures',
				'firedViolation',]

		widgets = {
			'name': Textarea(attrs={'cols': 40, 'rows': 1, 'class':'form-control','style':'max_width: 300px'}),
			'annualFunding': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finPrePeriod': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finCurPeriod': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finEndYear': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'cashExpense': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'preLastAudit': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'dateLastCheck': DateInput(format = '%d/%m/%Y', attrs={'type': 'date'}),
			#'period_since_the_last_governmental_audit': DateInput(attrs={'type': 'date'}),
			'dateReport': DateInput(format = '%Y-%m-%d', attrs={'type': 'date'}),
			'finViolations': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volRecoverFin': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volReceivableCurrent': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volReceivablePrevious': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'payableCurrent': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'payablePrevious': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
		}
		

class OrganizationKvaziForm(forms.ModelForm):
	class Meta:
		model = Organization_KVAZI
		fields = ['name',
				'annualFunding',
				'finEndYear',
				'cashExpense',
				'dateLastCheck',
				'dateReport',
				'finViolations',
				'volRecoverFin',
				'volReceivableCurrent',
				'volReceivablePrevious',
				'payableCurrent',
				'payablePrevious',
				'illegalActions',
				'disciplineSanctions',
				'employeeEthics',
				'administrativeMeasures',
				'disciplineMeasures',
				'firedViolation',
				'volAuthorizedCapitalCurrent',
				'volAuthorizedCapitalPrevious',
				'volIncomeCurrent',
				'volIncomePrevious',
				'volDividentsCurrent',
				'volAdministrativeSpendings',
				]

		widgets = {
			'name': Textarea(attrs={'cols': 40, 'rows': 1, 'class':'form-control','style':'max_width: 300px'}),
			'annualFunding': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finPrePeriod': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finCurPeriod': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'finEndYear': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'cashExpense': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'preLastAudit': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'dateLastCheck': DateInput(format = '%d/%m/%Y', attrs={'type': 'date'}),
			#'period_since_the_last_governmental_audit': DateInput(attrs={'type': 'date'}),
			'dateReport': DateInput(format = '%Y-%m-%d', attrs={'type': 'date'}),
			'finViolations': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volRecoverFin': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volReceivableCurrent': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'volReceivablePrevious': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'payableCurrent': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
			'payablePrevious': TextInput(attrs={'class':'form-control','style':'max_width: 300px'}),
		}
		


# this is not used
class RegistrationForm(forms.ModelForm):
	'''
	class Meta:
		model = CustomUser
		fields = ['organization_title',
				'address',
				'fathers_name',
				'position',
				'phone_number',
				'personal_phone_number','first_name', 'last_name', 'email', 'password']
		widgets = {
			'password': PasswordInput()
		}
	'''
	organization_title = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Наименование организаций")
	address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Адрес")
	first_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Имя")
	last_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Фамилия")
	fathers_name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Отчество")
	organization_title = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'max_width: 300px'}), label="Должность")
	phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','style':'max_width: 300px'}), label="Номер телефона")
	personal_phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','style':'max_width: 300px'}), label="Личный номер телефона")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'max_width: 300px'}), label="Почта")
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'max_width: 300px'}), label="Пароль")





class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'max_width: 300px','placeholder': 'Email'}), label="Почта")
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'max_width: 300px','placeholder': 'Пароль'}), label="Пароль")


class PasswordResetForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'max_width: 300px','placeholder': 'Email'}))