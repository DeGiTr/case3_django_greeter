from django.shortcuts import redirect, render

from .forms import NameForm
from .models import VisitorName


def home(request):
    greeting_name = request.session.pop("greeting_name", None)

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            request.session["greeting_name"] = visitor.name
            return redirect("greetings:home")
    else:
        form = NameForm()

    recent_names = VisitorName.objects.all()[:5]

    return render(
        request,
        "greetings/home.html",
        {
            "form": form,
            "greeting_name": greeting_name,
            "recent_names": recent_names,
        },
    )
