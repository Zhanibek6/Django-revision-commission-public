from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Organization_GU, Organization_KVAZI
from .forms import OrganizationGuForm, OrganizationKvaziForm, LoginForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from accounts.forms import UserAdminCreationForm
# Create your views here.

# For files
from django.http.response import HttpResponse
#from .export import export_to_excel, generate_organization_data
#from .export2 import generate_organization_data_2
from .export_new import generate_organization_data, export_to_excel, parse_data
import os
#import mimetypes

# Сброс пароля
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

# For combining queries
from itertools import chain


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
	"""Домашняя страница приложения revision_commissions"""
	return render(request, 'revision_commissions/index.html')


def organizations(request):
	"""Выводит список всех организаций"""
	
	# Если пользователь состоит в группе коммисии
	user = request.user
	if user.groups.filter(name="Commission").exists():
		organizations_gu = Organization_GU.objects.all()
		organizations_kvazi = Organization_KVAZI.objects.all()
	else:
		organizations_gu = Organization_GU.objects.filter(user_id=user.id)
		organizations_kvazi = Organization_KVAZI.objects.filter(user_id=user.id)
	
	organizations = chain(organizations_gu, organizations_kvazi)
	context = {'organizations': organizations}
	return render(request, 'revision_commissions/organizations.html', context)


@login_required
def organization_gu(request, organization_id):
	"""Выводит данные выбранной организации."""
	organization = get_object_or_404(Organization_GU, id=organization_id)
	user = request.user
	if organization.user == request.user or user.groups.filter(name="Commission").exists():
		pass
	else:
		raise Http404

	# Атрибуты
	context = {'organization': organization}
	return render(request, 'revision_commissions/organization_gu.html', context)


@login_required
def organization_kvazi(request, organization_id):
	"""Выводит данные выбранной организации."""
	organization = get_object_or_404(Organization_KVAZI, id=organization_id)
	user = request.user
	if organization.user == request.user or user.groups.filter(name="Commission").exists():
		pass
	else:
		raise Http404
	
	# Атрибуты
	context = {'organization': organization}
	return render(request, 'revision_commissions/organization_kvazi.html', context)


@login_required
def new_organization_choice(request):
	return render(request, 'revision_commissions/new_organization_choice.html')


@login_required
def new_organization_gu(request):
	"""Определяет добавление новой организации."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = OrganizationGuForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = OrganizationGuForm(request.POST)
		if form.is_valid():  # Если форма допустима.
			org = form.save(commit=False)

			# for score and risk
			parsed_data = parse_data(form.cleaned_data, "ГУ")
			org.score = parsed_data[0]
			org.risk = parsed_data[1]

			org.user = request.user
			org.save()
			#cd = form.cleaned_data
			return HttpResponseRedirect(reverse('revision_commissions:organizations'))
	
	context = {'form': form, 'type': 'gu'}
	return render(request, 'revision_commissions/new_organization.html', context)


@login_required
def new_organization_kvazi(request):
	"""Определяет добавление новой организации."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = OrganizationKvaziForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = OrganizationKvaziForm(request.POST)
		if form.is_valid():  # Если форма допустима.
			org = form.save(commit=False)

			parsed_data = parse_data(form.cleaned_data, "КВАЗИ")
			org.score = parsed_data[0]
			org.risk = parsed_data[1]
			
			org.user = request.user
			org.save()
			#cd = form.cleaned_data
			return HttpResponseRedirect(reverse('revision_commissions:organizations'))
	
	context = {'form': form, 'type': 'kvazi'}
	return render(request, 'revision_commissions/new_organization.html', context)


@login_required
def edit_organization(request, organization_id, type):
	"""Редактирует данные организации."""
	if type == "ГУ":
		organization = get_object_or_404(Organization_GU, id=organization_id)
		if organization.user != request.user:
			raise Http404
		
		if request.method != 'POST':
			# Форма заполняется данными текущей организации.
			form = OrganizationGuForm(instance=organization)
		else:
			# Отправка данных POST; обработать данные.
			form = OrganizationGuForm(instance=organization, data=request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse(
								'revision_commissions:organization_gu',
													args=[organization.id]))
	elif type == "КВАЗИ":
		organization = get_object_or_404(Organization_KVAZI, id=organization_id)
		if organization.user != request.user:
			raise Http404
		
		if request.method != 'POST':
			# Форма заполняется данными текущей организации.
			form = OrganizationKvaziForm(instance=organization)
		else:
			# Отправка данных POST; обработать данные.
			form = OrganizationKvaziForm(instance=organization, data=request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse(
								'revision_commissions:organization_kvazi',
													args=[organization.id]))
	
	context = {'form': form, 'organization': organization}
	return render(request, 'revision_commissions/edit_organization.html', context)


