from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Contacts index page.")


def show(request, contact_id):
    return HttpResponse("Contacts view page.")


def edit(request, contact_id):
    return HttpResponse("Contacts edit page.")
