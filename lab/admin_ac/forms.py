from django import forms
from django.contrib.admin.widgets import AdminDateWidget

import admin_ac.admin_conector as admin_conector

def choice_club():
    clubs = admin_conector.get_all_club()
    return ((i[0],i[1]) for i in clubs)


def choices_match():
    matches = admin_conector.get_all_match()
    choices = []
    for m in matches:
        match_str = '{0} - {1}'.format(m['name_club1'], m['name_club2'])
        choices.append( ( m['id_match'], match_str ) )
    return choices


class MatchCreate(forms.Form):
    club_1 = forms.ChoiceField(choices=choice_club)
    club_2 = forms.ChoiceField(choices=choice_club)
    date = forms.DateField()


class MatchEdit(forms.Form):
    club_1 = forms.ChoiceField(choices=choice_club)
    club_2 = forms.ChoiceField(choices=choice_club)
    date = forms.DateField()
    gool_club_1 = forms.IntegerField(required=False)
    gool_club_2 = forms.IntegerField(required=False)


class SearchForm(forms.Form):
    date = forms.DateField(required=False)
    date_max = forms.DateField(required=False)
    money_min = forms.IntegerField(required=False)
    money_max = forms.IntegerField(required=False)


class EventCreate(forms.Form):
    match_id = forms.ChoiceField(choices=choices_match)
    coeff_win_first = forms.DecimalField(label='First Win')
    coeff_draw = forms.DecimalField(label='Draw')
    coeff_win_second = forms.DecimalField(label='Second Win')
