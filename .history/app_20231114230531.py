from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    job_description = request.form["job_description"]
    person_info, profile_pic_url = ice_break(name=name, job_description = job_description)
    print(job_description)
    print(person_info.summary)
    print( person_info.topic_of_interest)
    print( person_info.facts)
    print( person_info.ice_breaker)
    print(profile_pic_url)

    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topic_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breaker,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
