from django.shortcuts import render, redirect
from .models import my
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User, auth

def search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=my.objects.filter(Q(First_Name__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'No Record Found')
        else:
            return HttpResponseRedirect('search')
    return render(request,'search.html')

def details(request):
	return render(request,'pt_dtls.html')

def login(request):
	if request.method=='POST':
		username = request.POST['user']
		password = request.POST['pass']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("/home")

		else:
			messages.info(request,'Invalid Username and Password')
			return redirect("/")
	else:
		return render(request,'index.html')

def fetch(request):
	all_pt = my.objects.all()
	return render(request, "patient.html", {'Patients':all_pt})

def form(request):
	if request.method=='POST':
		dict1=request.POST
		a = []
		for k,v in dict1.items():
			a.append(v)
		
		to_save = my(First_Name = a[1],
		Last_Name = a[2],
		Father_Name = a[3],
		DOB = a[4],
		Gender = a[5],
		Height = a[6],
		Weight = a[7],
		Marital_Status = a[8],
		Email_Id = a[9],
		Mob_No = a[10],
		Address = a[11],
		City = a[12],
		Pin_Code = a[13],
		State = a[14],
		Country = a[15])
		to_save.save()
		print("Data has been saved")
		return redirect("/apt")
	else:
		return render(request,"vip.html")	

def logout(request):
	auth.logout(request)
	return redirect('/')

def about(request):
	return render(request,'about.html')