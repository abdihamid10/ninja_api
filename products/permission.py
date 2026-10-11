from functools import wraps
from ninja.errors import HttpError

def has_permission(user, perm_code:str):
    if not user or not user.is_authenticated:
        raise HttpError(401, "unauthorized")

    if user.is_superuser:
        return True

    if not user.has_perm(perm_code):
        raise HttpError(403, "permission Denied")
    return True

def get_user_roles(user):
    if not user or not user.is_authenticated:
        return set()
    if not hasattr(user, "_roles"):
        user._roles = set(user.groups.values_list("name", flat=True))
    return user._roles

    


def required_owner(user):
    if not user or not user.is_authenticated:
        raise HttpError(401, "unauthorised")
    roles = get_user_roles(user)
    is_owner = "Owner" in roles
    if not is_owner and not user.is_superuser:
        raise HttpError(403, "permission Denied only Owner can do")



def required_Manager(user):
    if not user or not user.is_authenticated:
            raise HttpError(401, "unauthorised")
    roles = get_user_roles(user)
    is_owner = "Owner" in roles
    is_manager = "Manager" in roles
    if not is_manager and not is_owner and not user.is_superuser:
        raise HttpError(403, "Permission Denied: only Manager or owner can access")



#object lever permission
def object_owner_or_Admin(obj, user):
    if not user or not user.is_authenticated:
        raise HttpError(401, "Unauthorised")
    roles = get_user_roles(user)
    is_owner = "Owner" in roles
    is_manager = "Manager" in roles
    if obj.owner != user and not is_manager and not is_owner and not user.is_superuser:
        raise HttpError(403, "permission denied")
    
   