from django.contrib import messages
from django.shortcuts import render
from drf_haystack.serializers import HaystackSerializer
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from drf_haystack.viewsets import HaystackViewSet
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

from .forms import SignUpForm
from .models import Car
from .search import CarIndex

class CarSerializer(HaystackSerializer):
    class Meta:
        index_classes=[CarIndex]
        fields =["name","colour","description"]


class CarSearchView(HaystackViewSet):
    index_models = [Car]
    serializer_class = CarSerializer

@api_view(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        username = request.data.get("username")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        raw_password = request.data.get("password1")
        password = make_password(raw_password)
        context={
            "username":username,
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":password
        }
        l=User(**context)
        l.save()
    return render(request, 'registration/signup.html')


@api_view(['POST','GET'])
def login(request):
    if request.method == 'POST':
        email=request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user.check_password(password):
                # return Response({"message":"login succesfully"})
                messages.success(request, 'user login successfully!')
        else:
            # return Response({"message":"invallid credentials"})
            messages.warning(request, 'invallid password')
    return render(request,'registration/login.html')