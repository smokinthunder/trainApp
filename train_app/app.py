# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
import pytesseract
import datetime
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_values(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from extract_values(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_values(item)
    else:
        yield data


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    with open('stations.json') as file:
        contents = file.read()

    data = json.loads(contents)

    values = list(extract_values(data))

    # print(type(values))

    return render_template('index.html', data1=values)


current_date = datetime.now().date()
current_date_string = current_date.strftime("%d-%m-%Y")


@app.route('/check_train', methods=['POST'])
def check_train_src_des():
    data_list = []
    from test import get_two_station_trains, get_three_station_trains
    from station_for_time import get_three_with_time_station_trains
    if request.method == 'POST':
        from_station = request.form.get('from')
        to_station = request.form.get('to')
        departure_date = current_date_string
        print(departure_date)
        middle_station = request.form.get('middle')
        additional_time = request.form.get('additional')
        buffer = request.form.get('buffer')
        if middle_station and not additional_time:
            recommended_train_details_three = get_three_station_trains(from_station, middle_station, to_station,
                                                                       departure_date)
            print(recommended_train_details_three, 'o' * 50)

            if type(recommended_train_details_three) is str:
                data = recommended_train_details_three
                print(data, '~' * 50)
                return render_template('index.html', train_details=data)

            else:
                for list_to_dict in recommended_train_details_three:
                    print(type(list_to_dict))
                    data = list_to_dict.to_dict('records')
                    data_list.append(data)

                env = Environment(loader=FileSystemLoader('templates'))

                # Load the template
                template = env.get_template('index.html')

                return render_template('index.html', train_details=data_list, type_of_data='list')
        elif middle_station and additional_time and buffer:
            recommended_train_details_three = get_three_with_time_station_trains(from_station, middle_station,
                                                                                 to_station,
                                                                                 departure_date, additional_time,
                                                                                 int(buffer))
            print(recommended_train_details_three, 'o' * 50)

            if type(recommended_train_details_three) is str:
                data = recommended_train_details_three
                print(data, '~' * 50)
                return render_template('index.html', train_details=data)

            else:
                for list_to_dict in recommended_train_details_three:
                    print(type(list_to_dict))
                    data = list_to_dict.to_dict('records')
                    data_list.append(data)

                env = Environment(loader=FileSystemLoader('templates'))

                # Load the template
                template = env.get_template('index.html')

                return render_template('index.html', train_details=data_list, type_of_data='list')
        else:
            recommended_train_details = get_two_station_trains(from_station, to_station, departure_date)
            print(recommended_train_details, 'o' * 50)

            if type(recommended_train_details) is str:
                data = recommended_train_details
                print(data, '~' * 50)
                return render_template('index.html', train_details=data)

            else:

                data = recommended_train_details.to_dict('records')
                return render_template('index.html', train_details=data)
    return render_template('index.html')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
