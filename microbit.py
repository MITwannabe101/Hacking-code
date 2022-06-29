from microbit import *

pins.digital_write_pin(DigitalPin.P16, 1)
pins.digital_write_pin(DigitalPin.P12, 1)
pins.digital_write_pin(DigitalPin.P13, 0)
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
makerbit.connect_lcd(39)
makerbit.set_lcd_backlight(LcdBacklight.ON)
while True:
    pins.servo_write_pin(AnalogPin.P0, 180)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    humidity = "" + str(dht11_dht22.read_data(dataType.HUMIDITY))
    temperature = "" + str(dht11_dht22.read_data(dataType.HUMIDITY))
    makerbit.show_string_on_lcd1602("" + str(humidity) + ":" + str(temperature) + "C*",
        makerbit.position1602(LcdPosition1602.POS1),
        16)
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.PURPLE))
    pixel = 0
    while pixel < 4:
        strip.set_pixel_color(pixel, neopixel.colors(NeoPixelColors.PURPLE))
        basic.pause(100)
        pixel += 1
    pins.servo_write_pin(AnalogPin.P0, 180)
    pixel = 0
    while pixel < 4:
        strip.set_pixel_color(pixel, neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(100)
        pixel += 1
