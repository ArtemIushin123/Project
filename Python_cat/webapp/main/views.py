from django.shortcuts import render
import random as r
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Python_cat.Python_SQL import test_db


# Create your views here.
def main_page(request):
    import random as r
    a = []
    a = [[r.randint(0, 1) for j in range(7)] for i in range(9)]
    h = 13
    for i in a:
        if h != 24:
            str_t = ":00"
            i.insert(0, str(h) + str_t)
            h += 1
    ddmmyyyyn = "27:03:2077"
    ddmmyyyyk = "2:04:2077"
    data = {
        'hk': a,
        # формат переменной a это двумерный массив где: '8:00' это время записи 0 свободно 1 занято [['8:00', 0, 1, 0, 0, 1, 0, 1], ['8:30', 1, 1, 1, 1, 0, 0, 1], ['9:00', 1, 1, 0, 0, 1, 0, 1], ['9:30', 1, 0, 0, 0, 1, 0, 1], ['10:00', 0, 0, 0, 0, 1, 0, 0], ['10:30', 0, 1, 1, 1, 0, 0, 1], ['11:00', 1, 1, 0, 1, 1, 0, 0]
        'DDMMYYYYn': ddmmyyyyn,  # это день, месяц, год (начало недели)
        'DDMMYYYYk': ddmmyyyyk,  # это день, месяц, год (конец недели)
    }
    return render(request, "main/index.html", data)

<<<<<<< HEAD
=======

def appointment(request):
    import random as r
    a = []
    a = [[r.randint(0, 1) for j in range(7)] for i in range(9)]
    h = 13
    for i in a:
        if h != 24:
            str_t = ":00"
            i.insert(0, str(h) + str_t)
            h += 1
    ddmmyyyyn = "27:03:2077"
    ddmmyyyyk = "2:04:2077"
    data = {
        'hk': a,
        # формат переменной a это двумерный массив где: '8:00' это время записи 0 свободно 1 занято [['8:00', 0, 1, 0, 0, 1, 0, 1], ['8:30', 1, 1, 1, 1, 0, 0, 1], ['9:00', 1, 1, 0, 0, 1, 0, 1], ['9:30', 1, 0, 0, 0, 1, 0, 1], ['10:00', 0, 0, 0, 0, 1, 0, 0], ['10:30', 0, 1, 1, 1, 0, 0, 1], ['11:00', 1, 1, 0, 1, 1, 0, 0]
        'DDMMYYYYn': ddmmyyyyn,  # это день, месяц, год (начало недели)
        'DDMMYYYYk': ddmmyyyyk,  # это день, месяц, год (конец недели)

    }
    return render(request, "main/appointment.html", data)


def contacts1(request):
    return render(request, "main/contacts1.html")


def get_test(request):
    data = {
        'clients': test_db.get_all_clients()
    }
    return render(request, 'main/test.html', data)

>>>>>>> main
