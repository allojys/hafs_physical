input.onButtonPressed(Button.A, function () {
    answer_key = answer_key + 1
    basic.showNumber(answer_key)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(answer_key)
    basic.showNumber(answer_key)
})
radio.onReceivedString(function (receivedString) {
    num1 = receivedString
    if (num1 == "UP") {
        basic.showArrow(ArrowNames.North)
    }
    if (num1 == "DOWN") {
        basic.showArrow(ArrowNames.South)
    }
    if (num1 == "OK") {
        basic.showString("\"Ok\"")
    }
})
input.onButtonPressed(Button.B, function () {
    answer_key = answer_key - 1
    basic.showNumber(answer_key)
})
let num1 = ""
let answer_key = 0
radio.setGroup(34)
answer_key = randint(1, 10)
basic.showNumber(answer_key)
