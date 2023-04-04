from django.shortcuts import render, redirect
from .models import SliderActive, Category, SubCategory
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
# Create your views here.


def index(request):
    usd = request.POST.get('USD')
    dram = request.POST.get('DRAM')
    rub = request.POST.get('RUB')
    if request.method == 'POST':
        new_price = request.POST.get('change_price')
        item_id = request.POST.get('id')
        try:
            new_price = int(new_price)
            item_id = int(item_id)
            x = SubCategory.objects.get(id=item_id)
            x.price = new_price
            x.save()
        except:
            return redirect('index')
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list
    })


def index_detail(request, id):
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
        'category_filter':category_filter
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")