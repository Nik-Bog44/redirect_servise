from django.urls import path
from .views import CreateEmailRedirectView, HomeView, RedirectToUrlView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", CreateEmailRedirectView.as_view()),
    path("redirect/", RedirectToUrlView.as_view()),

]
