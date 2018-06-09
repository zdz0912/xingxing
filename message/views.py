# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    #读取
    #  all_message=UserMessage.objects.all()
    #
    # for message in all_message:
    #     print message.name

    #存储
    # user_message=UserMessage()
    # user_message.name="zdz"
    # user_message.message='test_input'
    # user_message.address="fuzhou"
    # user_message.email="123@321.com"
    # user_message.obj_id="efg"
    #
    # user_message.save()

    #从html中读取数据，存储到数据库
    # if request.method=="POST":
    #     name=request.POST.get('name','')
    #     message=request.POST.get('message','')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message=UserMessage()
    #     user_message.name=name
    #     user_message.message=message
    #     user_message.address=address
    #     user_message.email=email
    #     user_message.save()

    #删除


    return render(request,'message_form.html')