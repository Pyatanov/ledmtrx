def on_button_pressed_a():
    colorbit_51bit2.set_pixel_color(0, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(1, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(2, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(3, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(4, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(5, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(6, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.set_pixel_color(7, colorbit.colors(BitColors.VIOLET))
    colorbit_51bit2.show()
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    colorbit_51bit2.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

colorbit_51bit2: colorbit.Strip = None
colorbit_51bit2 = colorbit.create(DigitalPin.P0, 64, BitColorMode.RGB)
colorbit_51bit2.clear()
amtrx2 = 0

def on_forever():
    pass
basic.forever(on_forever)
