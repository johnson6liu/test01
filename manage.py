
from info import create_app

app = create_app()

@app.route("/")
def index():
    # redis_store.set("name", "python")

    # session["age"] = 28
    return "666"


if __name__ == '__main__':
    app.run()