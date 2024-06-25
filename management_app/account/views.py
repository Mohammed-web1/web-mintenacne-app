from django.shortcuts import render,redirect

from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = SignUpForm()
    form.order_fields(field_order=['name','last_name','role','username','email','password1','password2'])
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()

            print(user)
            #auth_login(request,user)
            new_user = User.objects.create(
                user = user,
                name=form.cleaned_data.get('name'),
                role=form.cleaned_data.get('role'),
            )
            messages.success(request, 'The user has been created successfully.')
            return redirect('admin')

    return render(request,'interface_admin/admin.html',{'form':form})

@login_required
def gestintervention(request):
    return render(request,'interface_admin/gestintervention.html')


@login_required
def gestutilisateur(request):
    return render(request,'interface_admin/gestutilisateur.html')

@login_required
def paramsys(request):
    return render(request,'interface_admin/paramsys.html')

@login_required
def rapp_stat(request):
    return render(request,'interface_admin/rapp_stat.html')



@login_required
def signalementproblem(request):
    return render(request,'interface_employee/signalementproblem.html')

@login_required
def suividemande(request):
    return render(request,'interface_employee/suividemande.html')



@login_required
def consuletintervention(request):
    return render(request,'interface_technicien/consuletintervention.html')


@login_required
def mizajour(request):
    return render(request,'interface_technicien/mizajour.html')

@login_required
def rapportintervention(request):
    return render(request,'interface_technicien/rapportintervention.html')



@login_required
def interface_technicien(request):
    role = User.objects.filter(user=request.user)
    role = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'interface_technicien':
        return render(request,'interface_technicien/technicien.html',{'x':role})
    else:
        return render(request,'404.html')


@login_required
def interface_employee(request):
    username = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'interface_employee':
        return render(request,'interface_employee/employe.html',{'username':username})
    else:
        return render(request,'404.html')

@login_required
def interface_admin(request):
    username = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'interface_admin':
        return render(request,'interface_admin/admin.html',{'username':username})
    else:
        return render(request,'404.html')



class MyLoginView(LoginView):

    def get_success_url(self):
        role = User.objects.filter(user=self.request.user).values('role')
        if role[0]['role'] == 'interface_technicien':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_TECH)
     
        elif role[0]['role'] == 'interface_employee':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_EMP)
        elif role[0]['role'] == 'interface_admin':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_ADMIN)


# def login(request):

#     form = AuthenticationForm()
#     if request.method =='POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             print(form)
#             user = form.save()
#             print(user)
#             auth_login(request,user)

#             return redirect('login')

#     """
#     if ....
#         redirect to ...
    
    
#     """
    

#     return render(request,'index/index.html',{'form':form})