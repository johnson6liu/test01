from . import index_blu

@index_blu.route("/")
def index():
    # redis_store.set("name", "python")

    # session["age"] = 28
    return "666"