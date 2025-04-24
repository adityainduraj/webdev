# students/views.py
from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    form = StudentForm()
    student_data = ''
    percentage = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            total = cleaned_data['english'] + cleaned_data['physics'] + cleaned_data['chemistry']
            percentage = total / 3

            student_data = f"""
Name: {cleaned_data['name']}
DOB: {cleaned_data['dob']}
Address: {cleaned_data['address']}
Contact: {cleaned_data['contact_number']}
Email: {cleaned_data['email']}
Marks - English: {cleaned_data['english']}, Physics: {cleaned_data['physics']}, Chemistry: {cleaned_data['chemistry']}
Total Percentage: {percentage:.2f}%
""".strip()

    return render(request, 'students/student_form.html', {
        'form': form,
        'student_data': student_data,
        'percentage': percentage
    })
