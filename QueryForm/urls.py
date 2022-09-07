from django.urls import path
from .views import QueryForm

urlpatterns = [
    path('', QueryForm.as_view(), name='form'),
]