from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Marks

class marksenteringform(forms.ModelForm):
    class Meta:
        model =  Marks
        fields=['Name','Roll_no','MarksInPhysics','MarksInMathematics','MarksInChemistry']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),'Roll_no':forms.NumberInput(attrs={'class':'form-control'}),'MarksInPhysics':forms.NumberInput(attrs={'class':'form-control'}),'MarksInMathematics':forms.NumberInput(attrs={'class':'form-control'}),'MarksInChemistry':forms.NumberInput(attrs={'class':'form-control'})}
        
        