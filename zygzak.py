import time, sys

indent = 0
indentzwiekszanie = True

try:
    while True:
        patern =  " "  * indent + "********"
        print(patern)
        time.sleep(0.2)

        if indentzwiekszanie:
            indent = indent + 1
            if indent == 20:
                indentzwiekszanie = False

        else:
            indent = indent - 1
            if indent == 0:
                indentzwiekszanie = True
except KeyboardInterrupt:
    sys.exit()


