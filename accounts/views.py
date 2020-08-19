from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from accounts.models import UserRegister, AddToCart
from homepage.models import Item
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
# Create your views here.
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'


def Register(request):
    if request.method == 'POST':

        user = UserRegister()


        user.user_name = request.POST['Candidate_Name']
        user.user_email = request.POST['Candidate_Emailid']
        user.user_gender = request.POST['Candidate_Gender']
        user.user_dob = request.POST['Candidate_DOB']
        user.user_phonenumber = request.POST['Candidate_Phonenumber']
        user.user_address = request.POST['Candidate_Adderss']
        user.user_city = request.POST['Candidate_City']
        user.user_state = request.POST['Candidate_State']
        user.user_password = request.POST['Candidate_Password']
        conform_password = request.POST['Candidate_Conformpassword']

        user.save()


        if user.user_password == conform_password:
            if User.objects.filter(username=user.user_name).exists():
                messages.info(request, "Username already exits")
                return redirect('Register')
            elif User.objects.filter(email=user.user_email).exists():
                messages.info(request, "Email already exits")
                return redirect('Register')
            else:
                user = User.objects.create_user(username = user.user_name, password = user.user_password, email= user.user_email)
                user.save()
                messages.info(request, "Registered successfully")
                return redirect('Login')
                
                
        else:
            print("User paswword unmatched")
            messages.info(request, "Password not matched")
            return redirect('Register')
        return redirect('index')
    else:
        return render(request, 'register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password = password)
         
        if user is not None : 
            auth.login(request, user)
            items = Item()
            items = Item.objects.all()
            
            return render(request, "index.html", {'items': items})

        else:
            messages.info(request, "invalid credentials")
            return redirect('Login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'logout.html')

def dropdown(request):
    text = "All functions of drop down menu will come into work as soon as possible"
    return render(request, 'dropdown.html', {'text':text})
    

def addtocart_view(request, userid):
    current_user = User.objects.get(pk = userid)
    #cart_all_items = AddToCart.objects.get(cart_useremail= current_user.email )
    if AddToCart.objects.filter(cart_useremail= current_user.email).exists():
       cart_all_items = AddToCart.objects.filter(cart_useremail= current_user.email )
       return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})
    
    else:
        
        text = "No Items in your cart !!!"
        return render(request, 'note.html', {'text': text})
        


def addtocart(request, userid, itemsid):
    if User.is_authenticated:
        current_user = User.objects.get(pk = userid)
        #print(current_user.email)
        #print(itemsid)
        cart_item = Item.objects.get(pk = itemsid)
        cart_add_item = AddToCart()
        cart_add_item.cart_useremail = current_user.email
        cart_add_item.cart_name = cart_item.item_name
        cart_add_item.cart_image = cart_item.item_image
        cart_add_item.cart_price = cart_item.item_price
        cart_add_item.cart_publisher = cart_item.item_publisher
        cart_add_item.cart_origin = cart_item.item_origin
        cart_add_item.cart_description = cart_item.item_description
        if AddToCart.objects.filter(cart_useremail= current_user.email).exists():
            print("1st if")
            fetch_all_cart_items = AddToCart.objects.filter(cart_useremail= current_user.email)
            if fetch_all_cart_items.filter(cart_name= cart_item.item_name).exists():
                print("2nd if")
                cart_add_item = fetch_all_cart_items.get(cart_name= cart_item.item_name)
                cart_add_item.cart_quantity += 1
                cart_add_item.save()

                #cart_add_item.cart_quantity += 1
                #cart_add_item.save()
            else:
                print("1st else part")
                cart_add_item.cart_quantity = 1
                cart_add_item.save()

        else:
            print("2nd else")
            cart_add_item.cart_quantity = 1
            cart_add_item.save()

        cart_add_item.cart_total_price = cart_add_item.cart_quantity * cart_add_item.cart_price
        cart_add_item.save()

       # cart_add_item.cart_total_price = cart_add_item.cart_quantity * cart_add_item.cart_price
        #cart_add_item.save()

            

        cart_all_items = AddToCart.objects.filter(cart_useremail = current_user.email).exclude(pk = cart_add_item.id)


        return render(request, 'addtocart.html', {'cart_add_item': cart_add_item, 'cart_all_items': cart_all_items})