def delete_organization(request, organization_id):
	organization = Organization.objects.get(id=organization_id)
	if organization.user == request.user or request.user.groups.filter(name="Commission").exists():
		organization.delete()
	return HttpResponseRedirect(reverse('revision_commissions:organizations'))


def register(request):
	# Регистрация пользователя
	if request.method != 'POST':
		form = UserAdminCreationForm()
	# if request = post
	else:
		form = UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			'''
			cd = form.cleaned_data
			email = cd.get("email")
			password = cd.get("password")
			user = authenticate(email=email, password=password)
			login(request, user)
			'''
			return HttpResponseRedirect(reverse('revision_commissions:login'))
	
	context = {'form': form}
	return render(request, "revision_commissions/register.html", context)


def login_view(request):
	# Логин
	if request.method != 'POST':
		form = LoginForm()
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			email = cd.get('email')
			password = cd.get('password')
			user = authenticate(request, username=email, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('revision_commissions:new_organization_choice'))
			else:
				context = {'form': form}
				return render(request, "revision_commissions/login.html", context)
	
	context = {'form': form}
	return render(request, "revision_commissions/login.html", context)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('revision_commissions:organizations'))


# For downloading the excel
@login_required
def download(request, organization_id, type):
	if type == "ГУ":
		org = Organization_GU.objects.get(id=organization_id)
		# Скачать может только пользователь создавший пост или из группы коммиссий
		if org.user == request.user or request.user.groups.filter(name="Commission").exists():
			arr = [
					org.annualFunding,
					org.finPrePeriod,
					org.finCurPeriod,
					org.finEndYear,
					org.cashExpense,
					org.dateLastCheck,
					org.dateReport,
					org.finViolations,
					org.volRecoverFin,
					org.volReceivableCurrent,
					org.volReceivablePrevious,
					org.payableCurrent,
					org.payablePrevious,
					org.illegalActions,
					org.disciplineSanctions,
					org.materialEthics,
					org.employeeEthics,
					org.administrativeMeasures,
					org.disciplineMeasures,
					org.firedViolation
				]
			data = generate_organization_data(arr, "ГУ")
		else:
			context = {'organization': org}
			return render(request, 'revision_commissions/organization.html', context)
	elif type == "КВАЗИ":
		org = Organization_KVAZI.objects.get(id=organization_id)
		if org.user == request.user or request.user.groups.filter(name="Commission").exists():
			arr = [
				org.annualFunding,
				org.finEndYear,
				org.cashExpense,
				org.dateLastCheck,
				org.dateReport,
				org.finViolations,
				org.volRecoverFin,
				org.volReceivableCurrent,
				org.volReceivablePrevious,
				org.payableCurrent,
				org.payablePrevious,
				org.illegalActions,
				org.disciplineSanctions,
				org.employeeEthics,
				org.administrativeMeasures,
				org.disciplineMeasures,
				org.firedViolation,
				org.volAuthorizedCapitalCurrent,
				org.volAuthorizedCapitalPrevious,
				org.volIncomeCurrent,
				org.volIncomePrevious,
				org.volDividentsCurrent,
				org.volAdministrativeSpendings,
			]
			data = generate_organization_data(arr, "КВАЗИ")
		else:
			context = {'organization': org}
			return render(request, 'revision_commissions/organization.html', context)

	import re
	'''Если в названии будут кавычки убирает их, иначе ошибка'''
	namesRegex = re.compile(r'"')  # Искать кавычки
	orgName = namesRegex.sub('', org.name)  # Заменить кавычки на ''
	data.insert(0, ["Наименование критерия", "Значение", "Балл"])
	export_to_excel(data, orgName)
	# type for .xlsx
	mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
	path = open(f'{BASE_DIR}/revision_commissions/exports/{orgName}.xlsx', 'rb')
	#mime_type, _ = mimetypes.guess_type(path)
	response = HttpResponse(path, content_type=mime_type)
	response['Content-Disposition'] = f"attachment; filename={orgName}.xlsx"

	# file deletes afterwards
	os.remove(f'{BASE_DIR}/revision_commissions/exports/{orgName}.xlsx')
	return response
	

