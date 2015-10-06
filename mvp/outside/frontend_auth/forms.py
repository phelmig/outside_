from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from longerusernameandemail.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from collections import OrderedDict


class SecdashPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = _(u'Ihre E-Mail Adresse')


class SecdashSetPasswordForm(SetPasswordForm):
    def __init__(self,user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['placeholder'] = _(u'Ihr neues Passwort')
        self.fields['new_password2'].widget.attrs['placeholder'] = _(u'Bitte wiederholen Sie Ihr neues Passwort')


SecdashSetPasswordForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['new_password1', 'new_password2']
)

class SecdashPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['placeholder'] = _(u'Ihr aktuelles Passwort')
        self.fields['new_password1'].widget.attrs['placeholder'] = _(u'Ihr neues Passwort')
        self.fields['new_password2'].widget.attrs['placeholder'] = _(u'Bitte wiederholen Sie Ihr neues Passwort')

        self.fields.keyOrder = ['old_password', 'new_password1', 'new_password1']


SecdashPasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
)


class SecdashAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SecdashAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text=u""
        self.fields['username'].widget.attrs['placeholder'] = _(u'Ihre E-Mail Adresse')
        self.fields['password'].widget.attrs['placeholder'] = _(u'Ihr Passwort')