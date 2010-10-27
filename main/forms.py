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
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_(u'Prénom'))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_(u'Nom'))
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
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
        



import math
from itertools import chain

from django import forms
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

class ColumnCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    """
    Widget that renders multiple-select checkboxes in columns.
    Constructor takes number of columns and css class to apply
    to the <ul> elements that make up the columns.
    """
    def __init__(self, columns=2, css_class=None, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.columns = columns
        self.css_class = css_class

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        choices_enum = list(enumerate(chain(self.choices, choices)))

        # This is the part that splits the choices into columns.
        # Slices vertically.  Could be changed to slice horizontally, etc.
        column_sizes = columnize(len(choices_enum), self.columns)
        columns = []
        for column_size in column_sizes:
            columns.append(choices_enum[:column_size])
            choices_enum = choices_enum[column_size:]
        output = []
        for column in columns:
            if self.css_class:
                output.append(u'<ul class="%s"' % self.css_class)
            else:
                output.append(u'<ul>')
            # Normalize to strings
            str_values = set([force_unicode(v) for v in value])
            for i, (option_value, option_label) in column:
                # If an ID attribute was given, add a numeric index as a suffix,
                # so that the checkboxes don't all have the same ID attribute.
                if has_id:
                    final_attrs = dict(final_attrs, id='%s_%s' % (
                            attrs['id'], i))
                    label_for = u' for="%s"' % final_attrs['id']
                else:
                    label_for = ''

                cb = forms.CheckboxInput(
                    final_attrs, check_test=lambda value: value in str_values)
                option_value = force_unicode(option_value)
                rendered_cb = cb.render(name, option_value)
                option_label = conditional_escape(force_unicode(option_label))
                output.append(u'<li><label%s>%s %s</label></li>' % (
                        label_for, rendered_cb, option_label))
            output.append(u'</ul>')
        return mark_safe(u'\n'.join(output))


def columnize(items, columns):
    """
    Return a list containing numbers of elements per column if `items` items
    are to be divided into `columns` columns.

    >>> columnize(10, 1)
    [10]
    >>> columnize(10, 2)
    [5, 5]
    >>> columnize(10, 3)
    [4, 3, 3]
    >>> columnize(3, 4)
    [1, 1, 1, 0]
    """
    elts_per_column = []
    for col in range(columns):
        col_size = int(math.ceil(float(items) / columns))
        elts_per_column.append(col_size)
        items -= col_size
        columns -= 1
    return elts_per_column