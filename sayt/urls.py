from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("shop/", shop, name="shop"),
    path("quality/", quality, name="quality"),
]