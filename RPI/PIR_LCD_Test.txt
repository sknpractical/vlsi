
#Raspberry Pi Libraries 
import RPi.GPIO as GPIO #GPIO library
import time #library for sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

#set mode as BCM
GPIO.setmode(GPIO.BCM)

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



#set pins
PIR = 21
BUZ = 22

#setup pins at output
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(BUZ, GPIO.OUT)



if __name__ =='__main__':
    try:
        while True:
            PIR_State = GPIO.input(PIR)
            if (PIR_State == True):
                print ("Motion Detected")
                lcd.clear()
                lcd.message = "Motion Detected"
                GPIO.output (BUZ, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output (BUZ, GPIO.LOW)
                time.sleep(0.5)
            
            else:
                lcd.clear()
                lcd.message = "NO Motion"
                print ("No Motion")
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        GPIO.cleanup()



    