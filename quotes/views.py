from django.shortcuts import render, redirect
from .models import Stock               # import from models (the name of the model you want to import)
from .forms import StockForm
from django.contrib import messages     # The messages in this file were utilized in base.html

def home(request):
    # API_KEY for iex cloud for pk_d498d40ec96e4e1d8bb7a6e68424254d
    # steps to using API: 1. connect 2. bring data back to app 3. parse it 4. do something with it
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST[ 'ticker' ]   # this is the name of the input in the base.html file
        # WORKING WITH THE API KEY
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")   # Pass in the ticker from the input in the base.html page

        try:
            api = json.loads(api_request.content)       # Parsing the data that is stored in the api_request
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', { 'api': api })     #create a function request the page/file we want to render then pass in a dictionary. The dictionary allows us to pass data to the homepage 

    else:
        return render( request, 'home.html', { 'ticker': "Enter a Ticker Symbol Above..." });   # If there is nothing posted return the following on home page


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    # Add STOCK TO THE DATA BASE        Unlike home which used a regular form this will use DJANGO FORM
    if request.method == 'POST':
        form = StockForm(request.POST or None)      # Created a form variable and a form needs to be created in forms.py

        if form.is_valid():     # Checks the form above for validity
            form.save()             # If valid save it
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')


    else:
        # GET/PULL DATA FROM THE DATABASE
        ticker = Stock.objects.all()        # Stock is the name of our model in models.py
        # CREATE a python list to hold each piece of information
        output = []

        # CONNECTING OUR DATABASE OBJECT PULLED TO FORM (add_stock.html) WITH OUR API KEY TO DISPLAY NEEDED INFO
        for ticker_item in ticker:      #converting ticker to ticker_item
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")   # Changed the ticker to ticker_item and wrapped in a string because we are pulling these items from our database
            try:
                api = json.loads(api_request.content)       # Parsing the data that is stored in the api_request
                output.append(api)  #Adding api to the list above (output)
            except Exception as e:
                api = "Error..."


        return render(request, 'add_stock.html', { 'ticker': ticker, 'output': output })        # Now pass output to the add_stock page as well


# PAGE FOR THE DELETING ACTION
def delete_stock(request):
    ticker = Stock.objects.all()       # Stock is the name of our model in models.py
    return render(request, 'delete_stock.html', { 'ticker': ticker })


# DELETING AN ITEM FROM THE DATABASE
def delete(request, stock_id):      # Passing in the stock_id which will be the id #
    item = Stock.objects.get(pk=stock_id)       # We want to grab an item from the model we created and we want to get the (primarykey=stock_id) or id number
    item.delete()                   # Call to delete the item
    messages.success(request, ('Stock Has Been Deleted!'))
    return redirect('delete_stock')

