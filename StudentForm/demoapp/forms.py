from django import forms

class StudentForm(forms.Form):
    sn = forms.CharField()
    sc = forms.CharField()
    si = forms.IntegerField()

    
