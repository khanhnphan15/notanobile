from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'about us '
        verbose_name_plural = 'about us '

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'why choose us '
        verbose_name_plural = 'why choose us '

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chef'

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50, verbose_name='meal')
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # //This is a common practice to store URL-friendly versions of strings in the database

    class Meta:
        verbose_name_plural = 'meals'

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meal_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    # A meal has many photos, a photo belongs to a meal
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for meal_id: {self.meal_id} @{self.url}"


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
