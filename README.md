# raspberrypi

Simple recipes for Raspberry pi + python examples

Raspberry PI is a cheap computer that runs Linux based OS & allows you to interact with Physical world via GPIO (General Purpose Input & Output pins) using which you can connect Sensors & Accuators. Given its computational ability it can be used for various purposes, including IoT, ML and many more.

**<h2>Steps to configure Raspberry PI:</h2>**
**<h3>Headless Method (SSH):</h3>** 

Navigate to https://www.raspberrypi.com/software/ and download the Raspberry Pi Imager software for your system, this allows you to select the flavour of raspberrypi OS & pre-configure the wifi, enable remote connectivity using SSH / VNC. <br> 
* This instruction is written for Raspberry Pi imager V1.8.4_ <br>
    * Open the Imager Software and select "Raspberry Pi Zero W" Or the device that you own <br> 
    * Select your SD Card (Make sure to format it using the Erase option from OS Menu) <br> 
    * Select the OS, Go to "Raspberry Pi OS (Other)" --> Select "Raspberry Pi OS Lite (32-bit)" that has no Desktop Environment. <br> 
    * Click Next and Click "Edit Settings" and use the below config <br> 
      * Hostname = raspberrypi <br> 
      * set username and password <br> 
      * username = pi <br> 
      * password = raspberry <br> 
      * Enable WiFi & provide the Wifi Credentials, Set the Wifi country you are connecting from <br> 
      * Set Locale Settings and select your TimeZone & select US Keyboard layout <br> 
      * Go to the Services Tab and Enable SSH & leave Use Password Authenticaion method selected. <br> 
      * Click Save and Select Yes to apply customization & click Yes again on the prompt. <br> 
    * Click Next and enter your system's password if prompted and wait for the OS to burn on SD Card. <br>
  * Now you can Eject the SD Card from system and insert it on to Raspberry Pi and boot it up. <br> 

<p> Power ON your Raspberry PI and wait for atleast 5 minutes for the initial boot process to complete, your Raspberry PI might reboot 2 times to resize your SD Card</p>
<b><h2>Accessing Raspberry PI remotely (Local Network)</h2></b>

* If you have enabled the SSH & Hostname you can access your RPI with its hostname via Terminal, For Windows OS, download & run PUTTY <a href="https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe">Click here</a> 
* If for some reason if you are not able to access RPI with its hostname, you need to find its IP address. The simplest way to do so, is to scan your network using some Network Scanners like Advanced IP Scanner, Angry IP Scanner. Locate the IP using Hostname "raspberrypi" or MAC Vendor as "Raspberry PI Org"

<h2>Initial update</h2>

* Inorder to ensure your RPI gets its updates, run the below commands
	* sudo apt-get update
 	* sudo apt-get upgrade -y
<br><br>


![circuit (3)](https://github.com/sreeramtkd/raspberrypi/assets/25638554/067811ea-2c3a-4706-b35d-34977430606f)
