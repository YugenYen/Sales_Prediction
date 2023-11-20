from django.shortcuts import render
from .ml_model import predict_sales

def index(request):
    if request.method == 'POST':
        tv = request.POST.get('tv', 0)
        newspaper = request.POST.get('newspaper', 0)
        radio = request.POST.get('radio', 0)

        prediction = predict_sales(tv, newspaper, radio)
        return render(request, 'index.html', {'prediction': prediction})
    else:
        return render(request, 'index.html')
