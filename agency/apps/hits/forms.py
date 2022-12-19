from apps.hits.models import Hits
from django import forms
from apps.hitmen.models import User


class HitAddForm(forms.ModelForm):
    class Meta:
        """Meta definition for HitAddForm."""

        model = Hits

        fields = (
            "assigne",
            "description",
            "target_name",
            "status",
            "creator",
        )
        widgets = {
            "assigne": forms.Select(
                attrs={
                    "placeholder": "Assigne ...",
                    "class": "input-group-field",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Description ...",
                    "class": "input-group-field",
                }
            ),
            "target_name": forms.TextInput(
                attrs={
                    "placeholder": "Targert Name ...",
                    "class": "input-group-field",
                }
            ),
            "status": forms.Select(
                attrs={
                    "placeholder": "Status ...",
                    "class": "input-group-field",
                }
            ),
            "creator": forms.HiddenInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super(HitAddForm, self).__init__(*args, **kwargs)
        self.fields["assigne"].queryset = User.objects.hitmen_to_select(user)
        self.fields["creator"].initial = user.id


class HitAddBulkForm(forms.ModelForm):
    class Meta:
        """Meta definition for HitAddForm."""

        model = Hits

        fields = (
            "assigne",
            "description",
            "target_name",
            "status",
            "creator",
        )
        widgets = {
            "assigne": forms.Select(
                attrs={
                    "placeholder": "Assigne ...",
                    "class": "input-group-field",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Description ...",
                    "class": "input-group-field",
                }
            ),
            "target_name": forms.TextInput(
                attrs={
                    "placeholder": "Targert Name ...",
                    "class": "input-group-field",
                }
            ),
            "status": forms.Select(
                attrs={
                    "placeholder": "Status ...",
                    "class": "input-group-field",
                }
            ),
            "creator": forms.Select(
                attrs={
                    "placeholder": "Creator ...",
                    "class": "input-group-field",
                }
            ),
        }
