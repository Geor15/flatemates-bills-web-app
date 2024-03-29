from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        return render_template("bill_form_page.html")


class ResultsPage(MethodView):
    def get(self):
        return render_template("results.html")


class BillForm(Form):
    pass


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))

app.add_url_rule("/bill-form", view_func=BillFormPage.as_view("bill_form_page"))

app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))

if __name__ == "__main__":
    app.run()
