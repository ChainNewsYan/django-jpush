from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from service.models import JiGuangReg
from service.serializers.register_ser import RegisterCreateSerializer


class RegisterAPIView(CreateAPIView):
    model = JiGuangReg
    queryset = JiGuangReg.objects.all()
    serializer_class = RegisterCreateSerializer
    permission_classes = [IsAuthenticated, ]
