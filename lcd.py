import i2c
import time

LCD_WIDTH = 16   # Maximum characters per line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

I2C_ADDR  = 0x27 # I2C device address
I2C_BUS = 1

class lcd:
    # Define some device constants
    LCD_CHR = 1 # Mode - Sending data
    LCD_CMD = 0 # Mode - Sending command
    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
    LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
    LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

    def __init__(self, address = I2C_ADDR, port = I2C_BUS):
        self.lcd_bus = i2c.i2c(address, port)

    def lcd_init(self):
        # Initialise display
        self.lcd_byte(0x33,lcd.LCD_CMD) # 110011 Initialise
        self.lcd_byte(0x32,lcd.LCD_CMD) # 110010 Initialise
        self.lcd_byte(0x06,lcd.LCD_CMD) # 000110 Cursor move direction
        self.lcd_byte(0x0C,lcd.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
        self.lcd_byte(0x28,lcd.LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01,lcd.LCD_CMD) # 000001 Clear display
        time.sleep(E_DELAY)

    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = the data
        # mode = 1 for data
        #        0 for command

        bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
        bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

        # High bits
        self.led_bus.write_byte(I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        # Low bits
        self.led_bus.write_byte(I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self, bits):
        # Toggle enable
        time.sleep(E_DELAY)
        self.led_bus.write_byte(I2C_ADDR, (bits | ENABLE))
        time.sleep(E_PULSE)
        self.led_bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
        time.sleep(E_DELAY)

    def lcd_string(self, message,line):
        # Send string to display

        message = message.ljust(LCD_WIDTH," ")

        self.lcd_byte(line, lcd.LCD_CMD)

        for i in range(LCD_WIDTH):
            self.lcd_byte(ord(message[i]),lcd.LCD_CHR)
    