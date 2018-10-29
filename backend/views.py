from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

# 로그인 체크용 토큰
token = ""

# 초기 페이지
def index(request):
    return render(request, 'index.html')

# 로그인 페이지
def login(request):
    return render(request, 'index.html')

# 회원가입 페이지
def signUp(request):
    return render(request, 'index.html')

# 아이디, 비밀번호 찾기 페이지
def passChange(request):
    return render(request, 'index.html')


class Auth(viewsets.ModelViewSet):

    @list_route(method = ['get'])
    def get_token(self, request):
        return JsonResponse({'token': token})

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