import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from api.database.models.items import stores

# Blueprint in Flask Smorest would divide API in multiple segment
blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"Message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON Payload"
            )

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"store already exists")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}

        stores[store_id] = store
        return store, 201