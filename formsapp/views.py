from django.shortcuts import render
from .forms import Forma1
from .forms import Forma2
from .forms import Forma3
from django.http import HttpResponse


# Create your views here.
def index(req):
    print(req)
    return render(req, 'index.html')


def formaone(req):
    anketa = Forma1()
    if req.method == 'POST':
        k1 = req.POST.get('name')
        k2 = req.POST.get('age')
        out = f'<p>{k1}</p><p>{k2}</p>'
        return HttpResponse(out)
    else:
        data = {
            'forma': anketa
        }
    return render(req, 'forform.html', data)


def upload(pic, name):
    image = pic
    file = open(f'formsapp/static/img/{name}.jpg', 'wb')
    file.write(image)
    fpath = f'img/{name}.jpg'
    return fpath


def formatwo(req):
    anketa = Forma2()

    if req.POST:
        k1 = req.POST.get('name')
        k2 = req.POST.get('num')
        k3 = req.POST.get('email')
        k4 = req.POST.get('check1')
        k5 = req.POST.get('check2')
        k6 = req.POST.get('lang')
        k7 = req.FILES.get('file').read()
        k7 = upload(k7, k1)
        if k4 == 'on':
            k4 = 'да'
        else:
            k4 = 'нет'

        if k5 == 'false':
            k5 = 'не получено'
        elif k5 == 'true':
            k5 == 'получено'
        else:
            k5 = 'не определился'

        data = {
            'forma': anketa,
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            'k5': k5,
            'k6': k6,
            'k7': k7,
        }

        return render(req, 'user.html', data)
    else:
        data = {
            'forma': anketa
        }
    return render(req, 'forform.html', data)


def formbirds(req):
    anketa = Forma3()

    if req.POST:
        k1 = req.POST.get('name')
        k2 = req.POST.get('family')
        k3 = req.POST.get('age')
        k4 = req.POST.get('color')
        k5 = req.POST.get('food')
        k6 = req.FILES.get('file').read()
        k6 = upload(k6, k1)

        data = {
            'forma': anketa,
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            'k5': k5,
            'k6': k6,
        }

        return render(req, 'final.html', data)
    else:
        data = {
            'forma': anketa
        }
    return render(req, 'forform.html', data)
