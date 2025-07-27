from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models_user import CustomUser
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'is_student', 'is_teacher']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_student': {'required': False},
            'is_teacher': {'required': False},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_role(request):
    return Response({
        'username': request.user.username,
        'is_student': request.user.is_student,
        'is_teacher': request.user.is_teacher,
        'is_superuser': request.user.is_superuser
    })