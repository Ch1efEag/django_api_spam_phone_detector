from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User
# , Spam
from rest_framework_simplejwt.tokens import RefreshToken  # Import JWT token class
from rest_framework.views import APIView
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'password', 'phone_number', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email')
        )
        if password:
            user.set_password(password)
            user.save()
        return user

# class LoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     password = serializers.CharField(write_only=True)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             phone_number = serializer.validated_data['phone_number']
#             password = serializer.validated_data['password']
#             user = authenticate(phone_number=phone_number, password=password)  # Changed from email to phone_number
            
#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'access_token': str(refresh.access_token),
#                     'refresh_token': str(refresh)
#                 })
#             else:
#                 return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SpamSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = U
    #     fields = ['phone_number','name','count']
    # def create(self, validated_data):
    #     user = Spam.objects.create_spam(
    #         name=validated_data['name'],
    #         phone_number=validated_data['phone_number'],
    #         count=validated_data.get('count')
    #     )
    #     return user
