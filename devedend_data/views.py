from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import requests
import re


data = {'Nestle': ['Nestle', 'Final', '650.00', '16-02-2021', '-', '29-04-2021', 65.0, 0.40385212799005904], 'Castrol': ['Castrol', 'Final', '60.00', '01-02-2021', '-', '22-04-2021', 3.0, 2.34375], 'ABB India': ['ABB India', 'Final', '250.00', '10-02-2021', '-', '19-04-2021', 5.0, 0.328515111695138], 'Schaeffler Ind': ['Schaeffler Ind', 'Final', '380.00', '16-02-2021', '-', '19-04-2021', 38.0, 0.7331661200077175], 'Sanofi India': ['Sanofi India', 'Special', '2400.00', '24-02-2021', '-', '19-04-2021', 240.0, 2.956757422693113]}
#Home page
def home(request):
    return render(request,'Home.html',{'Data':data})



