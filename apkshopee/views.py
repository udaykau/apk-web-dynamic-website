from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, cart, Total_Cart, Contact, Billing_Address
from signup1.models import Registration
from django.contrib.auth.decorators import login_required
from requests.packages import urllib3
import requests
urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'


@login_required
def index(request):
    username = request.user.username
    temp = Product.objects.all()
    carts = cart.objects.filter(Merchant_Email=username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    if Total_Cart.objects.filter(Merchant_Email=username).exists():
        Total_cart = Total_Cart.objects.get(Merchant_Email=username)
    else:
        Total_cart = Total_Cart(Merchant_Email=username, Total_Item='0', Total_Price='0')
        Total_cart.save()
    return render(request, 'apkshopee/index.html', {'products': temp, 'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def product(request, sno, gender):
    temp = Product.objects.get(sno = sno, Gender = gender)
    size = temp.Size_Description.split(',')
    color = temp.Color_Description.split(',')
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/product.html', {'i': temp, 'size': size, 'color': color, 'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def shop(request, gender, category):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email=username)
    carts = cart.objects.filter(Merchant_Email=username)
    if Product.objects.filter(Gender=gender, Category__name__contains=category).exists():
        products = Product.objects.filter(Gender=gender, Category__name__contains=category)
        wallet = Registration.objects.get(email = username)
        wallet = wallet.Points
        return render(request, 'apkshopee/shop-grid-fullwidth.html', {'cart': Total_cart, 'carts': carts, 'products': products, 'wallet': wallet})
    else:
        return redirect('ComingSoon')


@login_required
def Shop(request, category):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email=username)
    carts = cart.objects.filter(Merchant_Email=username)
    if Product.objects.filter(Category__name__contains=category).exists():
        products = Product.objects.filter(Category__name__contains=category)
        wallet = Registration.objects.get(email = username)
        wallet = wallet.Points
        return render(request, 'apkshopee/shop-grid-fullwidth.html', {'cart': Total_cart, 'carts': carts, 'products': products, 'wallet': wallet})
    else:
        return redirect('ComingSoon')


@login_required
def Search(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email=username)
    carts = cart.objects.filter(Merchant_Email=username)
    if request.method == 'POST':
        name = request.POST['name']
        products = Product.objects.filter(Product_Name__icontains=name)
        wallet = Registration.objects.get(email=username)
        wallet = wallet.Points
        return render(request, 'apkshopee/shop-grid-fullwidth.html', {'cart': Total_cart, 'carts': carts, 'products':products, 'wallet': wallet})


@login_required
def privacy_Policy(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/privacy-policy.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def faq(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/faq.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def aboutUs(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/about-us.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def Error404(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/error-404.html', {'cart':Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def Order_Complete(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/order-complete.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def Order_Uncomplete(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/order-notcompleted.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def Cart(request):
    username = request.user.username
    if request.method == 'POST' or request.FILES:
        sno = request.POST['sno']
        name = request.POST['name']
        price = request.POST['price']
        Qty = request.POST['Qty']
        temp = Product.objects.get(sno=sno)
        image = temp.Image1
        temp = int(price.replace(',', ''))*int(Qty)
        sno = int(sno)
        s, *d = str(temp).partition(".")
        r = ",".join([s[x - 2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        total = "".join([r] + d)
        data = cart(Merchant_Email=username, Image=image, Product_Sno=sno, Total_Price=total, Product_Name=name, Price=price, Qty=Qty)
        data.save()
        if Total_Cart.objects.filter(Merchant_Email= username).exists():
            data = Total_Cart.objects.get(Merchant_Email=username)
            data.Total_Item = int(data.Total_Item) + 1
            temp1 = int(data.Total_Price.replace(',', '')) + temp
            s, *d = str(temp1).partition(".")
            r = ",".join([s[x - 2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
            data.Total_Price = "".join([r] + d)
            data.save()
        else:
            data = Total_Cart(Merchant_Email=username, Total_Item='1', Total_Price=total)
            data.save()
        messages.success(request, "Your Item is Successfully Added to Cart")
        return redirect('index')
    data = cart.objects.filter(Merchant_Email=username)
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/product-cart.html', {'Carts': data, 'cart': Total_cart, 'wallet': wallet})


@login_required
def contact(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = Contact(First_name=First_name, Last_name=Last_name, Email=email, Phone=phone, Message=message)
        data.save()
        messages.success(request, "Our Team Will Contact you Shortly")
        return redirect('index')
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/contact-us.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def Checkout(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email=username)
    carts = cart.objects.filter(Merchant_Email=username)
    data = Registration.objects.get(email=username)
    fname, lname = data.name.rsplit(' ', 1)
    wallet1 = Registration.objects.get(email=username)
    wallet = wallet1.Points
    if Total_cart.Total_Item == '0':
        messages.success(request, "No item on Cart to Proceed")
        return redirect('index')
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        if wallet > int(Total_cart.Total_Price.replace(',', '')):
            sno = ''
            products = ''
            price = ''
            total = int(0)
            for i in carts:
                sno += ';'+i.Product_Sno
                products += ';'+i.Product_Name
                price += ';'+ i.Total_Price
                temp = int(i.Total_Price.replace(',', ''))
                total = int(total) + temp
                i.delete()
            Total_cart.delete()
            sno = sno[1:]
            products = products[1:]
            price = price[1:]
            s, *d = str(total).partition(".")
            r = ",".join([s[x - 2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
            total = "".join([r] + d)
            data = Billing_Address(Merchant_mail = username, Phone=phone, Address=address, City=city, State=state,
                                Pincode=pincode, Prices=price, Product_Sno=sno, Product_Name=products, Total_Price=total)
            data.save()
            wallet = wallet- int(Total_cart.Total_Price.replace(',', ''))
            wallet1.Points = wallet
            wallet1.save()
            messages.success(request, "Your Order has been Placed Successfully")
            data = Total_Cart(Merchant_Email=username, Total_Item='0', Total_Price='0')
            data.save()
            return redirect('index')
        else:
            messages.success(request, "Insufficient Amount in Wallet")
            return redirect('index')
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/product-checkout.html', {'cart': Total_cart, 'carts': carts, 'data': data, 'fname':fname, 'lname':lname, 'wallet': wallet})


@login_required
def TermsandCondition(request):
    username = request.user.username
    if request.method == 'POST':
        sno = request.POST['sno']
        temp_cart = cart.objects.get(sno = sno)
        temp_total_cart = Total_Cart.objects.get(Merchant_Email = username)
        amount = temp_total_cart.Total_Price.replace(',', '')
        amount = int(amount) - int(temp_cart.Total_Price.replace(',', ''))
        temp_total_cart.Total_Item = int(temp_total_cart.Total_Item) - 1
        s, *d = str(amount).partition(".")
        r = ",".join([s[x - 2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        temp_total_cart.Total_Price = "".join([r] + d)
        temp_total_cart.save()
        temp_cart.delete()
        messages.success(request, "Your Item is Successfully Removed from Cart")
        return redirect('index')
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/terms-and-conditions.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})


@login_required
def ComingSoon(request):
    username = request.user.username
    Total_cart = Total_Cart.objects.get(Merchant_Email= username)
    carts = cart.objects.filter(Merchant_Email= username)
    wallet = Registration.objects.get(email = username)
    wallet = wallet.Points
    return render(request, 'apkshopee/coming-soon.html', {'cart': Total_cart, 'carts': carts, 'wallet': wallet})
