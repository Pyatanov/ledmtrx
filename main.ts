input.onButtonPressed(Button.A, function () {
    run = 1
    while (run == 1) {
        for (let index = 0; index <= 7; index++) {
            for (let index2 = 0; index2 <= 7; index2++) {
                LedXYShow(index, index2)
                basic.pause(10)
                colorbit_51bit2.clear()
            }
        }
        for (let index = 0; index <= 7; index++) {
            for (let index2 = 0; index2 <= 7; index2++) {
                X = 7 - index
                Y = 7 - index2
                LedXYShow(X, Y)
                basic.pause(10)
                colorbit_51bit2.clear()
            }
        }
    }
})
input.onButtonPressed(Button.B, function () {
    run = 0
    colorbit_51bit2.clear()
})
function LedXYShow (X: number, Y: number) {
    XY = X * mxlen + Y
    colorbit_51bit2.setPixelColor(XY, colorbit.colors(BitColors.White))
    colorbit_51bit2.show()
}
let Y = 0
let X = 0
let run = 0
let XY = 0
let mxlen = 0
let colorbit_51bit2: colorbit.Strip = null
colorbit_51bit2 = colorbit.create(DigitalPin.P0, 64, BitColorMode.RGB)
colorbit_51bit2.clear()
mxlen = 8
XY = 0 * mxlen + 4
run = 1
basic.forever(function () {
	
})
