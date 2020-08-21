from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Tu nerd')
root.geometry("450x90")



# https://www.airnow.gov
# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=3AA1F65C-2223-46F5-B56B-690331F0E4ED

#Create Zipcode Lookup Function

def zipLookup():
    #zipcode.get()
    #zipLabel = Label(root, text = zipcode.get())
    #zipLabel.grid(row = 1, column = 0, columnspan = 2)
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=5&API_KEY=3AA1F65C-2223-46F5-B56B-690331F0E4ED")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background = weather_color)
        myLabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 20), background = weather_color)
        myLabel.grid(row = 1, column = 0, columnspan = 2)

    except Exception as e: 
        api = "Error..."

zipcode = Entry(root)
zipcode.grid(row = 0, column = 0, stick = W+E+N+S)

zipButton = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipButton.grid(row = 0, column = 1, stick = W+E+N+S)

root.mainloop()