from django.urls import path, register_converter
from horoscope import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path('<yyyy:sign_zodiac>', views.get_info_about_sign_zodiac_by_number, name='get_yyyy_converters'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number, name='get_info_about_sign_zodiac_by_number'),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='get_info_about_sign_zodiac'),

]
