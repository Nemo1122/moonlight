"""moonlight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path

urlpatterns = [
    path('budgets/', BudgetListView.as_view(), name='budgets'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget'),
    path('wastebook/', WasteBookListView.as_view(), name='wastebooks'),
    path('wastebook/<int:pk>/', WasteBookDetailView.as_view(), name='wastebook'),
    path('category1/', Category1ListView.as_view(), name='category1s'),
    path('category1/<int:pk>/', Category1DetailView.as_view(), name='category1'),
    path('category2/', Category2ListView.as_view(), name='category2s'),
    path('category2/<int:pk>/', Category2DetailView.as_view(), name='category2'),
]
