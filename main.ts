function Popit2 () {
    bluetooth.uartWriteString("Popit>")
}
bluetooth.onBluetoothConnected(function () {
    pins.digitalWritePin(DigitalPin.P8, 1)
})
bluetooth.onBluetoothDisconnected(function () {
    pins.digitalWritePin(DigitalPin.P8, 0)
})
function Popit () {
	
}
input.onButtonPressed(Button.B, function () {
    Popit2()
})
