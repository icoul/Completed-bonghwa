from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

from django.core.exceptions import ObjectDoesNotExist

import uuid
import string
import random
from django.utils import timezone
from hashlib import sha256
from django.core import serializers
from django.core.mail import send_mail

# 초기 페이지
def index(request):
    return render(request, 'index.html')

# 아이디 중복 체크
def username_duple_check(username):
    return User.objects.filter(is_active=1, username=username).count()

# 아이디, 이메일 유저 체크
def find_pass_user_check(username, email):
    try:
        return User.objects.filter(is_active=1, username=username, email=email).get()
    except ObjectDoesNotExist:
        return '0'

#랜덤 비밀번호 생성
def pass_generator(size=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

#비밀번호 SHA256으로 변경
def encrypt_string(value):
    return sha256(value.encode()).hexdigest()

class Auth(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    #로그인 상태 체크용 토큰 조회
    @list_route(method = ['get'])
    def get_user(self, request):
        if (not 'user' in request.session):
            request.session['user'] = {}

        return JsonResponse({'user': request.session['user']})

    #로그인
    @list_route(method = ['get'])
    def login(self, request, username, password):
        try:
            query = User.objects.get(is_active=1, username=username, password=password)
        except ObjectDoesNotExist:
            print('login failed')
            return JsonResponse({'user': {}})
        
        user = {'id': query.id, 'username': query.username, 'email': query.email, 'is_staff': query.is_staff}
        request.session['user'] = user
        print(request.session['user'])
        return JsonResponse({'user': request.session['user']})

    #로그아웃
    @list_route(method = ['get'])
    def logout(self, request):
        request.session['user'] = {}
        return HttpResponse(status=200)

    #회원가입
    @list_route(method = ['post'])
    def signUp(self, request, username, password, email):
        # result = 회원가입 결과
        # message = 회원가입 결과 알림메시지

        # 아이디 중복 체크
        if username_duple_check(username):
            return JsonResponse({'result': '0', 'message': '이미 가입된 아이디입니다.'})

        try:
            user = User(username = username,                      # 계정명
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

    #비밀번호 찾기
    @list_route(method = ['post'])
    def find_pass(self, request, username, email):
        if not find_pass_user_check(username, email):
            print("not have")
            return JsonResponse({'result': '0', 'message': '해당되는 아이디, 이메일의 유저가 존재하지 않습니다.'})
        
        newPass = pass_generator(6)    #임시 랜덤 비밀번호 생성
        encryptPass = encrypt_string(newPass)    #임시 비밀번호 SHA256타입으로 변환

        try:
            result = send_mail(
                '임시 비밀번호입니다.',
                username + '님의 임시 비밀번호는 ' + newPass + ' 입니다.',
                'icoul35@gmail.com',
                [email],
                fail_silently=False,
                auth_user='icoul35@gmail.com',
                auth_password='ha759461'
            )

            if not result:
                return JsonResponse({'result': '0', 'message': '비밀번호 찾기에 실패했습니다.'})
        except Exception as e:
            print('send_mail failed')
            print(e)
            return JsonResponse({'result': '0', 'message': '비밀번호 찾기에 실패했습니다.'})
        
        #임시 비밀번호 저장
        result = User.objects.filter(is_active=1, username=username, email=email).update(password=encryptPass)

        return JsonResponse({'result': '1', 'message': '임시 비밀번호를 이메일로 발송했습니다.'})

class Post(viewsets.ModelViewSet):
    #글 가져오기
    @list_route(methods= ['get'])
    def get_posts(self, request):
        posts = list(Contents.objects.all().order_by('-created_date').values())
        
        return JsonResponse({'posts': posts})
