from django.shortcuts import render, get_object_or_404
from .models import Project
# from orders.forms import OrderForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from .forms import PostFilterForm


def project_index(request):
    vse_posti = Project.objects.all()
    # form = ProjectFilterForm(request.GET)
    # if form.is_valid():
    #     if form.cleaned_data["min_price"]:
    #         vse_posti = vse_posti.filter(price__gte=form.cleaned_data["min_price"])
    #     if form.cleaned_data["max_price"]:
    #         vse_posti = vse_posti.filter(price__lte=form.cleaned_data["max_price"])
    #     if form.cleaned_data["ordering"]:
    #         vse_posti = vse_posti.order_by(form.cleaned_data["ordering"])
    context = {"vse_posti": vse_posti}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    # post = get_object_or_404(Project, id=post_id)
    post = Project.objects.get(pk=pk)
    context = {'post': post}

    # form = OrderForm(request.POST or None, initial={"post": post})
    return render(request, "project_detail.html", context)