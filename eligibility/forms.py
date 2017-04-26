from django import forms


class IdForm(forms.Form):
    # take employee id
    employee_id =forms.IntegerField(label="Employee ID" ,min_value=1,max_value=9999999)