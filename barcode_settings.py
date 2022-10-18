#setting Example of Zero Barcode Scanner

import zero_barcode
import time
import sys
import serial
'''
* write command "dmesg" in cmd line of raspberry pi and see the port
* if you use as HAT then your port is "ttyS0"
* if you use as barcode hat via micr-usb then your port will be ttyACM0,ttyACM1 so on...
'''
port = "/dev/ttyACM0"  # write port here for eg.ttyS0,ttyACM0,ttyACM1.... etc
Baudrate = 115200    # write baudrate here

def change_buzz_freq(scan):
    print("1 - Passive low frequency") #select low buzzer sound(Passive)
    print("2 - Passive medium frequency") #select medium buzzer sound(Passive) 
    print("3 - Passive high frequency") #select high buzzer sound(Passive)    
    num = int(input("Select an option number: ")) 
    if num == 1:
        scan.Select_buzzer_sound(int(num))
    elif num == 2:
        scan.Select_buzzer_sound(int(num))
    elif num == 3:
        scan.Select_buzzer_sound(int(num))
    else:
        print("Invalid Command")
def Red_light(scan):    
    print("1 - Enable red line") #Enable red line 
    print("2 - Disable red line") #Disable red line
    print("\n")
    num = int(input("Select an option number: "))

    if num == 1:
        print("Red scan line on")
        scan.Red_light_on() 
    elif num == 2:
        print("Red scan line off")
        scan.Red_light_off()
    else:
        print("Invalid Command")
    
def decode_beep(scan):
    print("1 - Enable decode beep") #Enable buzzer beep sound on successfull read
    print("2 - Disable decode beep") #Disable buzzer beep sound on successfull read
    print("\n")
    num = int(input("Select an option number: "))
    if num == 1:
        print("Decode beep turned on")
        scan.Enable_buzzer_beep_sound()
    elif num == 2:
        print("Decode beep turned off")
        scan.Disable_buzzer_beep_sound()
    else:
        print("Invalid Command")
        
def boot_beep(scan):
    print("1 - Enable beep on module power on") #Enable beep sound on start/restart
    print("2 - Disable beep on module power off") #Disable beep sound on start/restart
    print("\n")
    num = int(input("Select an option number: "))
    
    if num == 1:
        print("Beep on power on enabled")
        scan.Boot_beep_sound_enable()
    elif num == 2:
        print("Beep on power on disabled")
        scan.Boot_beep_sound_disable()
    else:
        print("Invalid Command")
        
def Red_light(scan):    
    print("1 - Enable red line") #Enable red line 
    print("2 - Disable red line") #Disable red line
    print("\n")
    num = int(input("Select an option number: "))

    if num == 1:
        print("Red scan line on")
        scan.Red_light_on() 
    elif num == 2:
        print("Red scan line off")
        scan.Red_light_off()
    else:
        print("Invalid Command")

def image_flip(scan):
    print("1 - Turn on image flipping") #image flipping enabled
    print("2 - Turn off image flipping (default)") #image flipping disable
    print("\n")
    num = int(input("Select an option number: "))
    if num == 1:
        scan.Enable_mirror_image()
    elif num == 2:
        scan.Disable_mirror_image()
    else:
        print("Invalid Command")
        
def symbologies(scan):
    print("1 - Enable all 1D symbologies") #set scanner for reading 1D symbologies
    print("2 - Disable all 1D symbologies") #all 1D symbologies disbled
    print("3 - Enable all 2D symbologies") #enable 2D symbologies 
    print("4 - Disable all 2D symbologies")#disable all 2D symbologies
    print("\n")
    num = int(input("Select an option number: "))
    if num == 1:
        print("1D symbologies enabled")
        scan.On_1D_mode()
    elif num == 2:
        print("1D symbologies disabled")
        scan.Off_1D_mode()
    elif num ==3:
        print("2D symbologies enabled")
        scan.On_2D_mode()
    elif num == 4:
        print("2D symbologies disabled")
        scan.Off_2D_mode()
    else:
        print("Invalid Command")
        
def reading_area(scan):
    print("1 - Full width (default)") #set reading area at default(100%)
    print("2 - Center 80%") #reading area at 80%
    print("3 - Center 60%") #reading area at 60%
    print("4 - Center 40%") #reading area at 40%
    print("5 - Center 20%") #reading area at 20%
    print("\n")
    num = int(input("Select an option number: "))
    if num == 1:
        print("Scanning 100% of frame")
        scan.Area_of_reading_change(100)
    elif num == 2:
        print("Scanning center 80% of frame")
        scan.Area_of_reading_change(80)
    elif num == 3:
        print("Scanning center 60% of frame")
        scan.Area_of_reading_change(60)
    elif num == 4:
        print("Scanning center 40% of frame")
        scan.Area_of_reading_change(40)
    elif num == 5:
        print("Scanning center 20% of frame")
        scan.Area_of_reading_change(20)
    else:
        print("Invalid Command")
        
def flash_light(scan): 
    print("1 - Enable white light") #white light ON
    print("2 - Disable white light") #white light OFF 
    num = int(input("Select an option number: "))
    if num == 1:
        print("White scan light on")
        scan.White_light_on()
    elif num == 2:
        print("White scan light off")
        scan.White_light_off()
    else:
        print("Invalid Command")
        
def reading_mode(scan):
    print("1 - Manual read mode (default)") #scanner at manual reading mode
    print("2 - Continuous read mode") #set scanner at continuous reading mode
    print("3 - Motion sensor mode") #set scanner at motion sensor reading mode
    print("\n")
    num = int(input("Select an option number: "))
    if num == 1:
        print("Manual trigger mode enabled")
        scan.Manual_mode_on()
    elif num == 2:
        print("Continuous read mode enabled")
        scan.Manual_mode_on(1)
    elif num == 3:
        print("Motion trigger mode enabled")
        scan.Manual_mode_on()
    else:
        print("Invalid Command")
        
barcode = zero_barcode.Barcode_Scanner(port,Baudrate)
    
if barcode.begin() == False:
    print("Zero Barcode module is not connected")

print("ready!")
while True:
        print("1 - Start Scan")
        print("2 - Stop Scan")
        print("3 - Scan White light")
        print("4 - Aiming Red line")
        print("5 - Beep on Successfull read")
        print("6 - Start/Restart Beep")
        print("7 - Change Buzzer Frequency")
        print("8 - Image Flipping")
        print("9 - Set Reading Area")
        print("10 - Set Reading Mode")
        print("11 - Symbologies")
        print("\n")
        num = int(input("Select an option number: "))
        if num == 1:
            barcode.start_scan()
        elif num == 2:
            barcode.stop_scan()
        elif num == 3:
            flash_light(barcode)
        elif num == 4:
            Red_light(barcode)
        elif num == 5:
            decode_beep(barcode)
        elif num == 6:
            boot_beep(barcode)
        elif num == 7:
            change_buzz_freq(barcode)
        elif num == 8:
            image_flip(barcode)
        elif num == 9:
            reading_area(barcode)
        elif num == 10:
            reading_mode(barcode)
        elif num == 11:
            symbologies(barcode)
        else:
            print("Invalid Command")

