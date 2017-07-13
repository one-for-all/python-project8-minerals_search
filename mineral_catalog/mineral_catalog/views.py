from django.shortcuts import redirect


def index(_):
    return redirect('minerals:list')
