from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class UserInformation(forms.Form):

    val1 = forms.IntegerField(label='pregnancies ', validators=[MinValueValidator(0), MaxValueValidator(30)])
    val2 = forms.FloatField(label='Glucose (mg/dL) ', validators=[MinValueValidator(0), MaxValueValidator(220)])
    val3 = forms.FloatField(label='Blood Pressure (mm Hg)', validators=[MinValueValidator(1), MaxValueValidator(200)])
    val4 = forms.FloatField(label='Skin Thikness', validators=[MinValueValidator(0)])
    val5 = forms.FloatField(label='Insulin (pmol/L)', validators=[MinValueValidator(0)])
    val6 = forms.FloatField(label='BMI', validators= [MinValueValidator(0)])
    val7 = forms.FloatField(label='Diabetes Pedigree Function', validators=[MinValueValidator(0), MaxValueValidator(2)])
    val8 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(130)], label='Age')
