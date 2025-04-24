# employees/forms.py
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
