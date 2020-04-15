from django.shortcuts import render

# Create your views here.
#  VUE项目 后台
def lin(request):

    return render(request, 'lin/index.html')

def map(request):

    return render(request, 'map/index.html')

def hutProject(request):

    return render(request, 'hutProject/index.html')