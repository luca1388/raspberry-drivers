#!/usr/bin/python
# -*- coding: utf-8 -*-

from i2c import lcd
from weather import weather
import time

display = lcd.lcd(0x27, 1)

def main():
  # Main program block

  # Initialise display
  display.lcd_init()

  while True:
    # Send some test
    weather_data = weather.get_weather_data()
    display.lcd_string(str(weather_data["name"]), display.LCD_LINE_1)
    display.lcd_string(str(weather_data["main"]["temp"]), display.LCD_LINE_2)
    # # Send some more text
    time.sleep(3)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    display.lcd_byte(0x01, display.LCD_CMD)


