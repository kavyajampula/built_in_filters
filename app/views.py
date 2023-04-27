from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    t=datetime.datetime.now()
    d={'data':'hai FILTers How are yoU','t':t,'c':1}
    return render(request,'built_in_filters.html',d)