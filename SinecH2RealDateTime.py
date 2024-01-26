from datetime import datetime, timedelta

def hex_sinec_to_datetime(hex_sinec_time):
    # Convert hexadecimal to decimal
    sinec_time_decimal = int(hex_sinec_time, 16)
    
    # Siemens SINEC time is in milliseconds since January 1, 1984
    base_date = datetime(1984, 1, 1)
    
    # Convert milliseconds to seconds
    seconds = sinec_time_decimal / 1000
    
    # Calculate the real date-time by adding seconds to the base date
    real_datetime = base_date + timedelta(seconds=seconds)
    
    return real_datetime

# Example usage:
hex_sinec_time = "1E1D06F3A9BC"  # Replace with your Siemens SINEC time in hex
result_datetime = hex_sinec_to_datetime(hex_sinec_time)
print("Siemens SINEC Time (hex):", hex_sinec_time)
print("Real Date-Time:", result_datetime)
