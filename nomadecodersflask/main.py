from flask import Flask, render_template, request, redirect

app = Flask("nomadecodersflask")


@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
  else:
    return redirect("/")
    
  print(word)
  return render_template("report.html", searchingBy=word, potato="mellow")

# @app.route("/contact")
# def contact():
#     return "Hello! Contact"


# @app.route("/<username>")
# def potato(username):
#     return f"Hello! your <h1>name</h1> is {username}"


app.run(host="0.0.0.0")
