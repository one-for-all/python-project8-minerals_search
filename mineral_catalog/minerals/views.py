from django.shortcuts import render, redirect, get_object_or_404
from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral.fields = mineral._meta.fields
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def random(_):
    mineral = Mineral.objects.order_by('?')[0]
    return redirect('minerals:detail', pk=mineral.pk)


def filter_by(request, letter):
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/list.html', {'minerals': minerals,
                                                  'letter': letter.upper()})


def search(request):
    minerals = Mineral.objects.filter(name__icontains=request.GET.get('q'))
    return render(request, 'minerals/list.html', {'minerals': minerals})


def filter_by_category(request, category):
    categories = [
        'Silicate',
        'Oxide',
        'Sulfate',
        'Sulfide',
        'Carbonate',
        'Halide',
        'Sulfosalt',
        'Phosphate',
        'Borate',
        'Organic',
        'Arsenate',
        'Native',
    ]
    if category == 'Other':
        minerals = Mineral.objects.exclude(category__in=categories)
    else:
        minerals = Mineral.objects.filter(category__iexact=category)
    return render(request, 'minerals/list.html', {'minerals': minerals,
                                                  'category': category})
