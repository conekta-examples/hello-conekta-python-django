from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from sales.models import Sale

def index(request):
    return HttpResponse("Hello, beauty. You're at the conekta index.")

def charge(request):
    token_id = 'tok_test_visa_4242'
    sale = Sale()
    return HttpResponse(sale.charge(300, token_id))
