from django.http import HttpResponse, request
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token


# Create your views here.
class add(APIView):
    def get(self, request):
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request):
        sdata = demos(data=request.data)
        if sdata.is_valid():
            sdata.save()
            return Response(({"status": "success", "reason": "Data stored"}), status=status.HTTP_201_CREATED)
        else:
            return Response(({"status": "failed", "reason": "Data not stored"}), status=status.HTTP_201_CREATED)


class view(APIView):
    def get(self, request):
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)


class update(APIView):
    def get(self, request):
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request):
        demo.objects.filter(address=request.data['address']).update(marks=500)
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)


class display(APIView):
    def get(self, request):
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)


class data(viewsets.ModelViewSet):
    queryset = demo.objects.all()
    serializer_class = demos

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# def a(request):
#     data = demo.objects.all()
#     print(data)
#     for i in data:
#         print(i.name,i.email,i.address,i.marks)
#     return render(request, 'a.html', {"data": data})
