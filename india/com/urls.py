from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("aboutus/", views.Aboutus, name="Home"),
    path("enquiry/", views.Enquiry, name="Home"),
    path("contact/", views.contact, name="Home"),
    path("bookyourtour/", views.Bookyourtour, name="Home"),
    path("factorytour/", views.Factorytour, name="Home"),
    path("faq/", views.Faq, name="Home"),
    path("box/", views.BOX, name="Home"),
    path("bag/", views.Bag, name="Home"),
    path("cards/", views.Cards, name="Home"),
    path("christmas/", views.Christmas, name="Home"),
    path("festivals/", views.Festival, name="Home"),
    path("giftitem/", views.Giftitem, name="Home"),
    path("jounal/", views.Journal, name="Home"),
    path("papers/", views.Papers, name="Home"),
    path("seedpapers/", views.Seedpapers, name="Home"),
    path("star/", views.Star, name="Home"),
    path("stationary/", views.Stationary, name="Home"),



]