from tkinter.constants import LEFT, RIGHT
import requests
import bs4
import tkinter as tk

def get_html_data(link):
  data=requests.get(link)
  return data

def get_covid_data():
  link="https://www.worldometers.info/coronavirus/"
  html_data=get_html_data(link)
  bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
  info_div = bs.find("div",class_="content-inner").findAll("div", id="maincounter-wrap")

  covid_data=""

  for i in range(3):
      text=info_div[i].find("h1",class_=None).get_text()
      count=info_div[i].find("span",class_=None).get_text()
      covid_data= covid_data+ text + " " + count +"\n"
  
  return covid_data


def get_country_data():
  country_name=textfield.get()
  link="https://www.worldometers.info/coronavirus/country/"+country_name

  html_data=get_html_data(link)
  bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
  info_div = bs.find("div",class_="content-inner").findAll("div", id="maincounter-wrap")

  covid_data=""
  try:
    for i in range(3):
      text=info_div[i].find("h1",class_=None).get_text()
      count=info_div[i].find("span",class_=None).get_text()
      covid_data= covid_data+ text + " " + count +"\n"
  except:
    print("")
   
  mainlabel['text']=covid_data

def reload():
  new_data= get_covid_data()
  mainlabel['text']=new_data


root=tk.Tk()
root.geometry("1024x720")
root.title("COVID-19 Tracker App")
f=("poppins",25,"bold")

banner=tk.PhotoImage(file="covid.png")
bannerlabel=tk.Label(root,image=banner)
bannerlabel.pack()

textfield=tk.Entry(root, width=50)
textfield.pack()


mainlabel=tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()

get_button= tk.Button(root, text="Click to Get Country Data", font=f, relief='solid', command=get_country_data)
get_button.pack(side = LEFT )

reload_button= tk.Button(root, text="Reload for Global Data", font=f, relief='solid', command=reload)
reload_button.pack(side = RIGHT )


root.mainloop()


