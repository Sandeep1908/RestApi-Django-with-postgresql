# RestApi-Django-with-postgresql

This api build using django with jwt authentication.
Postgresql Database include

Please Configure your database in settings.py
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.<databse>',

        'NAME': '<database name>',

        'USER': '<username>',

        'PASSWORD': '<password>',

        'HOST': '<host>',

        'PORT': '<port no>',

    }

}

    HOW TO USE
    
    1.There is three types of user 
        a.Admin
        b.Teacher
        c.Student
    
    You have to register first with these data.
        {"username":"<your username>", "password":"<your password.", "type":"<type of user>"}
        
        for example:
        {"username":"demo","password":"demo","type":"student"}
        

    2. According to these urls to perform operations
    
        #This url helps to show all data
        path('',views.studentdata.as_view()),

        #This url helps to show data of one user    
        path('<int:id>/',views.studentdata.as_view(),name='id'),

        #This url is used to admin user only
        path('admin/',views.AdminuserApi.as_view(),name='admin'),

        #This url helps to create user 
        path('register/',views.registerApi.as_view(),name='register'),

        #This url help to recover password
        path('forgotapi/',views.ForgotApi.as_view(),name='forgot')
        
 
