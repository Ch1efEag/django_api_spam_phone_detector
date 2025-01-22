from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
# , Spam
from .serializers import UserSerializer
# , SpamSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q
from rest_framework import serializers

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LoginView(TokenObtainPairView):
#     pass  # JWT authentication handles login

# class CustomTokenObtainPairSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, attrs):
#         phone_number = attrs.get('phone_number')
#         password = attrs.get('password')

#         # Custom authentication logic using phone_number instead of username/email
#         user = authenticate(phone_number=phone_number, password=password)
#         if not user:
#             raise serializers.ValidationError('Invalid credentials')

#         attrs['user'] = user
#         return attrs

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# class SpamMarkerView(generics.CreateAPIView):
#     serializer_class = SpamSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         spam_report, created = Spam.objects.get_or_create(
#             phone_number=phone_number,
#             defaults={'reported_by': request.user, 'report_count': 1}
#         )
#         if not created:
#             spam_report.report_count += 1
#             spam_report.save()

#         return Response({"message": "Reported successfully"}, status=status.HTTP_201_CREATED)

# class FindByNameView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         name = self.request.query_params.get('name', '')
#         return User.objects.filter(Q(username__startswith=name) | Q(username__icontains=name))

# class FindByNumberView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         phone_number = self.request.query_params.get('phone_number', '')
#         return User.objects.filter(phone_number=phone_number)
