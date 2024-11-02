from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, RedirectView


# def index(request):
#     return render(request, 'common/home-page.html')


class IndexView(TemplateView):
    template_name = 'common/home-page.html'
    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/home-page-logged-in.html']
        else:
            return ['common/home-page.html']


class RedirectHomeView(RedirectView):
    url = reverse_lazy('home page')
