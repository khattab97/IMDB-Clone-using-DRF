from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
from userauth import models


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['Response'] = 'Successfully Registered'
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key

        else:
            data = serializer.errors

        return Response(data)
