from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthenticationAPIView(APIView):
    authentication_classes = [JWTAuthentication]

# Create your views here.
class ExampleProtectedView(JWTAuthenticationAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This route is protected! You can access this :)"})
    
class ExampleAdminOnlyView(JWTAuthenticationAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "You are an admin!"})
    