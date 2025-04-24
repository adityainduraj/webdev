# How to Recreate the Employee Portal Django App

To recreate this Django application from scratch, follow these step-by-step instructions:

## Step 1: Set Up a Django Project

1. Make sure you have Django installed:
   ```bash
   pip install django
   ```

2. Create a new Django project:
   ```bash
   django-admin startproject employee_portal
   ```

3. Navigate to the project directory:
   ```bash
   cd employee_portal
   ```

## Step 2: Create the Employees App

1. Create a new Django app:
   ```bash
   python manage.py startapp employees
   ```

2. Add the 'employees' app to the project's installed apps in `employee_portal/settings.py`:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'employees',  # Add this line
   ]
   ```

## Step 3: Configure URLs

1. Create the main project URL configuration in `employee_portal/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('employees.urls')),
   ]
   ```

2. Create a new file `employees/urls.py` with this content:
   ```python
   from django.urls import path
   from .views import promotion_view

   urlpatterns = [
       path('', promotion_view, name='promotion_check'),
   ]
   ```

## Step 4: Create the Form

1. Create a new file `employees/forms.py` with this content:
   ```python
   from django import forms
   import datetime

   EMPLOYEE_IDS = [
       ('EMP001', 'EMP001'),
       ('EMP002', 'EMP002'),
       ('EMP003', 'EMP003'),
       ('EMP004', 'EMP004'),
   ]

   class PromotionCheckForm(forms.Form):
       employee_id = forms.ChoiceField(choices=EMPLOYEE_IDS)
       date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
   ```

## Step 5: Create the View

1. Edit `employees/views.py` with this content:
   ```python
   from django.shortcuts import render
   from .forms import PromotionCheckForm
   from datetime import date

   def promotion_view(request):
       form = PromotionCheckForm()
       result = None

       if request.method == 'POST':
           form = PromotionCheckForm(request.POST)
           if form.is_valid():
               doj = form.cleaned_data['date_of_joining']
               today = date.today()
               experience_years = (today - doj).days / 365.25  # approx. year calculation
               result = "YES" if experience_years > 5 else "NO"

       return render(request, 'employees/promotion_form.html', {
           'form': form,
           'result': result,
       })
   ```

## Step 6: Create the Template

1. Create a directory structure for templates:
   ```bash
   mkdir -p employees/templates/employees
   ```

2. Create the template file `employees/templates/employees/promotion_form.html`:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Promotion Eligibility</title>
   </head>
   <body>
       <h2>Check Promotion Eligibility</h2>
       <form method="post">
           {% csrf_token %}
           {{ form.as_p }}
           <button type="submit">Am I Eligible for Promotion</button>
       </form>

       {% if result %}
           <h3>Eligibility Result: <label>{{ result }}</label></h3>
       {% endif %}
   </body>
   </html>
   ```

## Step 7: Run Migrations and Start the Server

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Visit http://127.0.0.1:8000/ in your browser to see the promotion eligibility checker.

## Functionality Overview

This Django application provides a simple promotion eligibility checker where:

1. Users select an employee ID from a dropdown list
2. Users provide a date of joining via a date picker
3. When the form is submitted, the system calculates if the employee has more than 5 years of experience
4. The result (YES or NO) is displayed on the page indicating promotion eligibility

The key business logic is in the views.py file where it calculates the years of experience by finding the difference between today's date and the date of joining.
