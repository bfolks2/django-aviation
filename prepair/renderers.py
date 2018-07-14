from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework import exceptions


class PrepairAPIRenderer(BrowsableAPIRenderer):
    """
    HTML renderer used to override methods shown in the Browsable API.
    """

    def show_form_for_method(self, view, method, request, obj):
        """
        Returns True if a form should be shown for this method.
        """
        if method not in view.prepair_browsable and not self.has_prepair_permission(request):
            return  # Not a valid method

        try:
            view.check_permissions(request)
            if obj is not None:
                view.check_object_permissions(request, obj)
        except exceptions.APIException:
            return False  # Doesn't have permissions
        return True

    @staticmethod
    def has_prepair_permission(request):
        return request.user and request.user.is_staff and request.user.is_superuser
