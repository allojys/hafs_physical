def on_button_pressed_a():
    global answer_key
    answer_key = answer_key + 1
    basic.show_number(answer_key)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(answer_key)
    basic.show_number(answer_key)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global num1
    num1 = receivedString
    if num1 == "UP":
        basic.show_arrow(ArrowNames.NORTH)
    if num1 == "DOWN":
        basic.show_arrow(ArrowNames.SOUTH)
    if num1 == "OK":
        basic.show_string("\"Ok\"")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global answer_key
    answer_key = answer_key - 1
    basic.show_number(answer_key)
input.on_button_pressed(Button.B, on_button_pressed_b)

num1 = ""
answer_key = 0
radio.set_group(34)
answer_key = randint(1, 10)
basic.show_number(answer_key)