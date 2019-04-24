from django.http import HttpResponse
from django.shortcuts import render

import operator


def home(request):
    return render(request, "countword.html")


def welcome(request):
    return HttpResponse('sample welcom')

def count(request):
    msg = request.GET['message']
    w1 = msg.split()
    c1 = len(msg)- msg.count(' ')
    wlcount = {}
    for word in w1:
        if word in wlcount:
            wlcount[word] += 1
        else:
            wlcount[word] = 1
    sort1 = sorted(wlcount.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html',{"msg":msg, "length":len(w1), "clength":c1, "abc": wlcount, "edf": sort1})
