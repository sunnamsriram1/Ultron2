#!/usr/bin/python
import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime as dt
from datetime import date, timedelta
import pywhatkit as kit
import wikipedia as wiki
import webbrowser as wb
from plyer import notification
from bs4 import BeautifulSoup
import requests
import pyjokes
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import calendar
from tkinter import *
from collections import namedtuple
from lxml import html

listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate

speaker.setProperty('rate', 150)     # setting up new voice rate

def make_request(url):
  response = requests.get(url)
  return response.text

def speak(text):
    speaker.say('Yes Sir, ' + text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

def speak_ex1(text):
    speaker.say(text)
    speaker.runAndWait()


def wishMe():
    speak("Welcome back!")
    print(" ")
    hour = int(dt.datetime.now().hour)

    year = int(dt.datetime.now().year)
    month =(dt.datetime.now().strftime("%B-%m"))
    date = int(dt.datetime.now().day)
    Time = dt.datetime.now().strftime("%I:%M:%S %p")

    print("This Hour", hour)
    speak_ex("This hour is")
    speak_ex(hour)

    print("This Time Now", Time)
    speak_ex("the current Time Now is")
    speak_ex(Time)

    print("Today Date", date)
    speak_ex("Sir Today Date is")
    speak_ex(date)

    print("This Month", month )
    speak_ex("the current month is")
    speak_ex(month)


    print("This Year", year)
    speak_ex("the current year is")
    speak_ex(year)
    if hour >= 6 and hour < 12:
        speak_ex("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak_ex("Good Afternoon!")

    elif hour >= 18 and hour < 24:
        speak_ex("Good Evening!")

    else:
        speak_ex("Good Night!")

    speak_ex("Ultron at your service! Please tell me how can I help you? Sir")


wishMe()



#va_name = "Jarvis"
#va_name = 'Alex'
#va_name = "Sriram"
#va_name = "John"
va_name = "Ultron"
#va_name = "BoyBot"
#va_name = "Jupiter"
#va_name = "Kingston"
#va_name = "Ryan"
#va_name = "Albatross"

#speak_ex('I am Your ' + va_name + ', Tell me Sir.')

speak_ex('My Name is ' + va_name + 'I am your Assistant')

def take_command():
      command = ' '
      try:
          with sr.Microphone() as source:
              print('Listening.....')
              print(' ')
              voice = listener.listen(source)
              command = listener.recognize_google(voice)
              command = command.lower()
              if va_name in command:
                  command = command.replace(va_name + ' ', '')
                  #print(command)
                  #speak(command)
      except:
          #print('Check Your Microphone')
          print("How can i Help you, Sir")
          print(' ')
      return command

while True:

    user_command = take_command()
    #print(user_command)
    #speak(user_command)


    if 'close' in user_command:
        print('See You Again Boss. I Will be There when ever you call me. ')
        speak('See You Again Boss. I Will be There when ever you call me. ')
        break
    if "joke" in user_command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    if 'google' in user_command:
        speak('Okey! Openning google')
        wb.open('www.google.co.in')
        speak('google has been opened')
    if'sprogram' in user_command:
        speak('Okey! Opening sprogram ')
        url = 's program001'
        wb.open(url)
    if'website html code' in user_command or 'html code' in user_command:
        while True:
            print(" ")
            speak_ex('Enter a Your Website in https&http Sir')
            html = input('Enter A Your WebSite Https:// :  ')


            x = requests.get(html, timeout=1.50, params={"model": "Mustang"})
            print(" ")
            print("Status_Code", x.status_code)
            speak_ex(f" Sir Status_Code {x.status_code}")
            print(" ")
            print(x.text)
            break

    if 'instagram' in user_command:
        speak('opening instagram Sir!')
        #self.compText.set('opening instagram Sir!')
        wb.open('www.instagram.com')
    if 'whatsapp' in user_command:
        speak('Opening whatsapp Sir')
        #self.compText.set('opening whatsapp Sir')
        wb.open('www.whatsapp.com')
    if 'youtube' in user_command:
        speak('Opening Youtube Sir')
        wb.open('www.youtube.com')


    if 'calculator' in user_command:
        speak("Select Operation")
        # print("Select operation.")
        # print("1.Add")


        # Program make a simple calculator

        # This function adds two numbers
        def add(x, y):
            return x + y


        # This function subtracts two numbers
        def subtract(x, y):
            return x - y


        # This function multiplies two numbers
        def multiply(x, y):
            return x * y


        # This function divides two numbers
        def divide(x, y):
            return x / y


        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
            # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                    speak_ex("Answer")
                    speak_ex(add(num1, num2))


                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                    speak_ex("Answer")
                    speak_ex(subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                    speak_ex("Answer")
                    speak_ex(multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                    speak_ex("Answer")
                    speak_ex(divide(num1, num2))
                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input("Let's do next (Enter)(Exit to 0): ")
                speak_ex('Let s do  Enter to exit to 0')
                if next_calculation == "no":
                    break

            else:
                print("Invalid Input")
                break




    if 'adding' in user_command:
        speak("Enter first number: ")
        num1 = float(input("Enter first number: "))
        speak("Enter second number: ")
        num2 = float(input("Enter second number: "))
        add = (num1 + num2)
        speak_ex(add)
        print(add)


    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M:%S:%fSeconds %p")
        print(cur_time)
        speak(cur_time)
        #speak(cur_time)
        speak_ex('show me calender')
        user_command = take_command()
        if'calender' in user_command or 'yes' in user_command or 'show me' in user_command:

            # Function for showing the calendar of the given year
            def showCal():
                # Create a GUI window
                new_gui = Tk()

                # Set the background colour of GUI window
                new_gui.config(background="white")

                # set the name of tkinter GUI window
                new_gui.title("CALENDAR")

                # Set the configuration of GUI window
                new_gui.geometry("550x600")

                # get method returns current text as string
                fetch_year = int(year_field.get())

                # calendar method of calendar module return
                # the calendar of the given year .
                cal_content = calendar.calendar(fetch_year)

                # Create a label for showing the content of the calendar
                cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

                # grid method is used for placing
                # the widgets at respective positions
                # in table like structure.
                cal_year.grid(row=5, column=1, padx=20)

                # start the GUI
                new_gui.mainloop()


            # Driver Code
            if __name__ == "__main__":
                # Create a GUI window
                gui = Tk()

                # Set the background colour of GUI window
                gui.config(background="white")

                # set the name of tkinter GUI window
                gui.title("CALENDAR")

                # Set the configuration of GUI window
                gui.geometry("250x140")

                # Create a CALENDAR : label with specified font and size
                cal = Label(gui, text="CALENDAR", bg="dark gray",
                            font=("times", 28, 'bold'))

                # Create a Enter Year : label
                year = Label(gui, text="Enter Year", bg="light green")

                # Create a text entry box for filling or typing the information.
                year_field = Entry(gui)

                # Create a Show Calendar Button and attached to showCal function
                Show = Button(gui, text="Show Calendar", fg="Black",
                              bg="Red", command=showCal)

                # Create a Exit Button and attached to exit function
                Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

                # grid method is used for placing
                # the widgets at respective positions
                # in table like structure.
                cal.grid(row=1, column=1)

                year.grid(row=2, column=1)

                year_field.grid(row=3, column=1)

                Show.grid(row=4, column=1)

                Exit.grid(row=6, column=1)

                # start the GUI
                gui.mainloop()

        htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
        print(htmlcal.formatmonth(2020, 12))
    elif'village address details' in user_command:
        speak_ex('Enter Your City and Village Name Sir')
        v = input('Enter Village Name: ')
        geolocator = Nominatim(user_agent="Sriram")
        location = geolocator.geocode(v)
        speak_ex('Showing Your Village address ')
        print(location)
        speak_ex(location)
        speak_ex("Your Location Latitude Sir")
        print((location.latitude, location.longitude))
        speak_ex(location.latitude)
        speak_ex(location.longitude)
        print(location.raw)
        speak_ex(location.raw)




    elif'pin code' in user_command:
        speak_ex('given A Pin code find the details')
        speak_ex('Enter Your Pincode')
        z = input('Enter Your Pincode: ')
        geolocator = Nominatim(user_agent="Sriram")
        print("\nYour Pin_code:", z)
        location = geolocator.geocode(z)
        print(location)
        speak_ex(location)






    elif 'date' in user_command:
        cur_date = dt.datetime.now().strftime("%d-%m-%Y,%A")
        print(cur_date)
        speak(cur_date)
        #print("Current date and time: ", dt.datetime.now())
        speak_ex('Show Me Date Time formats, Sir')
        user_command = take_command()
        if 'yes' in user_command or 'no' in user_command or 'show' in user_command or 'show me' in user_command:
             # print('Yes or No!')
             # speak_ex("Yes or No")
             print(" ")
             speak_ex("Ok Showing Date Time formats, Sir")
             dt1 = dt.date.today().strftime("%Y")
             print("Current year: ", dt1)
             speak_ex('Current year')
             speak_ex(dt1)
             dt2 = dt.date.today().strftime("%B")
             print("Month of year: ", dt2)
             speak_ex('Month of year')
             speak_ex(dt2)
             dt3 = dt.date.today().strftime("%W")
             print("Week number of the year: ", dt3)
             speak_ex('Week number of the year')
             speak_ex(dt3)
             dt4 = dt.date.today().strftime("%w")
             print("Weekday of the week: ", dt4)
             speak_ex('Week of th week')
             speak_ex(dt4)
             dt5 = dt.date.today().strftime("%j")
             print("Day of year: ", dt5)
             speak_ex('Day of year')
             speak_ex(dt5)
             dt6 = dt.date.today().strftime("%d")
             print("Day of the month : ", dt6)
             speak_ex('Day of the month')
             speak_ex(dt6)
             dt7 = dt.date.today().strftime("%A")
             print("Day of week: ", dt7)
             speak_ex('Day of Week')
             speak_ex(dt7)
             # speak_ex('subtract five days from current date Sir')
             # user_command = take_command()
             # if 'ok' in user_command or 'yes' in user_command or 'show' in user_command or 'show me' in user_command:
             #     dt = date.today() - timedelta(5)
             #     print('Current Date :', date.today())
             #     print('5 days before Current Date :', dt)

        # else:
        #     print('Yes or No!')
        #     speak_ex("Yes or No")
        # speak_ex('fCurrent year {dt1}\n Month of year  ')
    elif'show date time formats' in user_command or 'date time formats' in user_command:
            print(" ")
            speak_ex("Showing Date Time formats, Sir")
            dt1 = dt.date.today().strftime("%Y")
            print("Current year: ", dt1)
            speak_ex('Current year')
            speak_ex(dt1)

            dt2 = dt.date.today().strftime("%B")
            print("Month of year: ", dt2)
            speak_ex('Month of year')
            speak_ex(dt2)

            dt3 = dt.date.today().strftime("%W")
            print("Week number of the year: ", dt3)
            speak_ex('Week number of the year')
            speak_ex(dt3)

            dt4 = dt.date.today().strftime("%w")
            print("Weekday of the week: ", dt4)
            speak_ex('Week of th week')
            speak_ex(dt4)

            dt5 = dt.date.today().strftime("%j")
            print("Day of year: ", dt5)
            speak_ex('Day of year')
            speak_ex(dt5)

            dt6 = dt.date.today().strftime("%d")
            print("Day of the month : ", dt6)
            speak_ex('Day of the month')
            speak_ex(dt6)

            dt7 = dt.date.today().strftime("%A")
            print("Day of week: ", dt7)
            speak_ex('Day of Week')
            speak_ex(dt7)

    elif 'year' in user_command:
        cur_year = dt.datetime.now().strftime("%Y")
        print(cur_year)
        speak(cur_year)
    elif "i love you" in user_command:
        speak("It's hard to understand")
    elif 'how are you' in user_command:
        speak("I am fine, Thank you")
        speak_ex("How are you, Sir")
    elif 'good morning' in user_command:
        speak_ex("Have a Good Day Sir")
        speak_ex("How are you Sir.")
        speak_ex("What are you doing today work")
    elif 'nothing' in user_command:
        speak_ex("How are you Friends Sir.")
        # print(speak)
    elif 'my friends all happy' in user_command:
        speak_ex("Life is incomplete without friends and so, this occasion provides us with just the right chance to express our gratitude and thanks to our friends who have always been there for us, in good and bad times")
    elif 'thank you' in user_command:
        speak_ex("its ok don't worry Sir")

    elif 'what are you doing' in user_command:
        speak_ex("Nothing Sir.")
        speak_ex("You Sir.")
    elif 'i am fine' in user_command:
        speak_ex("Welcome to My World, Sir")
    elif 'fine' in user_command:
        speak_ex("ok Sir.")
    elif "who i am" in user_command:
        speak("If you talk then definitely your human.")
        print(speak)

    elif "why you came to world" in user_command:
        speak("Thanks to Gaurav. further It's a secret")

    elif 'is love' in user_command:
        speak("It is 7th sense that destroy all other senses")

    elif 'reason for you' in user_command:
        speak("I was created as a Minor project by Mister Gaurav ")

    elif 'open stackoverflow' in user_command:
        speak("Here you go to Stack Over flow.Happy coding")
        wb.open("stackoverflow.com")

    elif "don't listen" in user_command or "stop listening" in user_command:
        speak("for how much time you want to stop jarvis from listening")

    elif "write a note" in user_command:
        speak("What should i write, sir")
        note = take_command()
        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        user_command = take_command()
        if 'yes' in user_command or 'sure' in user_command:
            strTime = dt.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
    elif "show note" in user_command:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())
        speak(file.read(6))

    elif "update assistant" in user_command:
       speak_ex("After downloading file please replace this file with the downloaded one")
    #
    # elif 'play' in user_command:
    #     user_command = user_command.replace('play ', ' ')
    #     print('Playing ' + user_command)
    #     speak('Playing ' + user_command + ', Enjoy Boss.')
    #     kit.playonyt(user_command)
    #     #kit.playonyt("PyWhatKit")
    #     break
    # elif 'search for' in user_command or 'google' in user_command:
    #     user_command = user_command.replace('search for ', ' ')
    #     user_command = user_command.replace('google ', ' ')
    #     speak('Searching for ' + user_command)
    #     kit.search(user_command)
    elif 'who is' in user_command or 'what is' in user_command:
        user_command = user_command.replace('who is ', ' ')
        user_command = user_command.replace('what is ', ' ')
        user_command = user_command.replace('tell me', ' ')
        info = wiki.summary(user_command, 3)
        #wiki.set_lang("te")
        i = wiki.search(user_command)
        w = wiki.page(user_command)
        print(i)
        speak_ex(i)
        print(w)
        print(w)
        speak_ex(w)
        print(info)
        speak(info)
    elif 'files reading' in user_command or 'read files' in user_command:
        speak_ex('Enter File Name Extension Sir')
        filename = input('Enter File Name Extension: ')

        # filename = filename +  '.txt'
        # pdf_book = open(filename, 'rb')
        f = open(filename, "r")
        print(f.read())
        speak_ex(f.read())
        f.close()

    elif'create file' in user_command:
        speak_ex('Enter A Content Sir')
        file = input("Enter A Content: ")

        f = open("demofile3.txt", "a")
        f.write(file)
        #f.close()
        speak_ex("Show me Text file Sir,")
        user_command = take_command()
        if 'yes' in user_command or 'sure' in user_command:
            f = open("demofile3.txt", "r")
            print(f.read())
            speak(f.read())

    elif'talk friend' in user_command:

        vtf = pyttsx3.init()

        rate = vtf.getProperty('rate')
        vtf.setProperty('rate', 160)


        def vtf_speak(text):
            print('Speaking.......')
            print(' ')
            vtf.say(text)
            vtf.runAndWait()


        x = input('Enter A Text: ')
        # #txt = "Hey,  I am Your Virtual Taking Friend  Hello Wrold"
        # txt = " Welcome back sir  i am Jarvis"
        # #txt = "Welcome. It’s Good to have you back Sir. "
        # #txt = "Hello, I'm one of the voices you can use to speech enable any content, for websites, documents, devices, applications, and more. When I read your text, it sounds like this."
        vtf_speak(x)

        while x != 'bye':
            x = input('What Should I Say (Bye to Exit): ')
            print(' ')
            x = x.lower()
            if x != 'bye':
                vtf_speak(x)
            else:
                vtf_speak('See You again Friend, that was Nice Talking to You')

    elif 'who are you' in user_command:
        speak_ex('My Name is ' + va_name + 'I am your Assistant')
        speak_ex("Tell me Sir.")


    elif 'my location' in user_command:
        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        speak_ex('Your Location  Details ')
        print('Ip Address :', ip_add)
        print('City_Name :', city)
        print('State :', state)
        print('Country :', country)
        speak_ex(f'Ip Address  {ip_add}\n City_Name  {city}\n State {state}\n Country {country}')
        # print('Ip Address =', ip_add)
        # speak_ex('You Are ip address')
        # speak_ex(ip_add)
        #
        # print('City_Name =', city)
        # speak_ex('city name')
        # speak_ex(city)
        #
        # print('State =', state)
        # speak_ex('state')
        # speak_ex(state)
        #
        # print('Country =', country)
        # speak_ex('country')
        # speak_ex(country)
        #



    # elif "today weather" in user_command:
    #
    #     # Google Open weather website
    #     # to get API of Open weather
    #     api_key = "pro.openweathermap.org/data/2.5/forecast/hourly?q="
    #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #     speak(" City name ")
    #     print("City name : ")
    #     city_name = take_command()
    #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    #     response = requests.get(complete_url)
    #     x = response.json()
    #
    #     if x["cod"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_pressure = y["pressure"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #         print(" Temperature (in kelvin unit) = " + str(
    #             current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
    #             current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
    #             weather_description))
    #
    #     else:
    #         speak(" Sorry Sir, I couldn't find the city in my database. Please try again City Not Found ")


        #return city, state, country

    elif 'today news' in user_command:
        url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
        news = requests.get(url).text
        news_dict = json.loads(news)
        articles = news_dict['articles']
        speak_ex(articles)
        speak_ex(news)
    # elif 'calculater' in user_command:
    #     url = 'https://www.calculatorsoup.com/calculators/math/basic.php'
    #     print(url)
    #     speak(url)
    elif 'today bbc news' in user_command:
        _NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


        def fetch_bbc_news(bbc_news_api_key: str) -> None:
            # fetching a list of articles in json format
            bbc_news_page = requests.get(_NEWS_API + bbc_news_api_key).json()
            # each article in the list is a dict
            for i, article in enumerate(bbc_news_page["articles"], 1):
                print(" ")
                print(f"{i}.) {article['title']}")
                speak_ex(f"{i}.) {article['title']}")
                # speak({i}.) {article['title']})


        if __name__ == "__main__":
            fetch_bbc_news(bbc_news_api_key="718b1a4a84614ca29a61e2e17ab9a554")




    elif 'covid-19' in user_command:
        covid_data = namedtuple("covid_data", "cases deaths recovered")


        def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> covid_data:
            xpath_str = '//div[@class = "maincounter-number"]/span/text()'
            return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))


        fmt = """\nTotal COVID-19 cases in the world: {}
                \nTotal Deaths due to COVID-19 in the world: {}
                \nTotal COVID-19 patients recovered in the world: {}"""
        print(fmt.format(*covid_stats()))
        speak_ex(fmt.format(*covid_stats()))

      # html_data = make_request('https://www.worldometers.info/coronavirus/')
      # #print(html_data)
      # soup = BeautifulSoup(html_data, 'html.parser')
      # total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
      # total_cases = total_global_row.find_all('td')[2].get_text()
      # new_cases = total_global_row.find_all('td')[3].get_text()
      # total_recovered = total_global_row.find_all('td')[6].get_text()
      # print('total cases : ', total_cases)
      # print('new cases', new_cases[1:])
      # print('total recovered', total_recovered)
      # notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
      # speak(notification_message)
      # speak_ex1(notification.notify)
      # notification.notify(
      #   title="COVID-19 Statistics",
      #   message=notification_message,
      #   timeout=10
      # )
      # speak("here are the stats for COVID-19")

    elif "today weather" in user_command:
        # APPID = "f12144836b4149c3a144836b4169c3ae"  # <-- Put your OpenWeatherMap appid here!
        # agromonitoring APPID = "4a1543035ae2af10c9f36ff2e1457fc4"
        APPID = "591a35045c6de641dae242c118676369"
        URL_BASE = "http://api.openweathermap.org/data/2.5/"


        # URL_BASE = "https://www.agromonitoring.com"
        # URL_BASE = "https://www.wunderground.com"
        def current_weather(q: str = "", appid: str = APPID) -> dict:
            """https://openweathermap.org/api"""
            return requests.get(URL_BASE + "weather", params=locals()).json()


        def weather_forecast(q: str = "", appid: str = APPID) -> dict:
            """https://openweathermap.org/forecast5"""
            return requests.get(URL_BASE + "forecast", params=locals()).json()


        def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
            """https://openweathermap.org/api/one-call-api"""
            return requests.get(URL_BASE + "onecall", params=locals()).json()


        if __name__ == "__main__":
            from pprint import pprint

            while True:
                location = input("Input a location: ").strip()
                if location:
                    print(current_weather(location))
                    speak_ex(current_weather(location))
                    break
                else:
                    break


        # # Google Open weather website
        # # to get API of Open weather
        # api_key = "591a35045c6de641dae242c118676369"
        # base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        # speak(" City name ")
        #
        # print("City name : ")
        # city_name = take_command()
        # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        # response = requests.get(complete_url)
        # x = response.json()
        #
        # if x["cod"] != "404":
        #     y = x["main"]
        #     current_temperature = y["temp"]
        #     current_pressure = y["pressure"]
        #     current_humidiy = y["humidity"]
        #     z = x["weather"]
        #     weather_description = z[0]["description"]
        #     print(" Temperature (in kelvin unit) = " + str(
        #         current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
        #         current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
        #         weather_description))
        #
        # else:
        #     speak(" Sorry Sir, I couldn't find the city in my database. Please try again City Not Found ")


    else:
      #speak_ex('Please Say it Again Boss.')
      speak_ex("How can i Help you, Sir")
