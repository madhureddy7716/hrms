from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    logout
)

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register_api(request):

    User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )

    return Response(
        {
            'message': 'User Registered Successfully'
        }
    )


@api_view(['POST'])
def login_api(request):

    user = authenticate(
        username=request.data['username'],
        password=request.data['password']
    )

    if user:

        return Response(
            {
                'message': 'Login Success'
            }
        )

    return Response(
        {
            'message': 'Invalid Credentials'
        }
    )


@api_view(['POST'])
def logout_api(request):

    logout(request)

    return Response(
        {
            'message': 'Logout Success'
        }
    )