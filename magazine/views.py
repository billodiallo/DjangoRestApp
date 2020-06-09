from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from magazine.serializers import UserSerializer
from rest_framework.response import Response
from magazine.models import User
from rest_framework import status
# Create your views here.


class UserCreateListAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ 
        create a user 
        """
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = serializer.data
        response = {
            "user": user,
            "message": "user created successfully"
        }
        return Response(response, status=status.HTTP_201_CREATED)
