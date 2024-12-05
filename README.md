# Weather App

# Quiz App
## This is an assignment for 'JustIT' within their technical training for Python
- Please see 'Project Brief.pdf' for full project details that this script must meet 
- Overview
- [x] 1. Welcome message 
- [x] 2. User Input
- [x] 3. Fetch Weather Data
- [x] 4. Display Weather Data
  - [x] Current temperature
  - [x] Weather conditions
  - [x] Wind Speed
  - [x] Humidity
- [x] 5. Data Validation
- [x] 6. Thank you message

# Index 
1. Overview and Error Handling 
2. References 

# 1. Overview and Error Handling 

## Initial Start and Rules
### Overview
- User is greeted to the script
- After the greeting, the user is shown the rules
- User must type any character to continue
- Once accepted, the user is shown an option screen to set the Units for their weather 
  
### Error Handling 
- User input to accept the rules must not be empty
- If the input is empty, repeat the input box and re-ask them to accept the rules

## Units Screen 
### Overview
- A screen to save how the user will see their weather - imperial or metric
- User is show two options:
  - 1. Metric
  - 2. Imperial
- User must select 1 or 2 to continue
- Once a valid number is entered (1 or 2). the input is saved into a global variable called 'weather_units
- Once a valid number is entered (1 or 2), then the user is taken to the main menu

### Error Handling 
- Users input is validated and check is the input value is either 1 or 2 
- If it isn't, then repeat the choice for the unit

## Main Menu
### Overview
- A screen to allow the user to have a choice on what they do
- User is shown three choice:
  - 1. Get current weather 
  - 2. Change units
  - 3. Exit
- User must select 1, 2 or 3 to continue 
- Once a valid number is selected, the user is navigated to the relevant screen
  - 1. Get current weather to weather cities
  - 2. Go to units screen and asks for a unit
  - 3. Exit to stop the script 
   
### Error Handling 
- Users input is validated and checked is the input is 1, 2 or 3
- If it isn't, then repeat the choice for the menu option

## Weather cities 
### Overview
- Shows the user a list of cities they can choose from, with an index value next to the city
- JSON files are read from the 'weather/' directory making the list dynamic, by adding more JSON files into 'weather'. The main menu will load them into the menu and also gets its name from the OpenWeather JSON file 
- Until a valid input is entered, the weather for a city will not show and the input is repeated

### Error Handling 
- Users input must be a valid option based on the city menu
- If the user enters an invalid number, the repeat the ask
  
## View a cities weather 
### Overview
- Output for the city the user has chosen is shown on the screen
- Depending on the unit the user has selected (unit or imperial), data is shown in a relevant format
  - e.g. Imperial = Fahrenheit, Miles per Hour
  - e.g. Metric = Celsius, Kilometers per Hour
- Once it is completed the user is shown the main menu

### Error Handling 
- When a user selects a city, the relevant filename is created, read and placed in the global variable 'weather_json'

# 2. References

> ## All weather JSON is from the OpenWeather API
> ## All data has been generated on 05/12/2024 around 10.00am 