from apps.hitmen.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

#

# class HitmenPermissionMixin(LoginRequiredMixin):
#     login_url = reverse_lazy('users_app:user-login')

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         #
#         if request.user.manager
#             # no tiene autorizacion
#             return HttpResponseRedirect(
#                 reverse(
#                     'users_app:user-login'
#                 )
#             )

#         return super().dispatch(request, *args, **kwargs)


# class ManagersPermissionMixin(object):
#     login_url = reverse_lazy("hitmen_app:hitman-login")

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         if not request.user.manager == 0:
#             # The user haven't authorization
#             return Http404("The hitman haven't authorization")
#         return super().dispatch(request, *args, **kwargs)


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
        if request.user.is_staff or manager is None:
            return super(AdminAndManagersPermissionMixin, self).dispatch(
                request, *args, **kwargs
            )
        return HttpResponseForbidden()
