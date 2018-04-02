from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.contrib.auth import logout, login, authenticate

from .models import *
from .serializers import *

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
@parser_classes((JSONParser,))
def app_login(request):
    uname = request.data.get('username')
    passwd = request.data.get('password')
    user = authenticate(username=uname, password=passwd)
    if user:
        login(request._request, user)
    else:
        return Response({"token": ""}, status=status.HTTP_403_FORBIDDEN)
    
    # generate token for client
    token, _ = Token.objects.get_or_create(user=user)
    r = JsonResponse({"token": token.key}, status=status.HTTP_202_ACCEPTED)
    # r.set_cookie(key="token", value=token.key)
    return r

@api_view(['POST'])
@parser_classes((JSONParser,))
def app_register(request):
    uname = request.data.get('username')
    passwd = request.data.get('password')
    fname = request.data.get('first_name')
    lname = request.data.get('last_name')
    email = request.data.get('email')

    try:
        u = User(username=uname, password=passwd, first_name=fname, last_name=lname, email=email)
        u.set_password(passwd)
        u.save()
        a = AdvancedUser(uid = u)
        a.save()
        return Response(status=status.HTTP_201_CREATED)
    
    # user already exist in database
    except IntegrityError:
        return Response(status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
#@permission_classes((IsAuthenticated,))
def app_logout(request):
    logout(request._request)
    request.user.auth_token.delete()
    r = Response() 
    # r.delete_cookie('token')
    r.status_code = status.HTTP_200_OK
    return r

@api_view(['GET'])
@parser_classes((JSONParser,)) 
#@permission_classes((IsAuthenticated,))
def get_posts(request):
    posts = Post.objects.all()
    posts_dict_list = []
    for post in posts:
        posts_dict_list.append(PostSerializer(post).data)
    return JsonResponse({"posts" : posts_dict_list}, safe=True)

@api_view(['GET'])
@parser_classes((JSONParser,)) 
#@permission_classes((IsAuthenticated,))
def get_post_by_title(request):
    pid = request.query_params.get('title')
    post = Post.objects.filter(title = pid)
    if len(post) <= 0:
        return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
    post_ser = PostSerializer(post[0])
    
    post_contents = PostContent.objects.filter(pid = post[0])
    print(post_contents)
    post_dict_list = []
    for post_content in post_contents:
        post_dict_list.append(PostContentSerializer(post_content).data)
    return JsonResponse({'title' : post_ser.data, 'content' : post_dict_list}, safe=True)
    
@api_view(['GET'])
@parser_classes((JSONParser,)) 
#@permission_classes((IsAuthenticated,))
def get_user_by_username(request):
    uid = request.query_params.get('username')
    users = User.objects.filter(username = uid)
    if len(users) > 0:
        advance = AdvancedUser.objects.filter(uid=users[0])
        if len(advance) > 0:
            _ser = AdvancedUserSerializer(advance[0])
        else:
            _ser = UserSerializer(users[0])
        return JsonResponse(_ser.data)       
    else:
        return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
    advance = AdvanceUser.objects.filter(uid=uid)
    advance_ser = AdvancedUserSerializer(advance)
    return JsonResponse(advance_ser.data, safe=True)
    
    
@api_view(['GET'])
@parser_classes((JSONParser,)) 
#@permission_classes((IsAuthenticated,))
def get_system_mesg_by_username(request):
    uid = request.query_params.get('username')
    users = User.objects.filter(username = uid)
    if len(users) > 0:
        user = users[0]
        mesgs = SystemMesg.objects.filter(uid = user)
        mesg_dict_list = []
        for mesg in mesgs:
            mesg_dict_list.append(SystemMesgSerializer(mesg).data)
        return JsonResponse({'mesg' : mesg_dict_list}, safe=True)
    else:
        return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)