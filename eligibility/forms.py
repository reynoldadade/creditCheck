from django import forms


class IdForm(forms.Form):
    Client_id = forms.IntegerField(max_value=99999999,min_value=1)