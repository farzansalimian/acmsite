from .models import Buyers
from django import forms


class buyersForm(forms.ModelForm):

    class Meta:
        model = Buyers
        fields = ('buyerFirstName', 'buyerlastName','nationalCode','address' ,'phoneNumber','mobileNumber', 'requireDeliveryTime', 'Deliveryaddress', 'deliveryMode', 'genderPressent')

        
    def save(self, commit=True):
        # Save the provided password in hashed format
        buyers = super(buyersForm, self).save(commit=False)
        # create a new user hash for activating email.
        if commit:
            buyers.save()
        return buyers

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    fullName = forms.CharField(max_length=100)
