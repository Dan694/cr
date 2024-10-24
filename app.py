from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = '5c02a8d8ba2312a73a6dc88cabc10589'
def six_digit_number(form, field):
    if not field.data.isdigit() or len(field.data) != 6:
        raise ValidationError("Число має бути 6-значним і позитивним")

class NumberForm(FlaskForm):
    name = StringField("Введіть 6-значне ціле число", validators=[
        DataRequired(), six_digit_number])
    submit = SubmitField("Submit")

@app.route('/vvod/', methods=['GET', 'POST'])
def vvod():
    form = NumberForm()

    if form.validate_on_submit():
        input = form.name.data
        input_str = str(input)
        if (int(input_str[0]) + int(input_str[1]) + int(input_str[2]) ==int(input_str[3]) + int(input_str[4]) + int(input_str[5])):
            return render_template("vivod_yes.jinja")
        else:
            return render_template("vivod_no.jinja")

    return render_template("vvod.jinja", form=form)