import math 
import glob
import json

weather_dir = 'weather/'
weather_files = glob.glob( weather_dir + '*.json')

weather_json = ''

weather_unit = ''

# Default loading screen
def init():
    print("")
    print("Choose the unit of temperature you want to see:")
    print("")
    print("1. Metric")
    print("--- Celcius, Metre, Kilometre etc ")
    print("2. Imperial")
    print("--- Fahrenheit, Yards, Miles etc ")
    print("")
    get_unit()

def user_init():
    print("")
    print("Welcome to: ")
    print("Weather Information System")
    print("")
    print("Before you show you the weather, we have you cover some how-to's")
    print("")
    print("In all menus, you would select the option with the number on the left")
    print("")
    print("E.g. 1. Show Weather")
    print("")
    print("Typing '1' would show you the weather")
    print("")
    print("Any boxes where it is waiting for you will show '>>> ' to indicate an input" )
    print("")
    print("Now let's get started!")
    print("")
    accept_terms()

def accept_terms():
    accepted = False

    while not accepted:
        print("Type in any character to continue")
        user_input = input(">>> ")

        if user_input != '':
            accepted = True
            init()
        else: 
            accept_terms()

def menu():
    index_val = 1

    print("")
    print("Welcome to: ")
    print("Weather Information System")
    print("")
    print("Please select an option")
    print("1. Get current weather")
    print("2. Change unit")
    print("3. Exit")
    print("")
    validate_menu()

def validate_menu():
    valid_choice = False
    
    print("Enter your choice ")
    choice = int(input(">>> "))
    while not valid_choice:
        try:
            match choice:
                case 1:
                    sub_menu()
                    valid_choice = True
                case 2:
                    init()
                    valid_choice = True
                case 3:
                    valid_choice = True
                    print("Exiting the program...")
                    break
                case _:
                    print("Incorrect choice, please try again")
                    validate_menu()
        except ValueError:
            print("Invalid input. Please enter a number.")
            validate_menu()
        except:
            print("An unexpected error occurred.")
            validate_menu()
    print("")

# Default Main Menu  
def sub_menu():
    print("")
    print("As this is an Alpha build, very few places are added to our database")
    index_val = 1 
    for weather_file in weather_files:
        filepath = weather_file

        with open( filepath, 'r' ) as file:
            data = json.load( file )
        
        for key, value in data.items():
            if key == 'name':
                print(f"{index_val}. {value}")
                index_val += 1
    print("")
    manage_user()

def manage_user():
    invalid_input = False

    print("Enter your choice ")
    choice = int( input(">>> ") )

    while not invalid_input:
        try:
            if choice in range( 1, len( weather_files ) + 1):
               invalid_input = True
               get_weather( weather_files[choice - 1 ] )
            else:
                print("Incorrect choice, please try again")
                manage_user()
        except ValueError:
            print("Invalid input. Please enter a number.")
            manage_user()
        except:
            print("An unexpected error occurred.")
            manage_user()

def get_weather( data ):
    choice = 1 
    global weather_json

    open_file( data )

    print("")
    print("Weather Information for: ")
    print(f"----- {weather_json['name']} -----")

    for key, value in weather_json.items():
        if key == 'weather':
            print("")
            print("> Weather Overview")
            print("")
            for sub_value in value:
                print(f"Overview: {sub_value['main']}")
                print(f"Description: {sub_value['description']}")
        elif key == 'main':
            print("")
            print("> Temperature")
            print("")
            for sub_key, sub_value in value.items():
                if sub_key == 'temp':
                    
                    print(f"Temperature: {convert_kelvin(sub_value)}")
                elif sub_key == 'feels_like':
                    print(f"Feels Like Temperature: {convert_kelvin(sub_value)}")
                elif sub_key == 'temp_min':
                    print(f"Minimum Temperature: {convert_kelvin(sub_value)}")
                elif sub_key == 'temp_max':
                    print(f"Maximum Temperature: {convert_kelvin(sub_value)}")
                elif sub_key == 'humidity':
                    print("")
                    print("> Humidity")
                    print("")
                    print(f"Humidity: {sub_value} %")
        elif key == 'wind':
            print("")
            print("> Wind")
            print("")
            for sub_key, sub_value in value.items():
                if sub_key == 'speed':
                    print(f"Wind Speed: {convert_speed(sub_value)}")
                elif sub_key == 'deg':
                    print(f"Wind Degree: {sub_value} °")
                    # print( sub_value['id'])

    print("")
    print("Returning to the main menu")
    print("")
    menu()

def convert_kelvin( data ):
    global weather_unit

    print(f"The weather unit is {weather_unit}")

    if weather_unit == 'metric':
        return "{:.2f}".format(data - 273.15) + ' °C'
    elif weather_unit == 'imperial':
        return "{:.2f}".format(( data - 273.15) * 1.8 + 32) + ' °F'

def convert_speed ( data ) :
    global weather_unit

    if weather_unit == 'metric':
        return "{:.2f}".format(data * 3.6) +' KM/H'
    elif weather_unit == 'imperial':
        return "{:.2f}".format(data * 2.236934) +' MP/H'
    
def get_unit():
    global weather_unit
    select_valid_unit = False

    print("Please choose a unit")
    choice = input(">>> ")

    while not select_valid_unit:
        match choice:
            case '1':
                weather_unit = 'metric'
                select_valid_unit = True
                print("")
                print("Okay, we are setting the units to Metric")
                print("")
                menu()
            case '2':
                weather_unit = 'imperial'
                select_valid_unit = True
                print("")
                print("Okay, we are setting the units to Imperial")
                print("")
                menu()
            case _:
                print("")
                print("Invalid choice. Please try again")
                print("")
                get_unit()

def open_file( filename ):
    global weather_json
    try:
        with open( filename, 'r') as file:
            weather_json = json.load( file)
    except FileNotFoundError:
        print("Error: Unable to open the file.")
    finally:
        file.close()

user_init()