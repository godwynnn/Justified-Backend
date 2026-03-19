from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import IntegrityError

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    data = request.data
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    email = data.get('email', '')
    password = data.get('password', '')

    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # We use email as the username for simplicity in this setup
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    from django.contrib.auth import authenticate
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=User.objects.get(email=str(email).strip()).username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    })
