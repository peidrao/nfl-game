import jwt

from django.conf import settings
from rest_framework import status, views, exceptions
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


class TokenIsValidView(views.APIView):
    def get(self, request):
        return Response(request.data)

    def post(self, request, *args, **kwargs):
        try:
            token = request.data["access"]
            decode = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            response = Response(
                status=status.HTTP_403_FORBIDDEN,
                data={"error": "access_token expired"},
            )
            return response
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed("access_token invalid token")
        except KeyError:
            raise exceptions.AuthenticationFailed("access_token invalid key")

        profile = Profile.objects.filter(is_active=True).get(id=decode["user_id"])
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)
