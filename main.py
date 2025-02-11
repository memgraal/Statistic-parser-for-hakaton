from flask import Flask, request
from parse_statistics import parse_statistics_from_url
from add_data import add_data_to_db


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_page():
    stats = parse_statistics_from_url()
    
    if request.method == "GET":
        add_data_to_db(
            stats["Победы"]["Всего"], stats["Победы"]["Дома"], stats["Победы"]["В гостях"], stats["Победы"]["Серия"],
            stats["Поражения"]["Всего"], stats["Поражения"]["Дома"], stats["Поражения"]["В гостях"], stats["Поражения"]["Серия"]
        )
        return stats


if __name__ == "__main__":
    app.run(debug=True)
