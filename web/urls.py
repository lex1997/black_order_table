from django.urls import path
import views

urlpatterns = [
    path('table/', views.DataTableView.as_view(), name='data-table'),
]