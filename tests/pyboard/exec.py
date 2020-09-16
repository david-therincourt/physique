from physique import Pyboard

pyb = Pyboard("/dev/ttyACM0")

pyb.enter_raw_repl()
pyb.exec_("print('Hello')")
pyb.exit_raw_repl()

pyb.close()
