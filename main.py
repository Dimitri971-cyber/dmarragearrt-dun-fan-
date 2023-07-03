A = 0
xiamiBoard.init_xia_mi_board()

def on_forever():
    global A
    A = pins.map(xiamiBoard.read_angle(), 0, 1023, 0, 180)
    xiamiBoard.ole_dshow_user_number(xiamiBoard.read_angle(), 0, 0)
    xiamiBoard.ole_dshow_user_number(A, 1, 0)
    pins.servo_write_pin(AnalogPin.P0, A)
basic.forever(on_forever)

def on_forever2():
    xiamiBoard.ole_dclear()
    basic.pause(500)
basic.forever(on_forever2)