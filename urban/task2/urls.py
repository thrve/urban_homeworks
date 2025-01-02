#!/usr/bin/env python


from django.urls import path
from .views import ClassBasedView, function_based_view

urlpatterns = [
    path('class_view/', ClassBasedView.as_view(), name='class_view'),
    path('function_view/', function_based_view, name='function_view'),
]
