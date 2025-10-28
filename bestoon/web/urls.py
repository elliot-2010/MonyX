from django.urls import path 
from . import views


urlpatterns = [
    path("submit/expense", view=views.submit_expense, name="submit_expense"),
    path("", view=views.main, name="main"),
    path("submit/income", view=views.submit_income, name="submit_income"),
    path("register/", view=views.register, name="register"),
    path('q/generalstat', view=views.generalstat, name='generealstat'),
    #path('login', view=views.login, name="login"),
    ]
