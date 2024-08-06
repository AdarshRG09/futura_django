from django import forms

from new_app.models import Construction



class Constructionform(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ("__all__")