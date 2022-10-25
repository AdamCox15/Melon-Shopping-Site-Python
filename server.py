from flask import Flask, render_template, redirect, flash, request
import jinja2

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def homepage():
    return render_template("base.html")

@app.route("/melons")
def melonsPage():
    melon_list = melons.get_all()   
    return render_template("melons.html", melon_list = melon_list)



@app.route("/melon/<melon_id>")
def individualMelons(melon_id):
    return render_template("individualMelon.html")

@app.route("/add_to_cart/<melon_id>")
def homepage(melon_id):
    return f"{melon_id} Added to cart" 

@app.route("/cart")
def cartPage():
    return render_template("cart.html")



if __name__ == "__main__":
    app.env = "development"
    app.run(debug= True, port= 8000, host= "localhost")

