from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.db.transaction import atomic, non_atomic_requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ipaddress import ip_address, ip_network
import json


@csrf_exempt
@require_POST
def webhook(request):
    whitelist_ip = "18.158.59.198"
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)

    if client_ip_address != ip_network(whitelist_ip):
        return HttpResponseForbidden('Permission denied.')

    payload = json.loads(request.body)
    try:
        if payload['EventType'] == "BankTransferPayout":
            pass
        elif payload['EventType'] == "BankTransferFunding":
            pass
        else:
            pass
        return HttpResponse(status=200)

    except:
        if payload['TransactionType'] == "credit":
            pass
        elif payload['TransactionType'] == "debit":
            pass
        else:
            pass
        return HttpResponse(status=200)

    