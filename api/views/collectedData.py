import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from api.database.models.items import collected_data

# Blueprint in Flask Smorest would divide API in multiple segment
blp = Blueprint("clientsData", __name__, description="Operations on collected_data")


@blp.route("/clients_data/<int:collected_data_id>")
class CollectedData(MethodView):
    def get(self, collected_data_id):
        try:
            return collected_data[collected_data_id]
        except KeyError:
            abort(404, message="collected_data not found")

    def delete(self, collected_data_id):
        try:
            del collected_data[collected_data_id]
            return {"Message": "collected_data deleted"}
        except KeyError:
            abort(404, message="collected_data not found")


@blp.route("/clients_data")
class CollectedDataList(MethodView):
    def get(self):
        return {"collected_data": list(collected_data.values())}

    def post(self):
        post_data = request.get_json()
        if "name" not in post_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON Payload"
            )
        for clients_data in collected_data.values():
            if post_data["name"] == clients_data["name"]:
                abort(400, message=f"collected_data already exists")

        collected_data_id = uuid.uuid4().hex

        clients_data = {**post_data, "id": collected_data_id}
        collected_data[collected_data_id] = clients_data
        return collected_data, 201