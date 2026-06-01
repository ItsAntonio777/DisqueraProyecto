from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from .models import (
    Post,
    CartItem,
    Profile,
    Order,
    OrderItem,
    Category,
    CartItem,
    
)

from .forms import (
    CommentForm,
    CheckoutForm,
    RegisterForm
)
@login_required
def eliminar_del_carrito(request, post_id):

    item = get_object_or_404(
        CartItem,
        user=request.user,
        post_id=post_id
    )

    item.delete()

    return redirect('cart')

# HOME
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'disquera/home.html', {
        'posts': posts,
        'categories': categories
    })

# CATEGORY
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    # REEMPLAZADO: 'category=category' por 'categories=category'
    posts = Post.objects.filter(categories=category, status=Post.ACTIVE)

    return render(request, 'disquera/category_detail.html', {
        'category': category,
        'posts': posts
    })


# DETAIL
def detail(request, id):
    post = get_object_or_404(Post, id=id)

    form = CommentForm()
    comments = post.comments.all().order_by('-created_at')

    return render(request, 'disquera/detail.html', {
        'post': post,
        'form': form,
        'comments': comments
    })

@login_required
def update_cart_quantity(request, id, action):

    item = get_object_or_404(CartItem, id=id, user=request.user)

    if action == 'add':
        item.quantity += 1

    elif action == 'remove':
        item.quantity -= 1

        if item.quantity <= 0:
            item.delete()
            return redirect('cart')

    item.save()

    return redirect('cart')


# CART
@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)

    total = sum(item.subtotal() for item in items)

    return render(request, 'disquera/cart.html', {
        'items': items,
        'total': total
    })


# ADD TO CART
@login_required
def add_to_cart(request, id):
    post = get_object_or_404(Post, id=id)

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')


# REGISTER
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'disquera/register.html', {'form': form})

@login_required
def checkout(request):

    items = CartItem.objects.filter(user=request.user)

    total = sum(item.subtotal() for item in items)

    if request.method == 'POST':

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.user = request.user
            order.total = total
            order.status = Order.PAID
            order.save()

            # 🔥 AQUÍ SE DESCUENTA STOCK Y SE CREA ORDEN
            for item in items:

                post = item.post

                # 🚨 validar stock
                if post.stock < item.quantity:
                    return redirect('cart')

                post.stock -= item.quantity
                post.save()

                OrderItem.objects.create(
                    order=order,
                    post=post,
                    quantity=item.quantity,
                    price=post.price
                )

            # limpiar carrito
            items.delete()

            return redirect('success')

    else:
        form = CheckoutForm()

    return render(request, 'disquera/checkout.html', {
        'form': form,
        'items': items,
        'total': total
    })

# SUCCESS
def success(request):
    return render(request, 'disquera/success.html')


# ORDERS
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'disquera/my_orders.html', {
        'orders': orders
    })


# PROFILE
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'disquera/profile.html', {
        'profile': profile
    })


# SEARCH (ARREGLADO)
def search(request):

    query = request.GET.get('q')
    search_type = request.GET.get('type')

    if search_type == 'artist':

        results = Post.objects.filter(
            artist__stage_name__icontains=query
        )

    else:

        results = Post.objects.filter(
            title__icontains=query
        )

    return render(request, 'disquera/search.html', {
        'results': results,
        'query': query,
        'search_type': search_type
    })