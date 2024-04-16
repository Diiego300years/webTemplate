import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from api.database.models.items import about_me

# Blueprint in Flask Smorest would divide API in multiple segment
blp = Blueprint("about_me", __name__, description="Operations on about_me")


@blp.route("/about_me/<int:item_id>")
class AboutMe(MethodView):
    def get(self, item_id):
        try:
            return about_me[item_id]
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/about_me")
class AboutMeValues(MethodView):
    def get(self):
        return {"collected_data": list(about_me.values())}

