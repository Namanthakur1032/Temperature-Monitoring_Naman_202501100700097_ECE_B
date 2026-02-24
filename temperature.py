import random
import time

def read_temperature():
    """Generate a random temperature"""
    return random.randint(0, 100)

def check_temperature(temp):
    """Check and display temperature status"""
    print(f"Current temperature: {temp}°C")

    if temp < 0:
        print("Warning: Temperature is below freezing point!")
    elif temp > 30:
        print("Warning: Temperature is above normal range!")
    else:
        print("Temperature is within the normal range.")

    print("-" * 22)

def monitor_temperature(readings=10, delay=2):
    """Monitor temperature for a fixed number of readings"""
    for _ in range(readings):
        temperature = read_temperature()
        check_temperature(temperature)
        time.sleep(delay)

# Start monitoring (10 readings)
monitor_temperature()