from django import forms
from . models import *
class Detail(forms.ModelForm):
    class Meta:
        model=DetailRegister
        fields=['bodytype','weight','mothertongue','maritalstatus','physicalstatus','eatinghabits','drinkinghabits','smokinghabits','contactnumber','parentcontact','star','country','state','citizenship','dateofbirth','placeofbirth','timeofbirth','forwho','partner','partnerage','partnerheight','partnermothertongue','partnerphysicalstatus','partnereatinghabits','partnersmokinghabits','partnerdrinkinghabits','partnereducation','partneroccupation','partnerannualincome','partnerreligion','partnercaste','partnerstar','partnercountry','partnerstate','partnercitizenship','partnercity',]