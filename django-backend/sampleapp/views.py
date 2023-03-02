from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.django.syncio import verify_session
from supertokens_python.recipe.userroles.interfaces import UnknownRoleError
from supertokens_python.recipe.userroles.syncio import create_new_role_or_add_permissions, add_role_to_user


def add_role_to_user_func(user_id: str, role: str):
    res = add_role_to_user(user_id, role)
    if isinstance(res, UnknownRoleError):
        # No such role exists
        return

    if res.did_user_already_have_role:
        # User already had this role
        pass


def create_role(role, permissions):
    res = create_new_role_or_add_permissions(role, permissions, None)
    if not res.created_new_role:
        # The role already existed
        return False
    return True


@method_decorator(verify_session(), name="dispatch")
class SessionView(APIView):
    def get(self, request, format=None):
        session_: SessionContainer = request.supertokens  # type: ignore
        # print(session_.__dict__)

        role, permissions = 'user', ['read']
        ok = create_role(role, permissions)
        if ok:
            add_role_to_user_func(session_.get_user_id(), role)

        return Response(
            {
                "sessionHandle": session_.get_handle(),
                "userId": session_.get_user_id(),
                "accessTokenPayload": session_.get_access_token_payload(),
                "sessionData": session_.sync_get_session_data(),
                "user": str(request.user) if request.user is not None else request.user,
            }
        )
