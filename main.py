bluetooth.onBluetoothConnected(function () {
    basic.showString("Conected")
    pins.digitalWritePin(DigitalPin.P8, 1)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showString("Disconected")
    pins.digitalWritePin(DigitalPin.P8, 0)
})
function Popit () {
    katakana.showString("Popits")
    bluetooth.uartWriteLine("Popit_>")
}
input.onButtonPressed(Button.B, function () {
    Popit()
})
