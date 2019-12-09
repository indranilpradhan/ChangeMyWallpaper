#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request as ur
import bs4
import subprocess
import os
from datetime import datetime
from datetime import date

try:
    url = "https://darksky.net/forecast/17.455,78.35/ca12/en"
    req = ur.Request(url, headers={'User-Agent': 'Chrome/77.0.3865.120'})
    html = ur.urlopen(req).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    data=soup.find_all("span",{"class":"summary swap"})
    for i in data:
        l =[x for x in i.contents[0].split()]
    s=''
    for i in range(1,len(l)):
        s += l[i] + " "
    print(s)

    a = os.listdir(os.getcwd()+"/weather")

    now = datetime.now().time()

    now = str(now)[:2]
    now = int(now)
    today = date.today()
    
    if "Rain" in s:
        d = os.getcwd()+"/weather/rainy"
        b = os.listdir(d)
        print(b)
        if now >= 7 and now <= 10:
            file_path = d + "/"+b[0]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 10 and now <= 13:
            file_path = d + "/"+b[1]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 13 and now <= 16:
            file_path = d + "/"+b[2]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 16 and now <= 19:
            file_path = d + "/"+b[3]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 19 and now <= 22:
            file_path = d + "/"+b[0]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)

    elif "Wind" in s:
        d = os.getcwd()+"/weather/windy"
        b = os.listdir(d)
        print(b)
        if now >= 7 and now <= 10:
            file_path = d + "/"+b[0]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 10 and now <= 13:
            file_path = d + "/"+b[1]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 13 and now <= 16:
            file_path = d + "/"+b[2]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 16 and now <= 19:
            file_path = d + "/"+b[3]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 19 and now <= 22:
            file_path = d + "/"+b[1]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)

    elif ("Cloudy" or "Overcast") in s:
        d = os.getcwd()+"/weather/cloudy"
        b = os.listdir(d)
        print(b)
        print("cloudy")
        print(d)
        if now >= 7 and now <= 10:
            file_path = d + "/"+b[0]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 10 and now <= 13:
            file_path = d + "/"+b[1]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 13 and now <= 16:
            file_path = d + "/"+b[2]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 16 and now <= 19:
            file_path = d + "/"+b[3]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 19 and now <= 22:
            file_path = d + "/"+b[2]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)

    elif ("Sun" or "Clear") in s:
        d = os.getcwd()+"/weather/sunny"
        b = os.listdir(d)
        print(b)
        if now >= 7 and now <= 10:
            file_path = d + "/"+b[0]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 10 and now <= 13:
            file_path = d + "/"+b[1]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 13 and now <= 16:
            file_path = d + "/"+b[2]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 16 and now <= 19:
            file_path = d + "/"+b[3]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
        elif now > 19 and now <= 22:
            file_path = d + "/"+b[3]
            command = "gsettings set org.gnome.desktop.background picture-uri 'file://%s'"%(file_path)
            status, output = subprocess.getstatusoutput(command)
except IOError:
    print("Unable to make connection")

