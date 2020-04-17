from django.contrib import admin
from django.urls import path
from .views import index,sign_up,login_view,guide,loan,schemes,retailers,applyLoan,user_logout,merch

urlpatterns = [
    path('', index),
    path('signup/',sign_up),
    path('login/',login_view),
    path('guide/',guide,name='guide'),
    path('loan/',loan,name='loan'),
    path('schemes/',schemes,name='schemes'),
    path('retailers/',retailers,name='retailers'),
    path('applyLoan/',applyLoan,name='applyLoan'),
    path('logout/',user_logout,name='logout'),
    path('merchandiser/',merch,name='merch'),


]