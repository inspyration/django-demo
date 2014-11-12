from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact


def index(request):
    return render(
        request,
        'index.html',
        {
            "contacts": Contact.objects.all().order_by("-create_date")
        },
    )


def show(request, contact_id):
    return HttpResponse("Contacts view page.")


def edit(request, contact_id):
    return HttpResponse("Contacts edit page.")
