from threading import Thread

def inputt():
    global inp
    try:
        inp = input("Enter string jani   ")
    except Exception as e:
        print("Error = ",type(e))
    print ("Entered string  "+inp)

def reverse():
    print("Reversed string "+(inp[::-1]))

def capital():
    print("Capatalized string  "+(inp.upper()))

def shift():
    var = ""

    for i in (inp):
        shifted_char = chr(ord(i)+2)
        var += shifted_char
    print("Shifted string  "+(var))


thread = Thread(target = inputt)
thread1 = Thread(target = reverse)
thread2 = Thread(target = capital)
thread3 = Thread(target = shift)


thread.start()
thread.join()
thread1.start()
thread2.start()
thread3.start()

if thread1.is_alive() is True:
    thread1.join()

if thread2.is_alive() is True:
    thread2.join()

if thread3.is_alive() is True:
    thread3.join()
