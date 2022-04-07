import PySimpleGUI as sg
import requests
import json
import webbrowser


#Theme
sg.change_look_and_feel('GreenTan') 


api_key = 'NASA API key here.'
url = 'https://api.nasa.gov/planetary/apod'


layout = [ [sg.Text('Date in YYYY-MM-DD:'), sg.Input(key='date', size=(15,1))],
            [sg.Button('Ok')] ]

window = sg.Window('Nasa APOD', layout)
while True:
    event, values = window.read()
    params={
    'api_key': api_key,
    'hd':'True',
    'date': values['date']
}

    response = requests.get(url,params=params)
    print(response)
    json = json.loads(response.text)
    image_url = json['hdurl']
    webbrowser.open(image_url)

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
window.close()