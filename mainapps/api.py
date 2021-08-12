from .models import *
from .serializers import *
from rest_framework import viewsets,permissions

class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer
class DivisionViewSet(viewsets.ModelViewSet):
    queryset= Division.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DivisionSerializer
class PositionViewSet(viewsets.ModelViewSet):
    queryset= Position.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PositionSerializer
class EmployeeTypeViewSet(viewsets.ModelViewSet):
    queryset= EmployeeType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeTypeSerializer
class EmployeePayTypeViewSet(viewsets.ModelViewSet):
    queryset= EmployeePayType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeePayTypeSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer
class AttandanceViewSet(viewsets.ModelViewSet):
    queryset= Attandance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttandanceSerializer
class MessageViewSet(viewsets.ModelViewSet):
    queryset= Message.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializer
class FeedViewSet(viewsets.ModelViewSet):
    queryset= Feed.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FeedSerializer
class AttendaceCodeViewSet(viewsets.ModelViewSet):
    queryset= AttendaceCode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttendaceCodeSerializer