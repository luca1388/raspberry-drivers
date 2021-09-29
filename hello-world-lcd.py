from i2c import lcd
import time

display = lcd.lcd(0x27, 1)

def main():
  # Main program block

  # Initialise display
  display.lcd_init()

  while True:
    # Send some test
    display.lcd_string("Hello world!", display.LCD_LINE_1)
    time.sleep(3)
  
    # Send some more text
    display.lcd_string("Raspberry PI", display.LCD_LINE_2)

    time.sleep(3)

    display.lcd_bounce_string("this is a very long string", display.LCD_LINE_2)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    display.lcd_byte(0x01, display.LCD_CMD)
