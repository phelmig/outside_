# -*- coding: utf-8 -*-


from django import forms


class LeadClosedForm(forms.Form):
    proof = forms.CharField(required=True,
                            min_length=5,
                            max_length=512,
                            widget=forms.TextInput(attrs={'placeholder':u"Nachweis"})
                            )


class LeadRepeatForm(forms.Form):
    date = forms.DateTimeField(required=True, input_formats=['%d.%m.%Y %H:%M'], widget=forms.HiddenInput())
    comment = forms.CharField(required=False,
                            min_length=0,
                            max_length=2048,
                            widget=forms.Textarea(attrs={'placeholder':u"Kommentar (optional)"})
                            )

class LeadFeedbackForm(forms.Form):
    lost = forms.BooleanField(label="Kunde ist verloren",required=False)
    comment = forms.CharField(required=True,
                            min_length=5,
                            max_length=2048,
                            widget=forms.Textarea(attrs={'placeholder':u"Feedback / Begründung"})
                            )