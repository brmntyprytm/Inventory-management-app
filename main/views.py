from django.shortcuts import render


def show_main(request):
    context = {"name": "Bramantyo", "class": "PBP International"}

    return render(request, "main.html", context)
