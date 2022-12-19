from apps.hitmen.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class AutheticatedPermissionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(AutheticatedPermissionMixin, self).dispatch(
                request, *args, **kwargs
            )
        return HttpResponseForbidden()


class AdminAndManagersPermissionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        manager = User.objects.manager_of_hitman(request.user.id)
        if request.user.is_superuser or manager is None:
            return super(AdminAndManagersPermissionMixin, self).dispatch(
                request, *args, **kwargs
            )
        return HttpResponseForbidden()
