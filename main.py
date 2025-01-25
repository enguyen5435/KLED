from machine import Pin, I2C
from ahtx0 import AHT10
from time import sleep

# Initialize I2C for the AHT10 sensor
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
sensor = AHT10(i2c)

# Initialize the light sensor (digital input)
light_sensor = Pin(14, Pin.IN)  # GPIO14 as digital input

print("Reading data from sensors...")
while True:
    try:
        # Read temperature and humidity from AHT10
        temperature = sensor.temperature  # In Celsius
        humidity = sensor.relative_humidity  # In %
        
        # Read light sensor output
        light_detected = light_sensor.value()  # 1 = no light, 0 = light
        
        # Print sensor readings
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity:.2f} %")
        print("Light Detected!" if not light_detected else "No Light Detected")
        
        # Wait before the next reading
        sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        sleep(2)