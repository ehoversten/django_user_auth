from django.shortcuts import render, redirect, HttpResponse


def landing(request):
    content = "You have landed"
    context = {
        "content" : content,
    }
    return render(request, "landing.html", context)
    # return HttpResponse("You have LANDED...")
