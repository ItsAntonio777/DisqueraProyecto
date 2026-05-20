from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):


    title = models.CharField(max_length=255)


    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )


    color_hex = models.CharField(
        max_length=7,
        default="#FFA51F"
    )


    def __str__(self):
        return self.title




class Artist(models.Model):


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    stage_name = models.CharField(max_length=255)


    bio = models.TextField()


    def __str__(self):
        return self.stage_name




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


    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )


    title = models.CharField(max_length=255)


    slug = models.SlugField(max_length=255)


    intro = models.TextField()


    body = models.TextField()


    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )


    stock = models.PositiveIntegerField(default=1)


    created_at = models.DateTimeField(auto_now_add=True)


    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS,
        default=ACTIVE
    )


    image = models.ImageField(
        upload_to='upload/',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/album/{self.id}/'




class Specification(models.Model):


    post = models.ForeignKey(
        Post,
        related_name='specs',
        on_delete=models.CASCADE
    )


    label = models.CharField(max_length=50)


    value = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.label}: {self.value}"




class Comment(models.Model):


    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )


    name = models.CharField(max_length=255)


    email = models.EmailField()


    body = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comentario de {self.name} en {self.post.title}"




class CartItem(models.Model):


    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )


    quantity = models.PositiveIntegerField(default=1)


    created_at = models.DateTimeField(auto_now_add=True)


    def subtotal(self):
        return self.post.price * self.quantity


    def __str__(self):
        return self.post.title
