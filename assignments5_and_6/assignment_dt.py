from datetime import datetime

# datetime to string
def datetime_to_str_1(dt):
    # Convert to format "2023-07-19"
    formatted_date = dt.strftime('%Y-%m-%d')
    return formatted_date

def datetime_to_str_2(dt):
    # Convert to format "23-07-19"
    formatted_date = dt.strftime('%y-%m-%d')
    return formatted_date

def datetime_to_str_3(dt):
    # Convert to format "July 19, 2023"
    formatted_date = dt.strftime('%B %d, %Y')
    return formatted_date

def datetime_to_str_4(dt):
    # Convert to format "Jul 19, 2023"
    formatted_date = dt.strftime('%b %d, %Y')
    return formatted_date

def datetime_to_str_5(dt):
    # Convert to format "19 July 2023"
    formatted_date = dt.strftime('%d %B %Y')
    return formatted_date

def datetime_to_str_6(dt):
    # Convert to format "Wednesday July 19, 2023"
    formatted_date = dt.strftime('%A %B %d, %Y')
    return formatted_date

def datetime_to_str_7(dt):
    # Convert to format "Wed July 19, 2023"
    formatted_date = dt.strftime('%a %B %d, %Y')
    return formatted_date

def datetime_to_str_8(dt):
    # Convert to format "2023-07-19 10:30:45"
    formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

def datetime_to_str_9(dt):
    # Convert to format "10:30:45"
    formatted_date = dt.strftime('%H:%M:%S')
    return formatted_date

def datetime_to_str_10(dt):
    # Convert to format "10:30 AM"
    formatted_date = dt.strftime('%H:%M %p')
    return formatted_date

# string to datetime
def str_to_datetime_1(s):
    # Convert from format "2023-07-19"
    parsed_date = datetime.strptime(s, '%Y-%m-%d')
    return parsed_date

def str_to_datetime_2(s):
    # Convert from format "23-07-19"
    parsed_date = datetime.strptime(s, '%y-%m-%d')
    return parsed_date

def str_to_datetime_3(s):
    # Convert from format "July 19, 2023"
    parsed_date = datetime.strptime(s, '%B %d, %Y')
    return parsed_date

def str_to_datetime_4(s):
    # Convert from format "Jul 19, 2023"
    parsed_date = datetime.strptime(s, '%b %d, %Y')
    return parsed_date

def str_to_datetime_5(s):
    # Convert from format "19 July 2023"
    parsed_date = datetime.strptime(s, '%d %B %Y')
    return parsed_date

def str_to_datetime_6(s):
    # Convert from format "Wednesday July 19, 2023"
    parsed_date = datetime.strptime(s, '%A %B %d, %Y')
    return parsed_date

def str_to_datetime_7(s):
    # Convert from format "Wed July 19, 2023"
    parsed_date = datetime.strptime(s, '%a %B %d, %Y')
    return parsed_date

def str_to_datetime_8(s):
    # Convert from format "2023-07-19 10:30:45"
    parsed_date = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    return parsed_date

def str_to_datetime_9(s):
    # Convert from format "10:30:45"
    parsed_date = datetime.strptime(s, '%H:%M:%S')
    return parsed_date

def str_to_datetime_10(s):
    # Convert from format "10:30 AM"
    parsed_date = datetime.strptime(s, '%H:%M %p')
    return parsed_date
