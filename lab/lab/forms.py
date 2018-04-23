from django import forms
import admin_ac.admin_conector as admin_conector

def choise_club():
    clubs = admin_conector.get_all_club()
    return ((i[0],i[1]) for i in clubs)

class BetMake(forms.Form):
    def __init__(self, *args, **kwargs ):
        super(BetMake, self).__init__(*args, **kwargs)
        self.fields['club'].choices = args[0]['choise']

    club = forms.ChoiceField()
    num = forms.IntegerField()
