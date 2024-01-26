from django import forms


class UserInformation(forms.Form):

    val1 = forms.FloatField(label='pregnancies')
    val2 = forms.FloatField(label='Glucose')
    val3 = forms.FloatField(label='Blood Pressure ')
    val4 = forms.FloatField(label='Skin Thikness')
    val5 = forms.FloatField(label='Insulin')
    val6 = forms.FloatField(label='BMI')
    val7 = forms.FloatField(label='Diabetes Pedigree Function')
    val8 = forms.FloatField(label='Age')
