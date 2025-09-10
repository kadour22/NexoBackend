from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions , throttling

from .serializers import RegistrationSerializer , ChangePasswordSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)