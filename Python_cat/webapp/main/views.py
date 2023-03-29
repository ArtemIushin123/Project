from django.shortcuts import render
import random as r


# Create your views here.
def main_page(request):
    import random as r
    a = []
    a = [[r.randint(0, 1) for j in range(7)] for i in range(32)]
    t = 1
    h = 8
    for i in a:
        if t % 2 == 0:
            str_t = ":30"
            i.insert(0, str(h) + str_t)
            h += 1
        else:
            str_t = ":00"
            i.insert(0, str(h) + str_t)

        t += 1
    data = {
        '_ctr': 7,
        'hk': a

    }
    return render(request, "main/index.html", data)


def appointment(request):
    import random as r
    a = []
    a = [[r.randint(0, 1) for j in range(7)] for i in range(32)]
    t = 1
    h = 8
    for i in a:
        if t % 2 == 0:
            str_t = ":30"
            i.insert(0, str(h) + str_t)
            h += 1
        else:
            str_t = ":00"
            i.insert(0, str(h) + str_t)

        t += 1
    data = {
        'hk': a,
    }
    return render(request, "main/appointment.html", data)


def contacts1(request):
    import random as r
    a = []
    a = [[r.randint(0, 1) for j in range(7)] for i in range(32)]
    t = 1
    h = 8
    for i in a:
        if t % 2 == 0:
            str_t = ":30"
            i.insert(0, str(h) + str_t)
            h += 1
        else:
            str_t = ":00"
            i.insert(0, str(h) + str_t)

        t += 1
    data = {
        'hk': a,
    }
    return render(request, "main/contacts1.html", data)
