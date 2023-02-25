from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from account.models import UserDetail

# Create your views here.


def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        # Get user details from form data
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            print('incorect')
            messages.info(request, 'Incorect password please.....')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            print('Username exists')
            messages.info(request, 'Username exists.....')
            return redirect('register')
            
        else:
        
            user=User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            # Create new user detail object
        
            user_detail = UserDetail(user=user, email=email, username=username)
            user_detail.save()
            messages.info(request, 'User  Created.....')            
            print('user created')
            return redirect('login')
    else:

        template_name='register.html'
        return render(request , template_name)

def login(request):    
    if request.method =='POST':
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        k=UserDetail.objects.get(username=uname)
        c=k.staff
        print(c)
        if c == False:
            messages.info(request, "Prohibited!! Contact Admin to be given role to Login and use the task manager app .")
            
            return redirect('login')
        else:
        
            user= auth.authenticate(username=uname, password=pass1)
            
            if User.objects.filter(username=uname).exists():           
            
                if user is not None:
                    auth.login(request, user)
                    print('login success')
                    messages.info(request, 'Login  Success.....')
                    return redirect('/')
                else:
                    print('invalid details')
                    messages.info(request, 'Invalid Password.....')
                    return redirect('login')
            else:            
                print('Invalid username')
                messages.info(request, 'Invalid username.....')
                return redirect('login') 
        
    template_name='login.html'
    return render(request , template_name)





# def logout(request):
#     auth.logout(request)
#     messages.info(request, "you're logged out")
    
#     print("you're logged out")
#     return redirect('login')

def logout(request):
    auth.logout(request)
    messages.info(request, "You're logged out.")
    return redirect('login')