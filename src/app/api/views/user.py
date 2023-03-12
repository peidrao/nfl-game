from rest_framework import status, views
from rest_framework.response import Response
from app.api.serializers.user import ProfileSerializer


from app.domain.models.profile import Profile


class ProfileCreateView(views.APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            profile = serializer.save()
            profile.set_password(profile.password)
            profile.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
