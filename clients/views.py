from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')


def client(request):
    return render(request,'client-detail.html')