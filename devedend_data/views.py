from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import requests
import re
#from devedend_data.models import data

# Create your views here.
#Home page
data = {'Nestle': ['Nestle', 'Final', '650.00', '16-02-2021', '-', '29-04-2021', 65.0, 0.40385212799005904], 'Castrol': ['Castrol', 'Final', '60.00', '01-02-2021', '-', '22-04-2021', 3.0, 2.34375], 'ABB India': ['ABB India', 'Final', '250.00', '10-02-2021', '-', '19-04-2021', 5.0, 0.328515111695138], 'Schaeffler Ind': ['Schaeffler Ind', 'Final', '380.00', '16-02-2021', '-', '19-04-2021', 38.0, 0.7331661200077175], 'Sanofi India': ['Sanofi India', 'Special', '2400.00', '24-02-2021', '-', '19-04-2021', 240.0, 2.956757422693113], 'ACC': ['ACC', 'Final', '140.00', '11-02-2021', '31-03-2021', '30-03-2021', 14.0, 0.7662835249042146], 'CRISIL': ['CRISIL', 'Final', '1400.00', '11-02-2021', '-', '30-03-2021', 14.0, 0.7223942208462333], 'Coal India': ['Coal India', 'Interim', '0.00', '23-02-2021', '16-03-2021', '15-03-2021', 0.0, 0.0]}


def home(request):
#     if('output' not in request.session.keys()):
#         data = {}
#         data= dividend()
#         request.session['output'] = data
#     else:
#         data = request.session.get('output')
    return render(request,'Home.html',{'Data':data})


#Data extraction
def dividend():
    html_tables = pd.read_html("https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php?sel_year=2021")
    df = html_tables[1]
    data = {}
    #company names
    key = df.T.values[0]
    #compny urls
    links = urls()
    count = 0
    for i in range(2,len(key)):
        l = []
        for j in range(len(df.T.values)):
            l.append(df.T.values[j][i])
        #if dividend is 0 than Dividend % FV and Dividend % MP is 0
        if(l[2] == '0.0'):
            l.append(0.0)
            l.append(0.0)
        else:
            try:
                dt = current_value('https://www.moneycontrol.com/india/stockpricequote'+links[i-2])
                c_v = dt.contents[1]['rel']
                f_v = dt.contents[0]
            except:
                c_v = 1
                f_v = 0
            l.append(d_fv(int(float(l[2])),int(float(f_v))))
            l.append(d_mp(int(float(c_v)),int(l[6])))

        data[key[i]] = l
    return data

#to fetch urls of every company
def urls():
    req = Request("https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php?sel_year=2021")
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    table = soup.find('table', 'b_12 dvdtbl')
    links = []
    for link in table.findAll('a'):
        links.append(link.get('href'))
    return links


#to extract current stock price and face value
def current_value(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    cv = soup.find('div', class_='inprice1 nsecp')
    fv = soup.find('td', class_='nsefv bsefv')
    fv.append(cv)
    return (fv)

#calculation of Dividend % (FV)
def d_fv(dv,fv):
    return (dv*fv)/100

#calculation of Dividend % (MP)
def d_mp(c_v,d_fv):
    return (d_fv*100)/c_v
