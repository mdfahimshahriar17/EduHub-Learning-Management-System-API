from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
from accounts.serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    ForgotPasswordSerializer,
    ResetPassword
)

User = get_user_model()

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        try:
            if serializer.is_valid():
                user = serializer.save()
            return Response(
                {
                    'detail':'Registration Successful',
                    'email':user.email,
                    'role':user.role
                }
            )
        except:
            return Response(
                {
                    "error":"Password does not match!"
                }
            )

class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            token = RefreshToken(request.data['refresh_token'])
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                 return Response(
                     {'detail':'User does not exist'}
                )

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            reset_link = f"{settings.FRONTEND_URL}/reset-password?uid={uid}&token={token}"
            
            send_mail(
                subject="Reset your password",
                message=f"Click the link to reset your password:\n {reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )

            return Response(
                     {'detail':'Mail sent successfully'}
                 )


class ResetPasswordView(APIView):
    pass