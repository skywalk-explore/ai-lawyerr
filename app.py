from flask import Flask, request, render_template, redirect, url_for
from appfiles import urlDictionary
from appfiles import PrivateHousingRentAdvice
from appfiles import Section21EvictionAdvice
from appfiles import Section8EvictionAdvice


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/help', methods=['GET', 'POST'])
def iNeedHelpWith():
    if request.method == 'POST':
        # getting formData selection from help.html page
        formData = request.form.get('I Need Help With')
        # the formData text is a key within the dictionary below that links to a link.
        return redirect(url_for(urlDictionary[formData]))
    if request.method == 'GET':
        return render_template('help.html')

@app.route('/privateHousingRentAdvice', methods=['GET', 'POST'])
def privateHousingRentAdvice():
    if request.method == 'POST':
        # collecting form data p.h.r.a template in dictionary format
        formData = request.form.to_dict()
        # passing the dict to p.h.r.a class instance
        instance = PrivateHousingRentAdvice(formData=formData)
        # calling the method within the class which calls all the methods within the class
        instance.callMethods()
        # passing instance.advice and instance.title to jinja2 template
        return render_template('advice.html', title=instance.title, advice=instance.advice)
    if request.method == 'GET':
        # redirected to this url from the /help page selection.
        return render_template('privateHousingRentAdvice.html')

@app.route('/section21EvictionAdvice', methods=['GET', 'POST'])
def section21EvictionAdvice():
    if request.method == 'POST':
        formData = request.form.to_dict()
        instance = Section21EvictionAdvice(formData=formData)
        instance.callMethods()
        return render_template('advice.html', title=instance.title, advice=instance.advice)
    if request.method == 'GET':
        return render_template('section21EvictionAdvice.html')

@app.route('/section8EvictionAdvice', methods=['GET', 'POST'] )
def section8EvictionAdvice():
    if request.method == 'POST':
        formData = request.form.to_dict()
        instance = Section8EvictionAdvice(formData=formData)
        instance.callMethods()
        return render_template('advice.html', title=instance.title, advice=instance.advice)
    if request.method == 'GET':
        return  render_template('section8EvictionAdvice.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)


