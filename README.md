# raspberrypi

Simple recipes for Raspberry pi + python examples

Raspberry PI is a cheap computer that runs Linux based OS & allows you to interact with Physical world via GPIO (General Purpose Input & Output pins) using which you can connect Sensors & Accuators. Given its computational ability it can be used for various purposes, including IoT, ML and many more.

**Steps to configure Raspberry PI:**
  Headless method (SSH / VNC)

**Headless Method:** 

Navigate to https://www.raspberrypi.com/software/ and download the Raspberry Pi Imager software for your system, this allows you to select the flavour of raspberrypi OS & pre-configure the wifi, enable remote connectivity using SSH / VNC. <br> 
     &ensp;_This instruction is written for Raspberry Pi imager V1.8.4_ <br> 
     *Open the Imager Software and select "Raspberry Pi Zero W" Or the device that you own <br> 
     *Select your SD Card (Make sure to format it using the Erase option from OS Menu) <br> 
     *Select the OS, Go to "Raspberry Pi OS (Other)" --> Select "Raspberry Pi OS Lite (32-bit)" that has no Desktop Environment. <br> 
     *Click Next and Click "Edit Settings" and use the below config <br> 
**Hostname = raspberrypi <br> 
&ensp;&ensp;&ensp;&ensp;set username and password <br> 
&ensp;&ensp;&ensp;&ensp;username = pi <br> 
&ensp;&ensp;&ensp;&ensp;password = raspberry <br> 
&ensp;&ensp;&ensp;&ensp;Enable WiFi & provide the Wifi Credentials, Set the Wifi country you are connecting from <br> 
&ensp;&ensp;&ensp;&ensp;Set Locale Settings and select your TimeZone & select US Keyboard layout <br> 
&ensp;&ensp;&ensp;&ensp;Go to the Services Tab and Enable SSH & leave Use Password Authenticaion method selected. <br> 
&ensp;&ensp;&ensp;&ensp;Click Save and Select Yes to apply customization & click Yes again on the prompt. <br> 
&ensp;&ensp;&ensp;&ensp;Click Next and enter your system's password if prompted and wait for the OS to burn on SD Card. <br> 
     Now you can Eject the SD Card from system and insert it on to Raspberry Pi and boot it up. <br> 
     
  

![circuit (3)](https://github.com/sreeramtkd/raspberrypi/assets/25638554/067811ea-2c3a-4706-b35d-34977430606f)
