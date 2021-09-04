from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import userdata
from .serializers import useSerializer
from rest_framework import status


# This view handels student and teacher user

class studentdata(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes      = [IsAuthenticated]

    #This method can use to see student data
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
            return Response(serializer.data)

        except Exception as e:
            print(e)

 # This method helps to creat data list
    def post(self, request):
        try:
            if User.objects.filter(
                username=request.user, groups__name='student').exists():
                return Response({'response': 'student can\'t be add data '},status=status.HTTP_401_UNAUTHORIZED)

            stu         = request.data
            serializer  = useSerializer(data=stu)
            if serializer.is_valid():
                serializer.save()
                return Response({'response': 'Data Created'},status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
       
# This Adminuser handels to create User list in database
class AdminuserApi(APIView):
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

            if type.lower()=='teacher':
                user=User(username=username)
                user.set_password(password)
                user.save()

                group=Group.objects.get(name='teacher')
                user.groups.add(group)
                token=RefreshToken()
                return Response({'id':user.id,'response':'Teacher user created by admin','token':str(token.access_token),})
        
        except Exception as e:
            print(e)


#This registerApi view help to user signup themselves to use this api
#There is three type of user allowed only 
# 1.Admin user
# 2.Teacher user
# 2.Student user
class registerApi(APIView):
    def post(self, request):
        try:
            username    = request.data.get('username')
            password    = request.data.get('password')
            type        = request.data.get('type')

            print(username)
            print(password)
            print(type)

            if type.lower() == 'student':
                user = User(username=username)
                user.set_password(password)
                user.save()

                group = Group.objects.get(name='student')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Student user added'},status=status.HTTP_201_CREATED)

            if type.lower() == 'teacher':
                user = User(username=username)
                user.set_password(password)
                user.save()

                group = Group.objects.get(name='teacher')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Teacher user added'},status=status.HTTP_201_CREATED)

            if type.lower() == 'admin':
                user = User(username=username)
                user.set_password(password)
                user.is_superuser   = True
                user.is_staff       = True
                user.save()

                group = Group.objects.get(name='admin')
                user.groups.add(group)
                refresh = RefreshToken()

                return Response({'token': str(refresh.access_token), 'response': 'Admin user added'},status=status.HTTP_201_CREATED)

            else:
                return Response({'response': 'Invalid user'},status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)

class ForgotApi(APIView):
    def post(self,request):
        try:
            username=request.data.get('username')
            password=request.data.get('password')

            if not User.objects.filter(username=username).exists():
                return Response({'response':'Username is not valid'})
            
            user=User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return Response({'response':'password changed'},status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)