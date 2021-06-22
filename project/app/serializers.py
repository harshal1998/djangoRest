from rest_framework import serializers
from .models import *


class demos(serializers.ModelSerializer):
    class Meta:
        model = demo
        fields = "__all__"
