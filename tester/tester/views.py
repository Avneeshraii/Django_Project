from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from mumbai.models import AddClient
from django.shortcuts import redirect,render

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

# <  Login > <  Login > <  Login > <  Login > <  Login > <  Login >

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render (request,'Login.html')

# <  Signup  > <  Signup  > <  Signup  > <  Signup  > <  Signup  > 

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

#  < HomePage > < HomePage > < HomePage > < HomePage > < HomePage >
def homepage(request):
    serviceData=Service.objects.all().order_py('service_title')
    data={
        'srviceData':serviceData
    }
    
    return render(request,"File.html")



# <Client> <Client> <Client> <Client> <Client> <Client> <Client><Client>


# < Add Client > # < Add Client > # < Add Client > # < Add Client > # < Add Client >

def Home(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

# < add clients> < add clients> < add clients> < add clients> < add clients> < add clients> 

def Client(request):
    emp = AddClient.objects.all()
    
    context ={
        'emp':emp,
    }
    
    return render(request,'Client.html',context)

def Sale(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = AddClient(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('client')
    
        return render(request,'Client.html')
    
 # < FOR EDIT AND UPDATE > < FOR EDIT AND UPDATE > < FOR EDIT AND UPDATE > < FOR EDIT AND UPDATE > < FOR EDIT AND UPDATE >   
    
def Edit(request):
        emp = AddClient.objects.all()
        
        context = {
            'emp' : emp,
        }
        return redirect(request,'Client.html',context)
    
    
def Update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = AddClient(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('client')
    return redirect(request,'Client.html')


# < for delete > < for delete >  < for delete > < for delete > < for delete > < for delete >

def Delete(request,id):
    emp = AddClient.objects.filter(id = id)
    emp.delete()
    
    context = {
        'emp':emp
    }
    
    return redirect('client')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def User(request):  
    return render (request,'User.html')




