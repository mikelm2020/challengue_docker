from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

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


# class ManagersPermissionMixin(LoginRequiredMixin):
#     login_url = reverse_lazy('users_app:user-login')

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         #
#         if not check_ocupation_user(request.user.ocupation, User.VENTAS):
#             # no tiene autorizacion
#             return HttpResponseRedirect(
#                 reverse(
#                     'users_app:user-login'
#                 )
#             )
#         return super().dispatch(request, *args, **kwargs)


class AdminPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy("users_app:user-login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not request.user.is_staff:
            # The user haven't authorization
            return Http404("The hitman haven't authorization")
        return super().dispatch(request, *args, **kwargs)
