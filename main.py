from machine import Pin
from time import sleep

led_board = Pin("LED", Pin.OUT)#Led Integrado
sleep(1)    #le damos tiempo a vREPL
print("\nLED esta destellando...")
while True:
    try: #Para apagar el programa con un ctrl + c
        led_board.toggle()#Invierte el estado del led, no existe en esp32
        # led_board.value(not led_board.value())
        sleep(.5) # sleep 0.5 sec
    except (KeyboardInterrupt):
        break
led_board.off() #Apago el led, porque si estaba prendido quedaria asi
print("Listo")
