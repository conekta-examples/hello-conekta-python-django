from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


from sales.models import Sale
from django.conf import settings

@csrf_protect
def index(request):
    if request.method == 'GET':
        return render(request, 'charge.html')
    else:
        token_id = request.POST["conektaTokenId"]
        sale = Sale()
        if token_id: #Prevents send empty token
            return HttpResponse(sale.charge(300, token_id))
