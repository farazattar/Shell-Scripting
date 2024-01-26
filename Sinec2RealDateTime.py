from datetime import datetime

def siemens_sinec_to_datetime(sinec_time):
    # Siemens SINEC time is in milliseconds since January 1, 1984
    base_date = datetime(1984, 1, 1)
    
    # Convert milliseconds to seconds
    seconds = sinec_time / 1000
    
    # Calculate the real date-time by adding seconds to the base date
    real_datetime = base_date + timedelta(seconds=seconds)
    
    return real_datetime

# Example usage:
sinec_time = 1234567890123  # Replace with your Siemens SINEC time
result_datetime = siemens_sinec_to_datetime(sinec_time)
print("Siemens SINEC Time:", sinec_time)
print("Real Date-Time:", result_datetime)
