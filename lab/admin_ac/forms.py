from django import forms
from django.contrib.admin.widgets import AdminDateWidget

import admin_ac.admin_conector as admin_conector
def choise_club():
    clubs = admin_conector.get_all_club()
    return ((i[0],i[1]) for i in clubs)


class MatchCreate(forms.Form):
    club_1 = forms.ChoiceField(choices=choise_club)
    club_2 = forms.ChoiceField(choices=choise_club)
    date = forms.DateField()
    coefficient = forms.DecimalField(max_digits=3)

class MatchEdit(forms.Form):
    club_1 = forms.ChoiceField(choices=choise_club)
    club_2 = forms.ChoiceField(choices=choise_club)
    date = forms.DateField()
    coefficient = forms.DecimalField(max_digits=3)
    gool_club_1 = forms.IntegerField(required=False)
    gool_club_2 = forms.IntegerField(required=False)

class SearchForm(forms.Form):
    date = forms.DateField(required=False)
    date_max = forms.DateField(required=False)
    money_min = forms.IntegerField(required=False)
    money_max = forms.IntegerField(required=False)
