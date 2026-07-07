import datetime

def get_current_time():
    """
    Returns the current time in HH:MM:SS format.
    """
    now = datetime.datetime.now()
    return now.strftime("%X")

def get_weather(city: str, unit: str) -> str:
    """
    Return the temperature in the given city in celsius or fahrenheit according to user choice
    """
    city = city.lower()
    unit = unit.lower()
    
    if city == "cairo":
        temperature = 35
    elif city == "alexandria":
        temperature = 35
    else:
        return "i dont have any informations about this city"
    if unit == "fahrenheit":
        temperature = temperature * 1.8 + 32  

    return{
        "city": city,
        "temperature": temperature,
        "unit": unit
    }

def calculator(a: float, b: float, operation: str)-> float:
    """
    Returns the result of addition, subtraaction, multiply or division according to user choice
    """
    
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "can do a divsion with zero in denomerator."
        result = a / b
    else:
        return "Invalid operation"

    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }    
    
def read_file(file_name: str)-> str:
    """
    Reads the contents of a text file and returns it as a string.
    Use this function when the user asks to read or view a file.
    """
    try:    
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise ValueError("Cant find the file")
    except Exception as e:
        return str(e)       