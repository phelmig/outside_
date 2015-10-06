"""
frontend_auth is a wrapper around the `django.contrib.auth.view` Views.

*   **templates/**  Contains the templates for login / pw change / pw reset views and the password_reset emails
*   **auth_mixins.py** Provides a simple mixin that tests if `instance.agency == request.user.agencyemployee.agency`, more to come
*   **forms.py** Contains simple wrapper around `django.contrib.auth.forms` to use placeholders instead of labels
*   **urls.py** Creates `django.contrib.auth.views` for with the following names:
    *   login   -    Login
    *   logout  -   Logout -> Redirect to 'login'
    *   change_password -   unused view to change the password
    *   password_change_done    - unused as well
    *   password_reset - Shows a form to request a pw reset
    *   password_reset_done - The view after the requested pw reset
    *   password_reset_confirm - The view after the user clicked on the reset link in the mail
    *   password_reset_complete - The view after the manual password reset
"""