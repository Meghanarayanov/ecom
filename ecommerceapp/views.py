from django.shortcuts import render,redirect
from ecommerceapp.models import Category
from ecommerceapp.models import Product
from ecommerceapp.models import Userdetails
from ecommerceapp.models import Cart
from django.contrib.auth.models import User,auth
#from django.contrib.auth.decorators import login_required #method 3
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def index(request):
    category=Category.objects.all()
    return render(request,'index.html',{'categorie':category})
    
def userindex(request):
    category=Category.objects.all()
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        countt = 0
   
    return render(request,'userindex.html',{'categorie':category,'coun': countt})
    
def loginpage(request):
    return render (request,'loginpage.html')
def signuppage(request):
    return render (request,'signuppage.html')
def adminpage(request):
    return render (request,'adminpage.html')
def logout(request):
    return render (request,'index.html')
def addcategory(request):
    return render (request,'addcategory.html')
def addproduct(request):
    category=Category.objects.all()
    return render(request,'addproduct.html',{'category':category})

    



def loginform(request):
     if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             #request.session["uid"]=user.id
            if user.is_staff:
                 login(request,user)
                 return redirect('adminpage')
            else:
                auth.login(request,user)
               
                return redirect('userindex')

        else:
            messages.info(request,"Invalid username or password! Try Again")
            return redirect('loginpage')
     else:
           return redirect('loginpage')


def signupform(request):
    if request.method == 'POST':
        u_firstname = request.POST['fname']
        u_lastname = request.POST['lname']
        u_username = request.POST['username']
        u_email = request.POST['email']
        u_password = request.POST['password']
        u_cpassword = request.POST['cpassword']
        u_address = request.POST['address']
        u_contact = request.POST['contact']
        u_image = request.FILES.get('image')

        if u_password == u_cpassword:
            if User.objects.filter(username=u_username).exists():
                messages.info(request, 'This username already exists!')
                return redirect('signuppage')
            else:
                user = User.objects.create_user(
                    first_name=u_firstname,
                    last_name=u_lastname,
                    username=u_username,
                    email=u_email,
                    password=u_password
                )

                user_details = Userdetails(
                    user=user,
                    user_address=u_address,
                    user_number=u_contact,
                    user_image=u_image
                )
                user_details.save()

                # You may consider logging in the user after creating the account
                # Example: login(request, user)

                # Redirect to the appropriate page after successful registration
                return redirect('loginpage')
        else:
            messages.info(request, "Passwords don't match!")
            return redirect('signuppage')

    return render(request, 'signuppage.html')


def addcategory_db(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
       
       
        c=Category(category_name=categoryname)
        c.save()
        return redirect('addcategory')
def addproduct_db(request):
     if request.method=='POST':
        p_name=request.POST['name']
        p_description=request.POST['description']
        p_price=request.POST['price']
        p_image = request.FILES.get('image')
        category1=request.POST['category']
        p_category=Category.objects.get(id=category1)
       
        p=Product(product_name=p_name,product_description=p_description,product_price=p_price,product_image=p_image,category=p_category)
        p.save()
        return redirect('addproduct')
     
def viewproduct(request):
    product=Product.objects.all()
    return render(request,'viewproduct.html',{'product':product})
def deleteproduct(request,pk):
    prd=Product.objects.get(id=pk)
    prd.delete()
    return redirect('viewproduct')
def viewuser(request):
      user=Userdetails.objects.all()
      return render(request,'viewuser.html',{'user':user})
def deleteuser(request,pk):
    user=Userdetails.objects.get(user=pk)
    user.delete()
    user1=User.objects.get(id=pk)
    user1.delete()
    return redirect('viewuser')
from django.shortcuts import redirect

def category_page(request, category_name):
   
    if category_name == 'men':
        return redirect('mencategory')
    elif category_name == 'women':
        return redirect('womencategory')
    elif category_name == 'boy':
        return redirect('boycategory')
    elif category_name == 'girl':
        return redirect('girlcategory')
    else:
       
        return redirect('index') 
    
def mencategory(request):
    category=Category.objects.all()
    men_category = Category.objects.get(category_name="Men")
    
    
    men_products = Product.objects.filter(category=men_category)
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        countt = 0
    
    return render(request, 'men.html', {'products': men_products,'categorie':category,'coun':countt})
    
def womencategory(request):
    category=Category.objects.all()
    women_category = Category.objects.get(category_name="women")
    
   
    women_products = Product.objects.filter(category=women_category)
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        countt = 0
    
    return render(request, 'women.html', {'products': women_products,'categorie':category,'coun':countt})
    
def boycategory(request):
    category=Category.objects.all()
    boy_category = Category.objects.get(category_name="boy")
    
   
    boy_products = Product.objects.filter(category=boy_category)
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        count = 0
    
    return render(request, 'boy.html', {'products': boy_products,'categorie':category,'coun':countt})
    
def girlcategory(request):
    category=Category.objects.all()
    girl_category = Category.objects.get(category_name="girl")
    
   
    girl_products = Product.objects.filter(category=girl_category)
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        countt= 0
    
    return render(request, 'girl.html', {'products': girl_products,'categorie':category,'coun':countt})
def addtocart(request,pk):
   pr=Product.objects.get(id=pk)
   cart_item, created=Cart.objects.get_or_create(user=request.user,product=pr)
   if not created:
       cart_item.quantity+=1
       cart_item.save()
   return redirect('cart')
def cart(request):
    category=Category.objects.all()
    cart_items=Cart.objects.filter(user=request.user).select_related('product')
    total_price=sum(item.total_price() for item in cart_items)
    if request.user.is_authenticated:
        countt = Cart.objects.filter(user=request.user).count()
    else:
        countt = 0
    
    return render(request,'cart.html',{'caite':cart_items,'totalprice':total_price,'coun':countt,'categorie':category})
def decrease(request,pk):
    cart_item=Cart.objects.get(product_id=pk,user=request.user)
    cart_item.quantity -=1
    cart_item.save()
    return redirect('cart')
def increase(request,pk):
    cart_item=Cart.objects.get(product_id=pk,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('cart')
def remove(request,pk):
    cart_item=Cart.objects.filter(product_id=pk,user=request.user).first()
    if cart_item:
      cart_item.delete()
    return redirect('cart')

def checkout(request):

   category=Category.objects.all()
   if request.method == 'POST':
       
        messages.info(request, "Your order is placed successfully. Thank you for ordering with us")
        return redirect('checkout')
    
   return render(request, 'checkout.html',{'categorie':category})
