from django import forms
import admin_ac.admin_conector as admin_conector


class BetForm(forms.Form):
    def __init__(self, id_match, *args, **kwargs):

        super(BetForm, self).__init__(*args, **kwargs)

        events = admin_conector.get_event(id_match)
        choices = [ ( event['id_event'], event['name_event'] )  for event in  events ]
        self.fields['event'].choices = choices

    event = forms.ChoiceField()
    money = forms.IntegerField()
