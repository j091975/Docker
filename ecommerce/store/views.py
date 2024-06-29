from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # handle form submission, e.g., save to database
    return render(request, 'store/index.html', {})  # Make sure 'index.html' is rendered with the context

def product_list(request):
    products = Product.objects.all()  # Fetch all records from the Product table
    return render(request, 'store/product_list.html', {'products': products})

def product_insert(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description', '')  # Default to an empty string if not provided
        stock = request.POST.get('stock', 0)  # Default to 0 if not provided

        # Create a new Product object and save it to the database
        new_product = Product(name=name, price=price, description=description, stock=stock)
        new_product.save()
        
        # Redirect to the same page after saving the new product
        return redirect('product_insert')
    
    # Fetch all products to display on the page
    products = Product.objects.all()
    return render(request, 'store/product_insert.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description', '')  # Default to an empty string if not provided
        stock = request.POST.get('stock', 0)  # Default to 0 if not provided

        # Create a new Product object and save it to the database
        new_product = Product(name=name, price=price, description=description, stock=stock)
        new_product.save()
        
        # Redirect to the index page after saving the new product
        return redirect('product_insert/')

    # If not a POST request, render the add product form (if needed separately)
    return render(request, 'store/index.html')  # Typically you wouldn't hit this for an add form in a single-page scenario