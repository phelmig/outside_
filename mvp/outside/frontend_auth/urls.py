from django.conf.urls import patterns, include, url
from frontend_auth.forms import SecdashAuthForm, SecdashPasswordChangeForm, SecdashPasswordResetForm, \
    SecdashSetPasswordForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('django.contrib.auth.views',
                       url(r'^login/$', 'login',
                           {'template_name': 'frontend_auth/login.html', 'authentication_form': SecdashAuthForm},
                           name="login"),
                       url(r'^logout/$', 'logout', {'next_page': '/login'}, name='logout'),
                       url(r'^password_changed/$', 'password_change_done',
                           {'template_name': 'frontend_auth/change_password_done.html'}, name='password_change_done'),
                       url(r'^change_password/$', 'password_change',
                           {'template_name': 'frontend_auth/change_password.html',
                            'password_change_form': SecdashPasswordChangeForm}, name="change_password"),

                       url(r'^password_reset/$', 'password_reset',
                           {'template_name': 'frontend_auth/password_reset.html',
                            'html_email_template_name': 'frontend_auth/mails/password_reset_mail.html',
                            'email_template_name': 'frontend_auth/mails/password_reset_mail.txt',
                            'password_reset_form': SecdashPasswordResetForm}, name="password_reset"),
                       url(r'^password_reset_done/$', 'password_reset_done',
                           {'template_name': 'frontend_auth/password_reset_done.html'}, name="password_reset_done"),
                       url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           'password_reset_confirm',
                           {'template_name': 'frontend_auth/password_reset_confirm.html',
                            'set_password_form': SecdashSetPasswordForm}, name="password_reset_confirm"),
                       url(r'^password_reset_complete/$', 'password_reset_complete',
                           {'template_name': 'frontend_auth/password_reset_complete.html'},
                           name="password_reset_complete"),
                       )
