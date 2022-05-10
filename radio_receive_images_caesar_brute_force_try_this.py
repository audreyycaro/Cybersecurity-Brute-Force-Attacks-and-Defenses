# radio_receive_images_caesar_brute_force_try_this.py

from microbit import *
import radio

''' Function converts plaintext to ciphertext using key '''

def ascii_shift(key, text):                
    result = ""                             
    for letter in text:                   
        ascii = ( ord(letter) + key - 32 ) % 94 + 32  
        result = result + chr(ascii)        
    return result                           

''' Script starts from here... '''

radio.on()
radio.config(channel=7)

sleep(1000)

while True:
    
    packet = radio.receive()

    if packet:
        print("Receive encrypted:", packet)
        # packet = caesar(-3, packet)             
        # print("packet:", packet)                
        # display.show(getattr(Image, packet))    
        # for key in range(-1, -26, -1):          
        for key in range(-1, -94, -1):           
            # result = caesar(key, packet)        
            result = ascii_shift(key, packet)     
            print("key:", key, "result:", result) 
            sleep(200)                            
        print()                                   
