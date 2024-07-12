import json
import os

from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render

from medic.models import Procedure


class HomeView(TemplateView):
    template_name = 'medic/home.html'
    extra_context = {
            'title': 'MEDIC - Медицинская диагностика'
        }


class ProcedureListView(ListView):
    model = Procedure
    extra_context = {
        'title': "Список услуг"
    }


class ProcedureDetailView(DetailView):
    model = Procedure

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()
        item = Procedure.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f"{item.name}"
        return context_data


class ContactsView(TemplateView):
    template_name = "medic/contacts.html"
    extra_context = {
        'title': "Contact Us"
    }

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            user_contacts = {
                'name': name,
                'phone': phone,
                'message': message
            }
            # Запись в уже существующий файл с данными
            if os.path.isfile('data.json'):
                with open('data.json', 'r') as file:
                    user_data: list[dict] = json.load(file)
                    user_data.append(user_contacts)
                with open('data.json', 'w') as file:
                    json.dump(user_data, file, indent=4)
                # Вывод JSON в терминал
                print(user_data)
            # Создание файла и первая запись данных
            else:
                with open('data.json', 'w') as file:
                    json.dump([user_contacts], file, ensure_ascii=False, indent=4)

        return render(request, 'medic/contacts.html')
