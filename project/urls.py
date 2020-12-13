from django.urls import path
from . import views

urlpatterns = [
    path('',views.upload_csvmodel,name="upload_csvmodel"),
    path('q2',views.question,name="question"),
    path('q3',views.questionth,name="questionth"),
]