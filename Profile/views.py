from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer,UpdateProfileSerializer
from .models import Profile

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

class UpdateProfileData(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)