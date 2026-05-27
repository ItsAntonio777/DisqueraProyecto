from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import (
    Post,
    CartItem,
    Profile,
    Order,
    OrderItem,
    Category
)

from .forms import (
    CommentForm,
    CheckoutForm,
    RegisterForm
)


# ✅ HOME
def home(request):

    posts = Post.objects.filter(
        status=Post.ACTIVE
    ).order_by('-created_at')

    categories = Category.objects.all()

    return render(request, 'disquera/home.html', {
        'posts': posts,
        'categories': categories
    })


# ✅ CATEGORÍAS
def category_detail(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug
    )

    posts = Post.objects.filter(
        category=category,
        status=Post.ACTIVE
    )

    return render(request, 'disquera/category_detail.html', {
        'category': category,
        'posts': posts
    })


# ✅ DETAIL
def detail(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    form = CommentForm()

    comments = post.comments.all().order_by('-created_at')

    return render(request, 'disquera/detail.html', {
        'post': post,
        'form': form,
        'comments': comments
    })


# ✅ CARRITO
@login_required
def cart(request):

    items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(
        item.subtotal()
        for item in items
    )

    return render(request, 'disquera/cart.html', {
        'items': items,
        'total': total
    })


# ✅ AGREGAR AL CARRITO
@login_required
def add_to_cart(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:

        item.quantity += 1
        item.save()

    return redirect('cart')


# ✅ REGISTRO
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.create(
                user=user
            )

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    return render(request, 'disquera/register.html', {
        'form': form
    })


# ✅ CHECKOUT
@login_required
def checkout(request):

    items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(
        item.subtotal()
        for item in items
    )

    if request.method == 'POST':

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.total = total
            order.status = Order.PAID

            order.save()

            for item in items:

                OrderItem.objects.create(
                    order=order,
                    post=item.post,
                    quantity=item.quantity,
                    price=item.post.price
                )

            items.delete()

            return redirect('success')

    else:

        form = CheckoutForm()

    return render(request, 'disquera/checkout.html', {
        'items': items,
        'total': total,
        'form': form
    })


# ✅ SUCCESS
def success(request):

    return render(
        request,
        'disquera/success.html'
    )


# ✅ PEDIDOS
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'disquera/my_orders.html', {
        'orders': orders
    })