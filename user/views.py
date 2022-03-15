import hashlib
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import *
# Create your views here.

def get_info(request):
    data={
        'name':'yechunting',
        'age': 20
    }
    return JsonResponse(data)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    import hashlib
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            #验证用户名是否已存在
            try:
                User.objects.get(username = serializer.validated_data['username'])   
                #上一个语句如果没有报错，执行下一句，不允许注册 
                return Response('existed', status=status.HTTP_406_NOT_ACCEPTABLE)         
            except:
                #报错则没有取到，允许注册
                pass
                
            #密码的哈希保存
            m = hashlib.md5()
            m.update(serializer.validated_data['password'].encode())
            serializer.validated_data['password'] = m.hexdigest()
            serializer.save()
        else:
            return Response('unvalidated',status=status.HTTP_400_BAD_REQUEST)
        return Response('创建用户成功',status=status.HTTP_201_CREATED)
        
    #登录
    def logon(self, request):
        print(request.data)
        #验证用户名
        try:
            user = User.objects.get(username = request.data['username'])
        except:
            return Response('error', status=status.HTTP_404_NOT_FOUND)
        #将密码转化为哈希值
        m = hashlib.md5()
        m.update(request.data['password'].encode())
        m_password = m.hexdigest()
        #验证密码
        if m_password == user.password:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response('error', status=status.HTTP_404_NOT_FOUND)
    


