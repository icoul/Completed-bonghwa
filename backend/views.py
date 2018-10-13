from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

token = ""

def index(request):
    if token:
        return render(request, 'index.html')
    else:
        return redirect('test/')

def test(request):
    return render(request, 'index.html')

class Login(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=1).values()
    serializer_class = UserSerializer

    @list_route(method = ['get'])
    def get_list(self, request):
        contentList = []
        
        for query in Login.queryset:
            contentList.append(query)

        return JsonResponse({'contentList': contentList})
