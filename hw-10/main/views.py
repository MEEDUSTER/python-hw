from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Contact


def contact_list(request):
    query = request.GET.get("q", "").strip()
    contacts = list(Contact.objects.all())
    if query:
        q = query.lower()
        contacts = [
            contact
            for contact in contacts
            if q in contact.first_name.lower() or q in contact.last_name.lower()
        ]
    return render(
        request,
        "main/contact_list.html",
        {"contacts": contacts, "query": query, "page": "list"},
    )


def contact_add(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(
        request,
        "main/contact_form.html",
        {"form": form, "page": "add", "is_edit": False},
    )


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(
        request,
        "main/contact_form.html",
        {"form": form, "page": "list", "is_edit": True, "contact": contact},
    )


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(
        request,
        "main/contact_confirm_delete.html",
        {"contact": contact, "page": "list"},
    )
