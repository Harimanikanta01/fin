from .models import Nari
from rest_framework import serializers
from .models import Banner
from .models import*
class Jay(serializers.ModelSerializer):
    class Meta:
        model=Nari
        fields="__all__"
class Ba(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields="__all__"
class Cre(serializers.ModelSerializer):
    class Meta:
        model=Create
        fields="__all__"
class Cir(serializers.ModelSerializer):
    class Meta:
        model=Circle
        fields="__all__"
class P11(serializers.ModelSerializer):
    class Meta:
        model=P1
        fields="__all__"
class P22(serializers.ModelSerializer):
    class Meta:
        model=P2
        fields="__all__"
class add1(serializers.ModelSerializer):
    class Meta:
        model=Add
        fields="__all__"
class Discount1(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields="__all__"
class Mobile1(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields="__all__"
class account1(serializers.ModelSerializer):
    class Meta:
        model=account
        field="__all__"
class Cart12(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
class product31(serializers.ModelSerializer):
    class Meta:
      model=product3
      fields="__all__"

