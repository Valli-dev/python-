try:
    hello_file=open("flight.txt", 'w')
    text="Hello Everyone!! Welcomez!!!!"
    hello_file.write(text)
except:
    print("Error Occurred , not able to write to file!!")
finally:
    hello_file.close()

try:
    hello_file=open("flights.txt" , 'r')
    text=hello_file.read()
    print(text)
except:
    print("Error Occurred , not able to read from file!!")
finally:
    hello_file.close()