@login_required
def table_view(request, organization_id, type):
	if type == "ГУ":
		org = Organization_GU.objects.get(id=organization_id)
		if org.user == request.user or request.user.groups.filter(name="Commission").exists():
			arr = [
				org.annualFunding,
				org.finPrePeriod,
				org.finCurPeriod,
				org.finEndYear,
				org.cashExpense,
				org.dateLastCheck,
				org.dateReport,
				org.finViolations,
				org.volRecoverFin,
				org.volReceivableCurrent,
				org.volReceivablePrevious,
				org.payableCurrent,
				org.payablePrevious,
				org.illegalActions,
				org.disciplineSanctions,
				org.materialEthics,
				org.employeeEthics,
				org.administrativeMeasures,
				org.disciplineMeasures,
				org.firedViolation
			]
			data = generate_organization_data(arr, "ГУ")

			# Update data
			org.score = data[-1][1]
			org.risk = data[-1][2]
			org.save()
			#data = generate_organization_data(arr)
		else:
			context = {'organization': org}
			return render(request, 'revision_commissions/organization.html', context)

	elif type == "КВАЗИ":
		org = Organization_KVAZI.objects.get(id=organization_id)
		if org.user == request.user or request.user.groups.filter(name="Commission").exists():
			arr = [
				org.annualFunding,
				org.finEndYear,
				org.cashExpense,
				org.dateLastCheck,
				org.dateReport,
				org.finViolations,
				org.volRecoverFin,
				org.volReceivableCurrent,
				org.volReceivablePrevious,
				org.payableCurrent,
				org.payablePrevious,
				org.illegalActions,
				org.disciplineSanctions,
				org.employeeEthics,
				org.administrativeMeasures,
				org.disciplineMeasures,
				org.firedViolation,
				org.volAuthorizedCapitalCurrent,
				org.volAuthorizedCapitalPrevious,
				org.volIncomeCurrent,
				org.volIncomePrevious,
				org.volDividentsCurrent,
				org.volAdministrativeSpendings,
			]
			data = generate_organization_data(arr, "КВАЗИ")

			# Temporary?
			org.score = data[-1][1]
			org.risk = data[-1][2]
			org.save()
		else:
			context = {'organization': org}
			return render(request, 'revision_commissions/organization.html', context)

	context = {'data': data, 'id': organization_id, 'type': type}
	return render(request, "revision_commissions/organization_info.html", context)
	

@login_required
def reports_view(request):
	if not request.user.groups.filter(name="Commission").exists():
		return HttpResponseRedirect(reverse('revision_commissions:index'))
	
	organizations_gu = Organization_GU.objects.all()
	organizations_kvazi = Organization_KVAZI.objects.all()
	organizations = chain(organizations_gu, organizations_kvazi)

	context = {'organizations': organizations}
	return render(request, 'revision_commissions/reports.html', context)


@login_required
def download_reports(request):
	if not request.user.groups.filter(name="Commission").exists():
		return HttpResponseRedirect(reverse('revision_commissions:index'))
	
	organizations_gu = Organization_GU.objects.all()
	organizations_kvazi = Organization_KVAZI.objects.all()
	organizations = chain(organizations_gu, organizations_kvazi)

	arr = [["Дата заполнения", "Наименование", "Баллы", "Группа риска", "ФИО сотрудника", "Номер телефона"]]

	for organization in organizations:
		arr.append([str(organization.updated_at), organization.name, organization.score, organization.risk, organization.user.first_name + " " + organization.user.last_name, organization.user.phone_number])

	export_to_excel(arr, "Report")
	# type for .xlsx
	mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
	path = open(f'{BASE_DIR}/revision_commissions/exports/{"Report"}.xlsx', 'rb')
	#mime_type, _ = mimetypes.guess_type(path)
	response = HttpResponse(path, content_type=mime_type)
	response['Content-Disposition'] = f"attachment; filename=Report.xlsx"

	# file deletes afterwards
	os.remove(f'{BASE_DIR}/revision_commissions/exports/Report.xlsx')

	return response


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = CustomUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Запрос на изменение пароля"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'revision-commission.herokuapp.com',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'revisioncommission@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})
 
