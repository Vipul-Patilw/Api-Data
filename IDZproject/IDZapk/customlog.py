from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib import messages
class CustomLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                             self.permission_denied_message)
            return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )