from flask import Flask, render_template, request
from stories import story

app= Flask(__name__)

suggestions = {
    "Place": "Forest",
    "Noun": "Dragon",
    "Verb": "Eat",
    "Adjective": "Angry",
    "Plural_Noun": "Ogers" 
}

@app.route("/", methods=["GET", "POST"])
def ask_questions():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts, suggestions=suggestions)

@app.route("/story")
def show_story():
    answers = request.args
    text = story.generate(answers)
    return render_template("story.html", text=text)



        