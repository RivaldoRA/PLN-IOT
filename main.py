import puerta

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        puerta.moverMotor()
    except KeyboardInterrupt:
        print("Ending program")