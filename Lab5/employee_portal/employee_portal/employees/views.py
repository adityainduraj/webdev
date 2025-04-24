# employees/views.py
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
