from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")


# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")


# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


def index(request):
    return render(request, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirected_month = months[month-1]
    redirected_path = reverse("month-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirected_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except Exception:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # Django will automatically find 404.html in templates folder
        raise Http404()
