def convert_to_24_hour(hour, minute, time_period):
    if time_period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  # time_period is "pm"
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    # Convert hour and minute to strings with leading zeros if necessary
    hour_str = str(hour_24).zfill(2)
    minute_str = str(minute).zfill(2)
    
    return hour_str + minute_str

# Test cases
print(convert_to_24_hour(8, 30, "am"))  
print(convert_to_24_hour(8, 30, "pm"))  
print(convert_to_24_hour(12, 15, "am"))  
print(convert_to_24_hour(12, 15, "pm"))  
