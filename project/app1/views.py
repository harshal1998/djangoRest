from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .a import *


class add(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        sdata = s(data=request.data)
        if sdata.is_valid():
            sdata.save()
            return Response({"status": "successfully added", "msg": "data stored"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "failed to add", "msg": "data not stored"}, status=status.HTTP_400_BAD_REQUEST)


class view(APIView):
    def get(self, request):
        data = list(demo.objects.all().values('name', 'email', 'address', 'marks'))
        return Response(data, status=status.HTTP_201_CREATED)


class update(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        data = request.data['name']
        data1 = request.data['marks']
        demo.objects.filter(name=data).update(marks=data1)
        return Response("data updated successfully. refresh to see changes!", status=status.HTTP_202_ACCEPTED)


class delete(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        data = request.data['name']
        demo.objects.filter(name=data).delete()
        return Response("data updated successfully. refresh to see changes!", status=status.HTTP_202_ACCEPTED)
