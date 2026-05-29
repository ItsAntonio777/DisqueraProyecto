from django.db import models
from django.contrib.auth.models import User


# 👤 PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


# 🏷️ CATEGORY
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    color_hex = models.CharField(max_length=7, default="#FFB03A")

    def __str__(self):
        return self.title


# 🎤 ARTIST
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.stage_name


# 🎵 POST (ÁLBUM / PRODUCTO)
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )

    artist = models.ForeignKey(
        Artist,
        related_name='posts',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # 🔥 CAMBIO AQUÍ: Ahora es ManyToManyField y en plural
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        blank=True
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    intro = models.TextField()
    body = models.TextField()

    songs = models.TextField(blank=True, null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title


# 📌 SPECIFICATIONS
class Specification(models.Model):
    post = models.ForeignKey(Post, related_name='specs', on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}: {self.value}"


# 💬 COMMENTS
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.name}"


# 🛒 CART
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.post.price * self.quantity

    def __str__(self):
        return self.post.title


# 📦 ORDER
class Order(models.Model):
    PENDING = 'pending'
    PAID = 'paid'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (PENDING, 'Pendiente'),
        (PAID, 'Pagado'),
        (SHIPPED, 'Enviado'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id}"


# 📦 ORDER ITEMS
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity