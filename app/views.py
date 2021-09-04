from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import userdata
from .serializers import useSerializer


# This view handels student and teacher user

class studentdata(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes      = [IsAuthenticated]

    def get(self, request, formate=None, id=None):
        try:
            stu         = userdata.objects.all()
            serializer  = useSerializer(stu, many=True)
            user        = User.objects.filter(
                        username=request.user, groups__name='student').exists()

            if id is not None:
                stu         = userdata.objects.get(id=id)
                serializer  = useSerializer(stu)
                user        = User.objects.filter(
                            username=request.user, groups__name='student').exists()
            if user == True:
                return Response(serializer.data)
            return Response({'response': 'user should be student'})

        except Exception as e:
            print(e)


    def post(self, request):
        try:
            if User.objects.filter(
                username=request.user, groups__name='student').exists():
                return Response({'response': 'student can\'n be add Data '})

            stu         = request.data
            serializer  = useSerializer(data=stu)
            if serializer.is_valid():
                serializer.save()
                return Response({'response': 'Data Created'})

        except Exception as e:
            print(e)
       

class Adminuser(APIView):
    def post(self, request):
        try:
            username    = request.data.get('username')
            password    = request.data.get('password')
            type        = request.data.get('type')

            if type.lower()=='student':
                user=User(username=username)
                user.set_password(password)
                user.save()

                group=Group.objects.get(name='student')
                user.groups.add(group)
                token=RefreshToken()
                return Response({'id':user.id,'response':'Student user created by admin','token':str(token.access_token),})
        
        except Exception as e:
            print(e)

class registerApi(APIView):
    def post(self, request):
        try:
            username    = request.data.get('username')
            password    = request.data.get('password')
            type        = request.data.get('type')

            if type.lower() == 'student':
                user = User(username=username)
                user.set_password(password)
                user.save()

                group = Group.objects.get(name='student')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Student user added'})

            if type.lower() == 'teacher':
                user = User(username=username)
                user.set_password(password)
                user.save()

                group = Group.objects.get(name='teacher')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Teacher user added'})

            if type.lower() == 'admin':
                user = User(username=username)
                user.set_password(password)
                user.is_superuser   = True
                user.is_staff       = True
                user.save()

                group = Group.objects.get(name='admin')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Admin user added'})

            else:
                return Response({'response': 'Invalid user'})
                
        except Exception as e:
            print(e)