def addtocart_inactiveuser(request):
    text = "Please login to add it in your cart"
    return render(request, 'note.html', {'text': text})

def deleteitem(request, itemid, userid):
    if AddToCart.objects.filter(pk= itemid).exists():
        login_user = User.objects.get(pk= userid)
        item = AddToCart.objects.get(pk=itemid ,cart_useremail= login_user.email)
        item.delete()
    
    else:
        text = "No Item exists in your cart. Please go to Homepage and add items in your cart."
        return render(request, 'note.html', {'text': text})
    cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
    return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

def increase_quantity(request, itemid, userid):
    if AddToCart.objects.filter(pk= itemid).exists():
        login_user = User.objects.get(pk= userid)
        item = AddToCart.objects.get(pk=itemid ,cart_useremail= login_user.email)
        item.cart_quantity += 1
        item.save()    
    item.cart_total_price = item.cart_quantity * item.cart_price
    item.save()
    cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
    return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

def decrease_quantity(request, itemid, userid):
    if AddToCart.objects.filter(pk= itemid).exists():
        login_user = User.objects.get(pk= userid)
        item = AddToCart.objects.get(pk= itemid, cart_useremail= login_user.email)
        if item.cart_quantity == 1:
            pass
        else:
            item.cart_quantity -= 1
            item.save()    
    item.cart_total_price = item.cart_quantity * item.cart_price
    item.save()
    cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
    return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

def profile(request, userid):
    if User.is_authenticated:
        text = "Your details"
        print(userid)
        print(type(userid))
        current_user = User.objects.get(pk = userid)
        print(type(current_user))
        profile_user = UserRegister.objects.get(user_name= current_user.username)
        print(type(profile_user))
    return render(request, 'profile.html', {'profile_user':profile_user, 'text':text})

def editprofile(request, userid):
    login_user = User.objects.get(pk= userid)
    current_user = UserRegister.objects.get(user_email=login_user.email)
    return render(request, 'editprofile.html', {'profile_user': current_user})

def update(request, userid):
    if User.is_authenticated:
        login_user = User.objects.get(pk= userid)
        user = UserRegister.objects.get(user_email=login_user.email)

        if request.method == "POST":

            user.user_name = request.POST['Candidate_Name']
            user.user_email = request.POST['Candidate_Emailid']
            user.user_gender = request.POST['Candidate_Gender']
            user.user_dob = request.POST['Candidate_DOB']
            user.user_phonenumber = request.POST['Candidate_Phonenumber']
            user.user_address = request.POST['Candidate_Address']
            user.user_city = request.POST['Candidate_City']
            user.user_state = request.POST['Candidate_State']    

            user.save()

    return redirect('index')

def buynow(request, itemid, userid):
    #Request paytm to add money from user account to your account
    login_user = User.objects.get(pk= userid)
    user = UserRegister.objects.get(user_email=login_user.email)

    orderitem = Item.objects.get(pk= itemid)
    if request.method=="POST":

        param_dict = {
                'MID': 'WorldP64425807474247',                  #'iSSLla27754627519933',    #'WorldP64425807474247',   #VMLsKh33374131769871
                'ORDER_ID': str(orderitem.id),
                'TXN_AMOUNT': '1',
                'CUST_ID': login_user.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'WEBSTAGING',
                'CHANNEL_ID':'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/accounts/handlerequest/',
            
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return HttpResponse("Something went wrong . Please try again")


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    print(checksum)
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    print(verify)


    if verify:
        print(response_dict['RESPCODE'])
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])

    return render(request, 'paymentstatus.html', {'response': response_dict})