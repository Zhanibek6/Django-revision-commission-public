"""Определяет схемы URL для revision_commissions."""

from django.urls import path, include
from . import views #, api_views
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy
from rest_framework import routers

app_name = 'revision_commissions'

# api
''' 
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'organizations', api_views.OrganizationViewSet)
'''

urlpatterns = [
	# Домашняя страница
	path('', views.index, name='index'),
	# Вывод всех организаций
	path('organizations/', views.organizations, name='organizations'),
	# Страница просмотра данных организации ГУ
	path('organizations/gu/<int:organization_id>/', views.organization_gu, name='organization_gu'),
	# Страница просмотра данных организации КВАЗИ
	path('organizations/kvazi/<int:organization_id>/', views.organization_kvazi, name='organization_kvazi'),
	# Страница для создания орг
	path('new_organization/', views.new_organization_choice, name="new_organization_choice"),
	# Страница для добавления организации ГУ.
	path('new_organization/gu/', views.new_organization_gu, name='new_organization_gu'),
	# Страница для добавления организации КВАЗИ.
	path('new_organization/kvazi/', views.new_organization_kvazi, name='new_organization_kvazi'),
	# Страница для редактирования данных организации.
	path('edit_organization/<int:organization_id>/<str:type>', views.edit_organization, name='edit_organization'),
	# Страница для регистрации	
	path('register/', views.register, name="register"),
	# Страница для логина
	path('login/', views.login_view, name="login"),
	# Выход из аккаунта
	path('logout/', views.logout_view, name="logout"),
	# Для скачивания файла
	path('organizations/<int:organization_id>/download/<str:type>', views.download, name='download'),
	# Для вывода информаций об организаций в виде таблицы на вебсайте
	path('organizations/<int:organization_id>/table/<str:type>', views.table_view, name="orgnaization_info"),
	# Для удаления организаций
	path('organizations/<int:organization_id>/delete/', views.delete_organization, name="delete_organization"),
	# Показ отчетов от пользователей
	path('reports/', views.reports_view, name="reports"),
	# Вывод отчетов
	path('download_reports/', views.download_reports, name="download_reports"),
	# для сброса пароля
	path("password_reset/", views.password_reset_request, name="password_reset"),
]	
