from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route

from .forms import UploadFileForm, mentionForm
from .models import Contents, User
from .serializer import ContentsSerializer, UserSerializer

from django.core.exceptions import ObjectDoesNotExist

import os
import uuid
import string
import random
from time import strftime
from django.utils import timezone
from hashlib import sha256
from django.core import serializers
from django.core.mail import send_mail
from django.db.models import OuterRef, Subquery, Count, IntegerField, Q

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

        user = request.session['user']
        return JsonResponse({'user': user})

    #로그인
    @list_route(method = ['get'])
    def login(self, request, username, password):
        try:
            query = User.objects.get(is_active=1, username=username, password=password)
        except ObjectDoesNotExist as e:
            print('login failed')
            print(e)
            return JsonResponse({'user': {}})
        
        user = {'id': query.id, 'username': query.username, 'email': query.email, 'is_staff': query.is_staff}
        request.session['user'] = user

        return JsonResponse({'user': user})

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
            user = User(username = username,                # 계정명
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

#모든 포스트를 가져온다
def get_all_post(minPage, maxPage, username):
    return list(Contents.objects.filter(Q(deleted=0), \
        (Q(contents__startswith='!') & Q(username=username)) | \
        Q(contents__startswith='!%s ' % username) | \
        ~Q(contents__startswith='!'))
        .order_by('-createdDate').values()[minPage:maxPage])

#나에게 온 멘션만 가져온다
def get_mentions(minPage, maxPage, username):
    return list(Contents.objects.filter(Q(deleted=0), \
        Q(contents__contains=username), \
        ~Q(contents__startswith='!')) \
        .order_by('-createdDate').values()[minPage:maxPage])
    
#내가 작성한 포스트만 가져온다
def get_my_post(minPage, maxPage, username):
    return list(Contents.objects.filter(deleted=0, username=username).order_by('-createdDate').values()[minPage:maxPage])

#나에게 온 또는 내가 보낸 비밀멘션만 가져온다
def get_secret_mention(minPage, maxPage, username):
    return list(Contents.objects.filter(Q(deleted=0), \
        (Q(contents__startswith='!') & Q(username=username)) | \
        Q(contents__startswith='!%s ' % username)) \
        .order_by('-createdDate').values()[minPage:maxPage])

#파일 업로드
def handle_uploaded_file(f, fname):
    with open('./static/image/' + fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#Date타입을 yyyy. mm. dd의 String타입으로 변경
def convertDateToString(objs):
    for obj in objs:
        obj['convert_date'] = obj['createdDate'].strftime("%Y. %m. %d %H:%M:%S")
        obj['createdDate'] = obj['createdDate'].strftime("%Y%m%d%H%M%S")
    
    return objs

class Post(viewsets.ModelViewSet):
    #포스트 가져오기
    @list_route(methods= ['get'])
    def get_posts(self, request, page, sortOption):
        #조회용 함수맵(전체, 멘션, 자신)
        functions = {'all': get_all_post, \
            'mention': get_mentions, \
            'my': get_my_post, \
            'secret': get_secret_mention}
        username = request.session['user']['username']
        minPage = (int(page) - 1) * 50 #해당 페이지 최소번호
        maxPage = int(page) * 50 #해당 페이지 최대번호
        posts = functions[sortOption](minPage, maxPage, username) #포스트 조회

        return JsonResponse({'posts': convertDateToString(posts)})

    #포스트 등록
    @list_route(methods= ['post'])
    def send_post(self, request):
        writer = request.session['user']['username']
        mentionId = request.POST['mentionId']
        mentionIndex = request.POST['mentionIndex']
        mentionDepth = request.POST['mentionDepth']

        # mentionIndex가 0이 아니라는 것은 해당 포스트이 멘션이라는 것이므로 depth를 구한다.
        if mentionIndex:
            query = Contents.objects.filter(deleted=0, mentionIndex=mentionIndex)

            #mentionIndex가 같은 post 중 선택한 mention의 depth가 최상위일 경우
            if query.latest('mentionDepth').mentionDepth == mentionDepth:
                #해당 depth에 +1을 해주어 depth를 쌓아간다.
                mentionDepth = int(mentionDepth) + 1
            else:
                #최상위가 아닐 경우 새로운 가지를 만들기 위해 해당 mention의 id를 index로 넣어준다.
                mentionIndex = mentionId
                mentionDepth = 1
        else:
            mentionIndex = mentionId
        
        # 아이디 중복 체크
        if not username_duple_check(writer):
            return JsonResponse({'result': '0', 'message': '올바른 계정이 아닙니다. 재로그인 후 다시 시도해주세요.'})

        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            filename = ''
            if 'image' in request.FILES:
                extention = os.path.splitext(str(request.FILES['image']))[1]
                now = timezone.now().strftime("%Y%m%d%H%M%S%f")
                filename = now + extention
                handle_uploaded_file(request.FILES['image'], filename)
            
            try:
                content = Contents(contents = request.POST['content'],       # 내용
                                username = writer,                           # 계정명
                                image = filename,                            # 이미지 이름
                                mentionIndex = mentionIndex,                 # 멘션번호
                                mentionDepth = mentionDepth,                 # 멘션순서
                                createdDate = timezone.now())                # 작성일
                content.save()
            except Exception as e:
                print('Send post failed')
                print(e)
                return JsonResponse({'result': '0', 'message': '포스트 업로드에 실패했습니다.'})            

        return JsonResponse({'result': '1', 'message': ''})

    #포스트 삭제
    @list_route(methods= ['post'])
    def delete_post(self, request, id):
        try:
            Contents.objects.filter(id=id).update(deleted=1)
        except Exception as e:
            print('Delete post failed')
            print(e)
            return JsonResponse({'result': 'false'})            

        return JsonResponse({'result': 'true'})

    #포스트 가져오기
    @list_route(methods= ['post'])
    def get_mentions(self, request):
        form = mentionForm(request.POST, request.FILES)
        
        if form.is_valid():
            mentionIndex = request.POST['mentionIndex']
            mentionDepth = request.POST['mentionDepth']
            mentions = []

            #mentionIndex가 0이면 최초의 post이기 때문에 루프를 하지 않음
            while mentionIndex != '0':
                #해당되는 mention보다 낮은 depth의 post들을 조회
                mention = list(Contents.objects\
                    .filter(Q(deleted=0) & \
                        ((Q(mentionIndex=mentionIndex) & Q(mentionDepth__lt=mentionDepth)) | \
                        Q(id=mentionIndex))).order_by('-createdDate').values())
                
                #list에 추가
                mentions.extend(mention)
                #해당 mention의 최초시점인 post를 조회
                parentPost = Contents.objects.get(id=mentionIndex)

                #최초의 post가 가진 mentionIndex와 Depth로 교체.
                mentionIndex = parentPost.mentionIndex
                mentionDepth = parentPost.mentionDepth

        return JsonResponse({'mentions': convertDateToString(mentions)})
