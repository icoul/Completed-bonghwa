from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

import uuid
from hashlib import sha256

# 초기 페이지
def index(request):
    return render(request, 'index.html')


class Auth(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @list_route(method = ['get'])
    def get_token(self, request):
        token = request.session['token']
        return JsonResponse({'token': token})

    @list_route(method = ['get'])
    def login(self, request, id, password):
        try:
            user = User.objects.get(is_active=1, username=id, password=password)
        except:
            print('로그인 실패')
            return False
        
        request.session['token'] = str(uuid.uuid4())
        return JsonResponse({'token': request.session['token']})

    @list_route(method = ['get'])
    def logout(self, request):
        request.session['token'] = ''
        return HttpResponse(status=200)
        

''' class Login(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=1).values()
    serializer_class = UserSerializer

    @list_route(method = ['get'])
    def get_list(self, request):
        contentList = []
        
        for query in Login.queryset:
            contentList.append(query)

        return JsonResponse({'contentList': contentList})
 '''