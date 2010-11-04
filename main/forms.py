# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


# Repiquage carrément du modèle
attrs_dict = { 'class': 'required' }

class CredisRegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    
    """
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs=attrs_dict),
                                 label=_(u'Prénom'),
                                 )
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_(u'Nom'),
                                )
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") },
                                help_text=u"Ce nom d'utilisateur sera public, affiché à la place du nom pour les visiteurs anonymes du site (Google par exemple)"
                                )
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Email address"),
                             help_text= u"Préférez votre e-mail personnel à celui de votre structure."
                             )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"),
                                help_text= u"Notez qu'utiliser les majuscules ou les minuscules peut être important"
                                )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again)"))
                                
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict), 
                             label=_(u'I have read and agree to the Terms of Service'), 
                             error_messages={'required': u'Vous devez accepter les Conditions Générales du site.'})
    
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
        
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("A user with that username already exists."))
        
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data
        
