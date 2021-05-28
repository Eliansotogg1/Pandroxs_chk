def temporizador():
    '''
    Threading es un simulador de procesador, puede simular 2 procesadores
    en uno solo para asi agilizar tareas.

    Esta funcion usa threading.Timer el cual es un temporizador.
    '''

    import threading

    def hola():
        print("Hola mundo")

    def morir():
        print("me quiero morir")

    timer1 = threading.Timer(5, hola)
    timer1.start()
    timer2 = threading.Timer(5, morir)
    timer2.start()
