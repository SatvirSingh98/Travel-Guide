from django.urls import path
from .views import AboutView, ContactView, DescriptionView

app_name = 'Travel'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('destination/<name>/', DescriptionView.as_view(), name='destination_description'),
]