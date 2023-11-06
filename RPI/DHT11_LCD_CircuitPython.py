#sudo pip3 install adafruit-circuitpython-dht
#sudo apt-get install libgpiod2

import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_dht
import RPi.GPIO as GPIO

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D19)

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D5)
lcd_en = digitalio.DigitalInOut(board.D6)
lcd_d4 = digitalio.DigitalInOut(board.D12)
lcd_d5 = digitalio.DigitalInOut(board.D13)
lcd_d6 = digitalio.DigitalInOut(board.D16)
lcd_d7 = digitalio.DigitalInOut(board.D17)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)


    
if __name__ == '__main__':
    while True:
        try:        
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
                  .format(temperature_f, temperature_c, humidity))
            lcd.clear()
            #lcd_line_1 = "Temperature:" + str(temperature_c) + " C"
            #lcd_line_2 = "\nHumidity:"+ str(humidity) + " %"
            #lcd.message = lcd_line_1 + lcd_line_2;
            lcd.message = ("Temper:%.1f C " %temperature_c)
            lcd.message = ("\nHumidity:%.1F " %humidity)
            
            time.sleep(2.0)
        
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue

        except KeyboardInterrupt:
            GPIO.cleanup()
            print ('Exiting Program')
            exit()
        

