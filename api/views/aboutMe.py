import uuid
from flask import request, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from api.database.models.items import about_me
from api.database.models.schemas import AboutMeSchema, DefaultErrorSchema, IntegerInputSchema

# Blueprint in Flask Smorest would divide API in multiple segment
blp = Blueprint("about_me", __name__, description="Operations on about_me, this text is added in blp=Blueprint()")


@blp.route("/about_me") # This is a decorator that will add a route to the blueprint
class AboutMeValues(MethodView):

    @blp.response(200, schema=AboutMeSchema(many=False), )
    @blp.doc(description="There should be option for read more, and check more of my photos.",
             summary="Shows all about_me values")
    @blp.doc(responses={
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        500: {"description": "Internal Server Error"}
    })
    def get(self):
        # example function to fetch data
        schema = AboutMeSchema(many=False)
        about_me_data = schema.dump(about_me)
        # about_me_data = False

        if not about_me_data:
            abort(404)

        response = make_response(about_me_data, 200)
        response.headers["Cache-Control"] = "no-store"
        return response

    @blp.errorhandler(404)
    def handle_404_error(err):
        schema = DefaultErrorSchema()
        return schema.dump({'code': 404,
                            'message': "Work in progress, please come back later",
                            'errors': {"my_error": err},
                            'status': 'NOT FOUND'}), 404

    @blp.arguments(IntegerInputSchema)
    @blp.response(201, schema=AboutMeSchema(many=False), )
    @blp.doc(description="There should be option for copy email and phone number also.",
             summary="Adding new photos to my page. For now it's integer")
    @blp.doc(responses={
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        500: {"description": "Internal Server Error"}
    })
    def post(self, data) -> dict|tuple:
        item_id = str(uuid.uuid4())
        about_me[item_id] = data['value']
        response_data = {"item_id": item_id, "added_value": data['value']}
        response = make_response(response_data, 201)
        response.headers['content-type'] = 'application/json'
        return response

    def put(self) -> dict:
        data = request.json
        item_id = data.get("item_id")
        if item_id not in about_me:
            abort(404, message="Item not found")
        about_me[item_id].update(data)
        return about_me[item_id]

    def delete(self) -> dict:
        data = request.json
        item_id = data.get("item_id")
        if item_id not in about_me:
            abort(404, message="Item not found")
        del about_me[item_id]
        return {"message": "Item deleted"}

    def patch(self) -> dict:
        data = request.json
        item_id = data.get("item_id")
        if item_id not in about_me:
            abort(404, message="Item not found")
        about_me[item_id].update(data)
        return about_me[item_id]

    def options(self) -> dict:
        return {"message": "Options"}

    def head(self) -> dict:
        return {"message": "Head"}



# @blp.route("/about_me/<int:item_id>")
# class AboutMe(MethodView):
#     def get(self, item_id: int) -> dict or abort(404):
#         try:
#             return about_me[item_id]
#         except KeyError:
#             abort(404, message="Item not found")
#
#

