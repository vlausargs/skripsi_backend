from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= '__all__'
class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields= '__all__'
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields= '__all__'
class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields= '__all__'
class EmployeePayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePayType
        fields= '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= '__all__'
class AttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attandance
        fields= '__all__'
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields= '__all__'
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields= '__all__'
class AttendaceCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendaceCode
        fields= '__all__'