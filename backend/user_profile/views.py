from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.serializer import UserSerializer
from user_profile.services import get_user_by_id


class UserView(APIView):
    """
    Displaying and updating user profile
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = get_user_by_id(request.user.pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = get_user_by_id(request.user.pk)
        context = {'country': request.data.get('country'), 'city': request.data.get('city'),
                   'street': request.data.get('street'), 'phone': request.data.get('phone')}
        serializer = UserSerializer(user, request.data, partial=True, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
