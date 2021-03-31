from django.db import models
from user.models import User
from django.conf import settings
from pytz import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    main_category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    third_category = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural ="category"


class Products(models.Model):
    
    COLOR_CHOICES = (
        ('White', 'white'),
        ('Black', 'black'),
        ('Red', 'red'),
        ('Blue', 'blue'),
        ('Green', 'green'),
        ('Yellow', 'yellow'),
        ('Purple', 'purple'),
        ('Pink', 'pink'),
    )

    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE, db_column="category_id")
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="product_image")
    price = models.CharField(max_length=50)
    # option = models.CharField()
    # sub_option = models.CharField()
    likes = models.IntegerField(default=0)
    info = models.TextField()
    detail = models.FileField(upload_to="product_detail")
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    brand = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    discount_rate = models.IntegerField(default=0)

    class Meta:
        verbose_name = "products"
        verbose_name_plural ="products"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id")
    product_id = models.ForeignKey(Products, related_name="products", on_delete=models.CASCADE, db_column="product_id")
    rating = models.IntegerField(default=5)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)

    class Meta:
        verbose_name = "review"
        verbose_name_plural ="review"