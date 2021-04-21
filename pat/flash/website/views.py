from django.shortcuts import render
import random


def home(request):
    return render(request, 'k.html', {})


def divide(request):
    return render(request, 'divide.html', {})


def multiply(request):
    return render(request, 'multiply.html', {})


def subtract(request):
    from random import randint

    num1 = randint(0, 0)
    num2 = randint(0, 10)
    request.session['num1'] = num1
    request.session['num2'] = num2

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) - int(old_num_2)
        print(correct_answer)
#        print(old_num_2)
        if (answer) == (correct_answer):
            my_answer = "Correct!"
            color = 'success'
        else:
            my_answer = 'incorrect'
            color = 'danger'

        return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num1,
            'num_2': num2,
            'color': color
        })

    return render(request, 'add.html', {
        'num_1': num1,
        'num_2': num2, })


def add(request):
    from random import randint

    num1 = randint(0, 0)
    num2 = randint(0, 10)
    request.session['num1'] = num1
    request.session['num2'] = num2

    if request.method == "POST":
        answer =    request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) + int(old_num_2)
        print(correct_answer)
        print(old_num_2)
        if (answer) == (correct_answer):
            my_answer = "Correct!"
            color = 'success'
        else:
            my_answer = 'incorrect'
            color = 'danger'

        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num1,
            'num_2': num2,
            'color': color
        })

    return render(request, 'add.html', {
        'num_1': num1,
        'num_2': num2,})
