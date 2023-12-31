# main_app/views.py
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Meal, Photo, Reservation, AboutUs, Why_Choose_Us, Chef, Category, Wine
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .form_reservation import ReserveTableForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .form_contact import ContactForm
from .form_meal import MealForm
from .form_signup import SignupForm
from datetime import date

from django.shortcuts import get_object_or_404
import uuid  # this is to make random numbers
import boto3  # this is to make calls to aws
import os  # os.environ['BUCKET_NAME'] is to read environment variables


def add_photo(request, meal_id):
    # in the html <input type='file' name='photo-file'/>
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        # initialize our boto3 client
        s3 = boto3.client('s3')
        # key This is the unique key, or the location on aws s3 bucket where we store the file
        key = 'project-6-5/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # [photo_file.name.rfind('.'):] grabs the file extension .jpeg, .gif, .png
        try:
            # accessing an environment variable
            bucket = os.environ['BUCKET_NAME']
            s3.upload_fileobj(photo_file, bucket, key)

            # build our url to save tin the database, this is the link to the image on aws s3
            url = F"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # Save the Url to the photo model and add the fk for the cat
            Photo.objects.create(url=url, meal_id=meal_id)
        except Exception as e:
            print(
                'An error occurred uploading to s3, probably wrong url, bucket name or keys code ~/.aws/credentials is '
                'where your keys are')
            print(e)

    return redirect('detail', meal_id=meal_id)


def home(request):
    meals = Meal.objects.all()
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()

    context = {
        'meals': meals,
        'meal_list': meal_list,
        'categories': categories,
        'why_choose_us': why_choose_us,
    }

    return render(request, 'home.html', context)


def about(request):
    context = {
        "app_description": "Welcome to the Nota Nobile",
    }
    return render(request, "about.html", context)


def aboutus_list(request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.all()
    context = {
        'about': about,
        'why_choose_us': why_choose_us,
        'chef': chef,
    }
    return render(request, 'about.html', context)


@login_required
def meals_index(request):
    meals = Meal.objects.all()

    return render(request, 'meals/index.html', {'meals': meals})


@login_required
def meals_detail(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    id_list = meal.wines.all().values_list('id')
    wines_meal_doesnt_have = Wine.objects.exclude(id__in=id_list)
    return render(request, 'meals/detail.html',
                  {'meal': meal,
                   'wines': wines_meal_doesnt_have}
                  )


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm

    def get_success_url(self):
        return reverse('detail', kwargs={'meal_id': self.object.pk})

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image_file')
        # initialize our boto3 client
        s3 = boto3.client('s3')
        # key This is the unique key, or the location on aws s3 bucket where we store the file
        key = 'project-6-5/' + uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]
        # [photo_file.name.rfind('.'):] grabs the file extension .jpeg, .gif, .png
        # accessing an environment variable
        bucket = os.environ['BUCKET_NAME']
        # upload to s3
        result = s3.upload_fileobj(image_file, bucket, key)
        del request.FILES['image_file']
        # build our url to save tin the database, this is the link to the image on aws s3
        url = F"{os.environ['S3_BASE_URL']}{bucket}/{key}"
        # Save the Url to the photo model and add the fk for the cat
        data = request.POST.copy()
        data['image'] = url
        request.POST = data
        form = self.get_form()
        if form.is_valid():
            form.instance.image = url
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'price', 'preparation_time', 'ingredients']


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = '/meals'


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}

    return render(request, 'reservation/reservation.html', context)


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['group3@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('send_success')

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)


def send_success(request):
    return render(request, 'contact/success.html', {})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = SignupForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    else:
        form = SignupForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ReservationsList(ListView):
    model = Reservation

    def get_queryset(self):
        # Get the original queryset
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(user=self.request.user)


class ReservationsDetail(DetailView):
    model = Reservation


class ReservationsCreate(CreateView):
    model = Reservation
    form_class = ReserveTableForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        form.instance.name = f'{self.request.user.first_name} {self.request.user.last_name}'

        # Call the parent class's form_valid to handle the model save and other operations
        response = super().form_valid(form)

        # After saving the reservation, send an email
        subject = 'Your Reservation Confirmation'
        message = f'Dear {self.request.user.first_name},\n\nYour reservation for {form.instance.Date} at {form.instance.time} has been confirmed.\n\nThank you for choosing us!'
        from_email = 'noreply@yourdomain.com'
        recipient_list = [self.request.user.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            print("Error sending email. Invalid header detected.")

        return response

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.email = self.request.user.email
    #     # form.instance.first_name = form.request.user.first_name
    #     # form.instance.last_name = self.request.user.last_name
    #     form.instance.name = self.request.user

    #     return super().form_valid(form)


class ReservationsUpdate(UpdateView):
    model = Reservation
    # add here what fields to update
    fields = ['Date', 'time', 'name']


class ReservationsDelete(DeleteView):
    model = Reservation
    success_url = '/reservations'


def pair_wine(request, meal_id, wine_id):
    meal = Meal.objects.get(id=meal_id)
    meal.wines.add(wine_id)
    return redirect('detail', meal_id=meal_id)


def unpair_wine(request, meal_id, wine_id):
    meal = Meal.objects.get(id=meal_id)
    meal.wines.remove(wine_id)
    return redirect('detail', meal_id=meal_id)


class WineList(ListView):
    # wine = Wine
    def get_queryset(self):
        return Wine.objects.all()


class WineDetail(DetailView):
    model = Wine


class WineCreate(CreateView):
    model = Wine
    fields = '__all__'


class WineUpdate(UpdateView):
    model = Wine
    fields = ['name', 'price']


class WineDelete(DeleteView):
    model = Wine
    success_url = '/wines'
