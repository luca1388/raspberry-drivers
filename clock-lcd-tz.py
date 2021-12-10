from i2c import lcd
import time
from datetime import datetime
import pytz

display = lcd.lcd(0x27, 1)

def main():
  # Main program block

  # Initialise display
  display.lcd_init()

  while True:
    # Send some test
    tz_Rome = pytz.timezone('Europe/Rome') 
    datetime_Rome = datetime.now(tz_Rome)

    display.lcd_string(datetime_Rome.strftime("%H:%M"), display.LCD_LINE_1)
    display.lcd_string(datetime_Rome.strftime("%m/%d/%Y %a"), display.LCD_LINE_2)
   # time.sleep(3)
  
    # Send some more text
    #display.lcd_string("Raspberry PI", display.LCD_LINE_2)

    #time.sleep(3)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    display.lcd_byte(0x01, display.LCD_CMD)
