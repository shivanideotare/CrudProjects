from django.urls import path
from .views import student,update

urlpatterns = [
    path('stu/', student),
    path('update/<int:id>/', update),
]
