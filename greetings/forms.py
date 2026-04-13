from django import forms

from .models import VisitorName


class NameForm(forms.ModelForm):
    class Meta:
        model = VisitorName
        fields = ["name"]
        labels = {"name": "Ваше имя"}
        error_messages = {
            "name": {
                "required": "Введите имя, прежде чем отправлять форму.",
            }
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Например, Анна",
                    "autocomplete": "name",
                }
            )
        }

    def clean_name(self) -> str:
        name = self.cleaned_data["name"].strip()

        if not name:
            raise forms.ValidationError("Введите имя, прежде чем отправлять форму.")

        return name
