from django import forms
from . import models

THERAPY_CHOICES = [('Therapy','Therapy'),('EMDR','EMDR'),('Couple','Couple'),('Individual','Individual')]
LOCATION_CHOICES = [('Location','Location'),('Online','Online'), ('In Person','In Person')]

class PriceForm(forms.Form):
    class Meta:
        model = models.Prices
        fields = ['Therapy', 'Online', 'In_Person']
        
class MessageForm(forms.Form):
    Name = forms.CharField(max_length=25, 
                           help_text='25 characters max.', 
                           widget= forms.TextInput(attrs={'Placeholder': 'Name', 'Class' : 'name-form', 'name' : 'name:'}))
    Email = forms.EmailField(help_text='A valid email address, please.',
                             widget=forms.EmailInput(attrs={'Placeholder': 'Email', 'Class' : 'email-form', 'name' : 'email:'}))
    Therapy = forms.ChoiceField(initial='Therapy',
                                widget= forms.Select(attrs={'Id':'therapy', 'Class' : 'therapy-form', 'name' : 'therapy'}),
                                choices=THERAPY_CHOICES)
    Type = forms.ChoiceField(initial='Location',
                           widget= forms.Select(attrs={'Id':'types', 'Class' : 'location-form', 'name' : 'location'}),
                           choices=LOCATION_CHOICES)
    Message = forms.CharField(max_length=1000, 
                              required=False,
                              widget= forms.Textarea(attrs={'Class' : 'message-form', 'name' : 'message'}))
    class Meta:
        fields = ['Name', 'Email', 'Therapy', 'Type', 'Message']
        
class TherapyForm(forms.Form):
    class Meta:
        model = models.Therapies
        fields = ['Therapy',]