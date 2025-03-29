from django.urls import path
from .views import ComplimentView

urlpatterns = [
    path('compliment/', ComplimentView.as_view(), name='compliment'),
]