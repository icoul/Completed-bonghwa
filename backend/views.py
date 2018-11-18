from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

import uuid
from django.utils import timezone
from hashlib import sha256

# 초기 페이지
def index(request):
    return render(request, 'index.html')

# 아이디 중복 체크
def idDupleCheck(id):
    return User.objects.filter(is_active = 1, username = id).count()


class Auth(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    #로그인 상태 체크용 토큰 조회
    @list_route(method = ['get'])
    def get_token(self, request):
        token = request.session['token']
        return JsonResponse({'token': token})

    #로그인
    @list_route(method = ['get'])
    def login(self, request, id, password):
        try:
            user = User.objects.get(is_active=1, username=id, password=password)
        except:
            print('login failed')
            return HttpResponse(status=500)
        
        request.session['token'] = str(uuid.uuid4())
        return JsonResponse({'token': request.session['token']})

    #로그아웃
    @list_route(method = ['get'])
    def logout(self, request):
        request.session['token'] = ''
        return HttpResponse(status=200)

    #회원가입
    @list_route(method = ['post'])
    def signUp(self, request, id, password, email):
        # result = 회원가입 결과
        # message = 회원가입 결과 알림메시지

        # 아이디 중복 체크
        if idDupleCheck(id):
            return JsonResponse({'result': '0', 'message': '이미 가입된 아이디입니다.'})

        try:
            user = User(username = id,                      # 계정명
                        password = password,                # 계정 비밀번호
                        email = email,                      # 이메일
                        is_superuser = 0,                   # 운영자 여부
                        is_staff = 0,                       # 스태프 여부
                        is_active = 1,                      # 계정 삭제여부
                        date_joined = timezone.now())       # 계정 생성일
            user.save()
        except:
            print('signUp failed')
            return JsonResponse({'result': '0', 'message': '회원가입에 실패했습니다.'})

        return JsonResponse({'result': '1', 'message': '회원가입에 성공했습니다.'})


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