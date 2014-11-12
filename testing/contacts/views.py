from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views import generic

from django.db.models import Q

from .models import Contact
from .forms import ContactForm


def index(request):
    return render(
        request,
        "index.html",
        {
            "contacts": Contact.objects.all().order_by("-create_date")
        },
    )


class Show(generic.DetailView):
    model = Contact
    template_name = "show.html"


def edit(request, contact_id=None):
    if contact_id:
        contact = get_object_or_404(Contact, pk=contact_id)
    else:
        contact = Contact()

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show", args=(contact.id,)))
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        "edit.html",
        {
            "contact": contact,
            "form": form,
        },
    )


class Data(BaseDatatableView):
    # The model we"re going to show
    model = Contact

    # define the columns that will be returned
    columns = ["first_name", "last_name", "position", "create_date"]

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ""
    order_columns = ["first_name", "last_name", "position", "create_date"]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 100

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == "position":
            return row.position.name
        elif column == "create_date":
            return row.create_date.strftime("%a %d %b %Y, à %H:%M:%S"),
        else:
            return super(Data, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get("search[value]", None)

        if search:
            qs = qs.filter(
                Q(first_name__contains=search) |
                Q(last_name__contains=search) |
                Q(position__name__contains=search)
            )

        return qs
