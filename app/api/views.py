from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes #private routing
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets

from django.contrib.auth import get_user_model


from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import NotesSerializer, UserSerializer
from app.models import Notes



from django.contrib.auth.forms import UserCreationForm



#this where i need to make users with post
# changing the information that we can get from the token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['POST'])
# def createUser(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = User.objects.create_user(username=username, password=password)
#     user.save()
#     users = user.notes_set.all() # this makes its only get that users data
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)
#     # return Response({'successful': 'Username and password created'})


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer



    
@api_view(['POST'])
def createUser(request):
    # form = UserCreationForm


    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

        # # if not username or not password:
        #     # return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username,email=email,password=password)
    serializer = UserSerializer(user)

    return Response(serializer.data)

# @api_view(['GET'])
# def showUsers(request):
#     user=User
#     users = User.user_set.all() # this makes its only get that users data

#     # view = showUsers.as_view({'get': 'retrieve'})


#     response = view(request)
#     serializer_class = UserSerializer(users, many=True)

#     return Response(serializer_class.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.notes_set.all() # this makes its only get that users data
    serializer = NotesSerializer(notes, many=True)
    return Response(serializer.data)
#serilzier turns pythong into json to be parsed

# @api_view(['POST'])
# def create(request):

