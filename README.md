# Zero-Barcode-HAT

<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img2.JPG" />
<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img1.JPG" />

### Zero Barcode HAT for Raspberry Pi is a robust and compact barcode scanner board that consists of a DE2120 scanner module, buzzer, 1.14” LCD screen, micro-USB port. It is designed to scan 20 different barcode symbologies in the segment of both 1D and 2D symbology like barcodes and QR codes.
## Reserved Pins Of Zero Barcode HAT
* Following are the reserved pins of Zero barcode HAT Scanner
<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/Zero_barcode_ReservedPin.png" />

## Important Datasheets in this directory 
  * **DE2120_Datasheet.pdf (Datasheet of DE2120)**
  * **Setting_Manual_DY_Scan_DE2120.pdf (Set settings of barcode)**
  
  
### Steps for setup RPi to work with Zero-Barcode HAT

#### Step 1 - So, before start working with this module first you have to enable the SPI in raspberry pi, for this go to cmd then type sudo raspi-config then go to ->interface option -> and enable the SPI by Following the below image steps
   * After typing the command in your command line press enter, it will take you on a new tab of configuring RPi.
    <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC1.PNG" /> 

   * As the below image showing a tab to configure your RPi, use arrow key of your keyboard and go to Interface options and press enter. After that keep following the      image instruction till finish SPI configuration 
     <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC2.PNG" /> 

   * <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC3.PNG" /> 

   * <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC4.PNG" /> 

   * <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC5.PNG" /> 

   * <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC6.PNG" /> 

   * After Finishing it-up reboot your RPi by typing reboot command and press enter
     <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC7.PNG" /> 

#### Step 2 - Now, Setup your Pi Zero Barcode HAT for using with RPi

   * After attaching the Barcode HAT to the RPi Zero, turn it on with a USB cable and begin configuring the barcode scanner for RPi. 

   * First, you need to change the mode of the Zero Barcode HAT for this you need to scan the below barcode settings before running the code
  
   <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/ttl_rs232.JPG" />
   
   * In this step you have to Change the baud rate to (9600) for this you need to scan the below barcode by pressing the scan button on the Zero Barcode Hat.    You        can also change the baud rate according to your choice by reffering to Barcode Manual provided in this Repo
     <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/baudrate.JPG" />

   * The DE2120 is completely user configurable, you can configure many settings according to your requirement by reffering the DE2120 Manual(Barcode manual) provided      in this Repo
 
#### Step 3 - Code 
   * **barcode_scanner.py** - Run this file in raspberry pi, Now scan the barcode, you will see barcode also show in display
#### Step 4 - code 
* **de2120_ex2_serial_settings.py** - Run this file if woant to change(Configure) settings of Barcode Scanner 

## Use Zero Barcode HAT without Raspberry Pi( Via USB Cable )
You can also use this barcode HAT simply with USB cable for reading (without any controller board). 

#### Step 1 - For this you simply need to scan the Below barcode and Yor barcode scanner is now ready to work in USB keyboard mode.

   <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img7.JPG" />
  
#### Step 2 - In USB keyboard mode, you have to open a notepad/word and scan any barcode or QR-code to get their number in your system. As shown in image below

   <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/SC.PNG" />


## Working
<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img6.png" />

## Applications
First of all, move all the files from the applications folder to the outside folder which is the Zero Barcode HAT folder, so that main.py could access the files in the lib sub-directory
* Pins of the ultrasonic sensor (we use this sensor to avoid pressing the push button to scan the barcode ), we use 3v ultrasonic sensor
   * Trig is connected to GPIO 4
   * Echo is connected to GPIO 17
* Servo motor
   * Servo motor pin is connected to GPIO 2

## Working of Applications 
  * Smart shopping
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img1.png" />
  
  * Smart Library Management System
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img4.png" />
  
  * Smart Attendence System
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img2.png" />

   
## Documentation

* [Pi Barcode HAT Hardware](https://github.com/sbcshop/Pi-Barcode-HAT-Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [Pi Barcode HAT](https://shop.sb-components.co.uk/products/barcode-hat-for-raspberry-pi?_pos=1&_sid=aa7761aaf&_ss=r)

 ![Pi Barcode HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/5_4efca5ba-1f85-4eb6-b89b-4d26162b093e.jpg?v=1665556430&width=400)

* [Barcode Breakout](https://shop.sb-components.co.uk/products/barcode-breakout?_pos=2&_sid=f80a0123d&_ss=r)

 ![Barcode Breakout](https://cdn.shopify.com/s/files/1/1217/2104/products/3_6c5d4598-fe42-4a18-8d8a-ab235e78c375.jpg?v=1665562539&width=400)
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>


