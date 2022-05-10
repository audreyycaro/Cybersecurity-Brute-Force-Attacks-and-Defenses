# radio_send_images_caesar_key_unknown_try_this.py

from microbit import *
import radio
import random                               

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

string_list = ["HAPPY", "SAD", "ANGRY"]

# key = random.randint(1, 25)              
key = random.randint(1, 93)                

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        
        # packet = caesar(3, packet)            
        # packet = caesar(key, packet)          
        packet = ascii_shift(key, packet)        
        
        
        print("Send encrypted:", packet)
        radio.send(packet)
        # sleep(2500)                       
        sleep(6000)                         
