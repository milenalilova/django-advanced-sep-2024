from django.urls import path, include

from employeesApp.common.views import IndexView, RedirectHomeView

urlpatterns = [
    path('', IndexView.as_view(), name='home page'),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect home page'),
]
