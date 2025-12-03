import puerta
import servidorWeb

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        puerta.moverMotor()
        servidorWeb.prenderServidor()
    except KeyboardInterrupt:
        print("Ending program")
