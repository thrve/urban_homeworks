from django.shortcuts import render
from django.views import View


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_view.html')


def function_based_view(request):
    return render(request, 'second_task/function_view.html')
