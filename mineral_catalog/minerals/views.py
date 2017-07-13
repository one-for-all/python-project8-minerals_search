from django.shortcuts import render, redirect, get_object_or_404
from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral.fields = mineral._meta.fields
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def random(request):
    mineral = Mineral.objects.order_by('?')[0]
    return redirect('minerals:detail', pk=mineral.pk)
