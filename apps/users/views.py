import re
from django.shortcuts import render
from rest_framework.views import APIView
from apps.users.models import CustomUser
from django.contrib.sessions.models import Session
from .serializers import UserSerializer, UserSerializerCustom, UserTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from datetime import datetime
# Create your views here.
class UserList(APIView):
    
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)
    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# generic class to list a model
class GeneralApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()

# Example using generic class
class UserListApiView(GeneralApiView):
    serializer_class = UserSerializer



class UserDetailView(APIView):
    """View a Author detail

    * Requires: token authentication
    * Any user can access
    """
    def get(self, request, pk=None, format=None):
        
        user = CustomUser.objects.get(id=pk)
        user_serialized = UserSerializer(user, many=False)
        return Response(user_serialized.data)

    def put(self, request, pk=None):

        try:
            user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            user = None
            # raise Http404("Poll does not exist")
            return Response({'message':'Id do no exist'}, status=status.HTTP_404_NOT_FOUND)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            user_serialized = UserTokenSerializer(user).data
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                if created:
                    return Response({'message': 'login successful', 'token': token.key, 'user':user_serialized}, status=status.HTTP_201_CREATED)
                else:
                    all_sesions = Session.objects.filter(expire_date__gte = datetime.now())
                    # delete all sesions around user
                    if all_sesions.exists():
                        for session in all_sesions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({'message': 'login successful', 'token': token.key, 'user':user_serialized}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'this user cant login'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'done'}, status=status.HTTP_200_OK)