from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'medic/home.html'
    extra_context = {
            'title': 'MEDIC - Медицинская диагностика'
        }
