from django.shortcuts import render, redirect
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.conf import settings
import os
from .forms import UserInformation
from django.contrib import messages


def home(request):
    img_path = os.path.join('static', 'DiabetesPrediction', 'images', 'Picture.jpg')
    return render(request, 'home.html', {'img_path': img_path})


def predict(request):
    data = pd.read_csv(r"C:\Users\pc\Desktop\Project 2 MeriSKILL/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    if request.method == 'POST':
        form = UserInformation(request.POST)
        if form.is_valid():

            val1 = form.cleaned_data['val1']
            val2 = form.cleaned_data['val2']
            val3 = form.cleaned_data['val3']
            val4 = form.cleaned_data['val4']
            val5 = form.cleaned_data['val5']
            val6 = form.cleaned_data['val7']
            bmi = form.cleaned_data['val7']
            val8 = form.cleaned_data['val8']
            print(f"Val1: {val1},Val2: {val2}")
            # if bmi<18.5:
            #     messages.warning(request, 'Sous-poids')
            # elif 18.5< bmi <24.9:
            #     messages.warning(request, 'Poid normal')
            # elif 25< bmi < 29.9:
            #     messages.warning(request, 'Surpoids')
            # elif 30 < bmi < 43.5:
            #     messages.warning(request, 'Obésité de classe I')
            # elif 35 < bmi < 39.9:
            #     messages.warning(request, 'Obésité de classe II ')
            # elif bmi > 40:
            #     messages.warning(request, 'Obésité de classeIII (obésité sévère) ')

            pared = model.predict([[val1, val2, val3, val4, val5, val6, bmi, val8]])

            result1 = ""
            if pared == [1]:
                result1 = "Positive"
                print(result1)
                messages.success(request, 'Positif!')
            elif pared == [0]:
                result1 = 'Negative'
                print(result1)
                messages.error(request, 'Negatif!')

    else:
        form = UserInformation()
    return render(request, 'user_info.html', {'form': form})


