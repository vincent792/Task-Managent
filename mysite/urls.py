from django.contrib import admin
from django.urls import path,include
from account.views import home,login,register,logout


urlpatterns = [

    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
]
