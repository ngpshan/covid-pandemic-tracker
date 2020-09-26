from django.shortcuts import render
import requests
#import pandas as pd
#import plotly.express as px


def index(request):
    response = requests.get('https://disease.sh/v3/covid-19/all?yesterday=true&allowNull=true')
    response_json = response.json()
    #print("Number of active cases:", response_json['active'])

    return render(request, "index.html", {
        'cases': response_json['cases'],
        'active': response_json['active'],
        'recovered': response_json['recovered'],
        'deaths': response_json['deaths']
                  })


def countrylist(request):
    countries = requests.get('https://disease.sh/v3/covid-19/countries?yesterday=true&sort=active&allowNull=true')
    countries_json = countries.json()
    #for info in countries_json:
    #    {'countriesjs' : info['country']}
    return render(request, "countries_list.html", {'countries_json':countries_json,
                                                   'range': range(1, 216)})



def lineplot(request):
    cline = requests.get('https://disease.sh/v3/covid-19/historical/all?lastdays=180')
    cline_json = cline.json()
    #for ele in cline_json['cases']:
    #    print(ele) # gets past 10 dates
#print ( list(cline_json['cases'].values() )) # list of cases values
#print( list(cline_json['cases'].keys() )) # list of past 10 dates

    context1 = {
        'casesval': list(cline_json['cases'].values()),
        'casesdate': list(cline_json['cases'].keys()),
    }

    return render(request, 'lineplot.html', context1)