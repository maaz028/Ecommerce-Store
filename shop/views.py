
from typing import Counter
from django.shortcuts import render
from math import ceil
from shop.models import Product, contact, order, update_order

def index(request):
    allprods = []
    Counter = 0
    catprods = Product.objects.values('category','id')
    categ = {item['category'] for item in catprods}
    for cat in categ:
        Counter += 1
        products = Product.objects.filter(category=cat)
        slides = ceil((len(products)/3)) 
        lengthp = len(products)
        allprods.append([products, range(1,slides),slides, Counter, lengthp])     
    params = {'allprods':allprods}
    return render(request,'shop/index.html', params)


def contact_us(request):
    if request.method == 'POST':
        namee = request.POST.get('name', '')
        emaill = request.POST.get('email', '')
        phonee = request.POST.get('phone', '')
        queryy = request.POST.get('text', '')    
        contacts = contact(name = namee, email= emaill,phone = phonee, query_txt = queryy )
        contacts.save() 
    return render(request, 'shop/contact_us.html')

def fetch_data(request):
    data = Product.objects.all()
    return render(request,'shop/data.html', {'data':data})

def products(request, pid):
    prod = Product.objects.filter(id = pid)
    params = {'products':prod}
    return render(request, 'shop/products.html',params)

def checkout (request):
    return render(request,  'shop/checkout.html')

def order_func(request): 
    if request.method == 'POST':
        items = request.POST.get('items','')
        price = request.POST.get('total_price','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')  
        
        if name != '' and email != '':
            
            order_details = order(items = items,total_price=price, name = name, email = email, address = address, city = city, state = state, zip = zip)
            order_details.save()
            id= order_details.order_id
            update_details = update_order(order_id= id, update_desc = "Order has been placed")
            update_details.save()
            
            thank = True
            return render(request, 'shop/checkout.html', {'id':id,'thank':thank})
        else:
            empty = True
            return render(request, 'shop/checkout.html', {'empty':empty})
    


def tracker(request):
    
    
    try:
        if request.method == 'POST':
            order_id = request.POST.get('orderid','')
            email = request.POST.get('email','')
            order_id = int(order_id)
            
            print(order_id,' ',email)
            order_ID = order.objects.filter(order_id=order_id, email=email)
            if len(order_ID) > 0:
                print('entered')
                update_id = update_order.objects.filter(order_id = order_id)
                params = {'update':update_id,'order_details':order_ID}
            
                return render(request, 'shop/tracker.html', params)
            
            else:
                order_not_found = True
                return render(request, 'shop/tracker.html', {'order_not_found':order_not_found, 'id':order_id})
    except Exception as e:
        missing_data = True
        return render(request, 'shop/tracker.html', {'missing_data':missing_data})
    else:
        return render(request, 'shop/tracker.html')


    
def search_results(request):
    query = request.GET.get('search','')
    if query!='':
        allprods = []
        Counter = 0
        catprods = Product.objects.values('category','id')
        categ = {item['category'] for item in catprods}
        for cat in categ:       
            productstemp = Product.objects.filter(category=cat)
            products = []
            for item in productstemp:
                if search(query,item):
                    print(item.prodcut_name, ' ', item.prodcut_description)
                    products.append(item) 
            if len(products)>0:
                slides = ceil((len(products)/3)) 
                lengthp = len(products)
                allprods.append([products, range(1,slides),slides, Counter, lengthp])   
        params = {'allprods':allprods}
        return render(request,'shop/index.html', params)
    else:
        allprods = []
        Counter = 0
        catprods = Product.objects.values('category','id')
        categ = {item['category'] for item in catprods}
        for cat in categ:
            Counter += 1
            products = Product.objects.filter(category=cat)
            slides = ceil((len(products)/3)) 
            lengthp = len(products)
            allprods.append([products, range(1,slides),slides, Counter, lengthp])     
        params = {'allprods':allprods}
        return render(request,'shop/index.html', params)

def search(query,item):
    if query in item.prodcut_name.lower() or query in item.prodcut_description.lower() or query in item.category.lower():
        return True
    elif query == '':
        return True
    
    
def store(request):
    return render(request,'shop/store.html') 