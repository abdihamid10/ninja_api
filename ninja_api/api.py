from ninja import NinjaAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from products.api import router
from ninja_extra import NinjaExtraAPI
api = NinjaExtraAPI()
api.add_router("/", router)

api.register_controllers(NinjaJWTDefaultController)