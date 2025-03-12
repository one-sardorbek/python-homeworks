from bs4 import BeautifulSoup
weather_html="""<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>"""

soup=BeautifulSoup(weather_html,"html.parser")
weathers=[]

days=soup.find_all("tr")
for day in days:
    weather=[]
    datas=day.find_all("td")
    for data in datas:
        weather.append(data.text) #storing all datas
    weathers.append(weather)#storing all datas
weathers.remove(weathers[0]) #to delete one empty list
#displaying datas
for weather in weathers:
    print(weather)
#Finding the highest temperature
temperatures=[]
for weather in weathers:
    weather[1]=weather[1].replace("°C","") #to make the temperatures integer
    temperatures.append(int(weather[1]))
print(max(temperatures))
#Finding the "Sunny" condition.
for weather in weathers:
    if weather[2]=="Sunny":
        print(weather)
#Calculating Average Temperature
average=sum(temperatures)/len(temperatures)
print(str(average)+" °C")
