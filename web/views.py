from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматически входить после успешной регистрации
            login(request, user)
            return redirect('data-table')  # Перенаправление на вашу страницу после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class DataTableView(ListView):
    model = Product
    template_name = 'web/data_table.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
