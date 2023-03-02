from rest_framework.authentication import SessionAuthentication
from supertokens_python.recipe.session import SessionContainer

from .models import STUser


class SupertokensAuthentication(SessionAuthentication):
    def authenticate(self, request):
        session_: SessionContainer | None = getattr(request, "supertokens", None)

        if not session_:
            return None

        user_id = session_.get_user_id()

        try:
            user = STUser.objects.get(pk=user_id)
        except STUser.DoesNotExist:
            user = STUser(pk=user_id, display_name="")
            user.save()

        self.enforce_csrf(request)

        return (user, None)
