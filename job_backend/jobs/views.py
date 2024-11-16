from django.shortcuts import render
from jobs.models import Company
from jobs.serializers import UserSerializer, CompanySerializer
from rest_framework import generics
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework import permissions


# GET and POST
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): # can only view companies created by you
        user = self.request.user
        return Company.objects.filter(owner=user)
    
    def perform_create(self, serializer):
       if serializer.is_valid():
          serializer.save(owner=self.request.user)
       else:
           print(serializer.errors)


# For Single snippet: GET, PUT, DELETE
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]



# POST
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

