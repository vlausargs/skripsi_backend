from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/Company',CompanyViewSet, 'Company')
router.register('api/Division',DivisionViewSet, 'Division')
router.register('api/Position',PositionViewSet, 'Position')
router.register('api/EmployeeType',EmployeeTypeViewSet, 'EmployeeType')
router.register('api/EmployeePayType',EmployeePayTypeViewSet, 'EmployeePayType')
router.register('api/Employee',EmployeeViewSet, 'Employee')
router.register('api/Attandance',AttandanceViewSet, 'Attandance')
router.register('api/Message',MessageViewSet, 'Message')
router.register('api/Feed',FeedViewSet, 'Feed')
router.register('api/AttendaceCode',AttendaceCodeViewSet, 'AttendaceCode')

urlpatterns = router.urls