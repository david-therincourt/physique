from physique import Pyboard
feather = Pyboard("/dev/ttyACM0")
reponse = feather.exec_file("hello.py")
print(reponse)
