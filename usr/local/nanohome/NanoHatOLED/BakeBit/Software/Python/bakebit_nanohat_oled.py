#!/usr/bin/env python
#
# BakeBit example for the basic functions of BakeBit 128x64 OLED (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_OLED_128x64)
#
# The BakeBit connects the NanoPi NEO and BakeBit sensors.
# You can learn more about BakeBit here:  http://wiki.friendlyarm.com/BakeBit
#
# Have a question about this example?  Ask on the forums here:  http://www.friendlyarm.com/Forum/
#
'''
## License

The MIT License (MIT)

BakeBit: an open source platform for connecting BakeBit Sensors to the NanoPi NEO.
Copyright (C) 2016 FriendlyARM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import bakebit_128_64_oled as oled
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import sys
import subprocess
import threading
import signal
import os
import socket
import fcntl
import struct

global width
width=128
global height
height=64

global pageCount
pageCount=2
global pageIndex
pageIndex=0
global showPageIndicator
showPageIndicator=False

global pageSleep
pageSleep=120
global pageSleepCountdown
pageSleepCountdown=pageSleep

oled.init()  #initialze SEEED OLED display
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setHorizontalMode()

global drawing
drawing = False

global image
image = Image.new('1', (width, height))
global draw
draw = ImageDraw.Draw(image)
global fontb24
fontb24 = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 24);
global font14
font14 = ImageFont.truetype('DejaVuSansMono.ttf', 14);
global smartFont
smartFont = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 10);
global fontb14
fontb14 = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 14);
global font11
font11 = ImageFont.truetype('DejaVuSansMono.ttf', 11);
global font12
font12 = ImageFont.truetype('DejaVuSansMono.ttf', 12);

global lock
lock = threading.Lock()

def draw_page():
    global drawing
    global image
    global draw
    global oled
    global font
    global font14
    global smartFont
    global width
    global height
    global pageCount
    global pageIndex
    global showPageIndicator
    global width
    global height
    global lock
    global pageSleepCountdown
    global os

    lock.acquire()
    is_drawing = drawing
    page_index = pageIndex
    lock.release()

    if is_drawing:
        return

    #if the countdown is zero we should be sleeping (blank the display to reduce screenburn)
    if pageSleepCountdown == 1:
        oled.clearDisplay()
        pageSleepCountdown = pageSleepCountdown - 1
        return

    if pageSleepCountdown == 0:
        return

    pageSleepCountdown = pageSleepCountdown - 1

    lock.acquire()
    drawing = True
    lock.release()

    # Draw a black filled box to clear the image.            
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Draw current page indicator
    if showPageIndicator:
        dotWidth=4
        dotPadding=2
        dotX=width-dotWidth-1
        dotTop=(height-pageCount*dotWidth-(pageCount-1)*dotPadding)/2
        for i in range(pageCount):
            if i==page_index:
                draw.rectangle((dotX, dotTop, dotX+dotWidth, dotTop+dotWidth), outline=255, fill=255)
            else:
                draw.rectangle((dotX, dotTop, dotX+dotWidth, dotTop+dotWidth), outline=255, fill=0)
            dotTop=dotTop+dotWidth+dotPadding

    # Draw Home

    if page_index==0:
        text = time.strftime("%e %b %Y %H:%M")
        draw.text((2,2),text,font=font11,fill=255)
        draw.text((2,18),'Recovery',font=fontb24,fill=255)
        cmd = "wstat"
        #cmd = "ip a | grep wlan0 | grep inet | awk '{print $2}' | rev | cut -c4- | rev"
        wstat = subprocess.check_output(cmd, shell = True )
        draw.text((2,50),str(wstat, encoding='utf-8', errors='ignore'),font=font12,fill=255)

    # Backup & Restore Menu

    elif page_index==1:  

        draw.rectangle((2,2,width-4,2+16), outline=0, fill=255)
        draw.text((2, 4),  '-> Install Update',  font=smartFont, fill=0)

        draw.rectangle((2,16,width-4,16+16), outline=0, fill=0)
        draw.text((2, 18),  '-> Backup',  font=smartFont, fill=255)

        draw.rectangle((2,30,width-4,30+16), outline=0, fill=0)
        draw.text((2, 32),  '-> Restore',  font=smartFont, fill=255)
        
        draw.rectangle((2,44,width-4,44+16), outline=0, fill=0)
        draw.text((2, 46),  '-> Check Backup',  font=smartFont, fill=255) 

    # Draw Shutdown -- no

    elif page_index==3:
        draw.text((2, 2),  'Shutdown?',  font=fontb14, fill=255)

        draw.rectangle((2,20,width-4,20+16), outline=0, fill=0)
        draw.text((4, 22),  'Yes',  font=font11, fill=255)

        draw.rectangle((2,38,width-4,38+16), outline=0, fill=255)
        draw.text((4, 40),  'No',  font=font11, fill=0)

    # Draw Shutdown -- yes

    elif page_index==4:
        draw.text((2, 2),  'Shutdown?',  font=fontb14, fill=255)

        draw.rectangle((2,20,width-4,20+16), outline=0, fill=255)
        draw.text((4, 22),  'Yes',  font=font11, fill=0)

        draw.rectangle((2,38,width-4,38+16), outline=0, fill=0)
        draw.text((4, 40),  'No',  font=font11, fill=255)

    # Draw Shutdown Message

    elif page_index==5:
        draw.text((2, 2),  'Shutting down',  font=fontb14, fill=255)
        draw.text((2, 20),  'Please wait...',  font=font11, fill=255)

    # Draw Change Wifi - Wifi Client

    elif page_index==6: 
        draw.text((2, 2),  'Wifi Mode',  font=fontb14, fill=255)

        draw.rectangle((2,18,width-4,18+16), outline=0, fill=255)
        draw.text((4, 20),  'Wifi Client',  font=smartFont, fill=0)

        draw.rectangle((2,32,width-4,32+16), outline=0, fill=0)
        draw.text((4, 34),  'Hotspot',  font=smartFont, fill=255)
        
        draw.rectangle((2,46,width-4,46+16), outline=0, fill=0)
        draw.text((4, 48),  'NanoGate',  font=smartFont, fill=255)

    # Draw Chang Wifi - Hotspot

    elif page_index==7:
        draw.text((2, 2),  'Wifi Mode',  font=fontb14, fill=255)

        draw.rectangle((2,18,width-4,18+16), outline=0, fill=0)
        draw.text((4, 20),  'Wifi Client',  font=smartFont, fill=255)

        draw.rectangle((2,32,width-4,32+16), outline=0, fill=255)
        draw.text((4, 34),  'Hotspot',  font=smartFont, fill=0)
        
        draw.rectangle((2,46,width-4,46+16), outline=0, fill=0)
        draw.text((4, 48),  'NanoGate',  font=smartFont, fill=255)

    # Draw Chang Wifi - NanoGate

    elif page_index==8:
        draw.text((2, 2),  'Wifi Mode',  font=fontb14, fill=255)

        draw.rectangle((2,18,width-4,18+16), outline=0, fill=0)
        draw.text((4, 20),  'Wifi Client',  font=smartFont, fill=255)

        draw.rectangle((2,32,width-4,32+16), outline=0, fill=0)
        draw.text((4, 34),  'Hotspot',  font=smartFont, fill=255)
        
        draw.rectangle((2,46,width-4,46+16), outline=0, fill=255)
        draw.text((4, 48),  'NanoGate',  font=smartFont, fill=0)

    # Draw Change to Wifi Client
 
    elif page_index==9:
        draw.text((2, 2),  'Wifi Client',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)

    # Draw Change to Hotspot
 
    elif page_index==10:
        draw.text((2, 2),  'Hotspot',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)

    # Draw Change to NanoGate
 
    elif page_index==11:
        draw.text((2, 2),  'NanoGate',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)

    # Backup & Restore - Backup

    elif page_index==12:  
        draw.rectangle((2,2,width-4,2+16), outline=0, fill=0)
        draw.text((2, 4),  '-> Install Update',  font=smartFont, fill=255)

        draw.rectangle((2,16,width-4,16+16), outline=0, fill=255)
        draw.text((2, 18),  '-> Backup',  font=smartFont, fill=0)

        draw.rectangle((2,30,width-4,30+16), outline=0, fill=0)
        draw.text((2, 32),  '-> Restore',  font=smartFont, fill=255)
        
        draw.rectangle((2,44,width-4,44+16), outline=0, fill=0)
        draw.text((2, 46),  '-> Check Backup',  font=smartFont, fill=255) 

    # Backup & Restore - Restore

    elif page_index==13:  
        draw.rectangle((2,2,width-4,2+16), outline=0, fill=0)
        draw.text((2, 4),  '-> Install Update',  font=smartFont, fill=255)

        draw.rectangle((2,16,width-4,16+16), outline=0, fill=0)
        draw.text((2, 18),  '-> Backup',  font=smartFont, fill=255)

        draw.rectangle((2,30,width-4,30+16), outline=0, fill=255)
        draw.text((2, 32),  '-> Restore',  font=smartFont, fill=0)
        
        draw.rectangle((2,44,width-4,44+16), outline=0, fill=0)
        draw.text((2, 46),  '-> Check Backup',  font=smartFont, fill=255) 

    # Backup & Restore - Check

    elif page_index==14:  
        draw.rectangle((2,2,width-4,2+16), outline=0, fill=0)
        draw.text((2, 4),  '-> Install Update',  font=smartFont, fill=255)

        draw.rectangle((2,16,width-4,16+16), outline=0, fill=0)
        draw.text((2, 18),  '-> Backup',  font=smartFont, fill=255)

        draw.rectangle((2,30,width-4,30+16), outline=0, fill=0)
        draw.text((2, 32),  '-> Restore',  font=smartFont, fill=255)
        
        draw.rectangle((2,44,width-4,44+16), outline=0, fill=255)
        draw.text((2, 46),  '-> Check Backup',  font=smartFont, fill=0) 

    # Update...
 
    elif page_index==15:
        draw.text((2, 2),  'Update NanoHome',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)

    # Backup...
 
    elif page_index==16:
        draw.text((2, 2),  'Backing up',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)
        
    # Restore...
 
    elif page_index==17:
        draw.text((2, 2),  'Restoring',  font=fontb14, fill=255)
        draw.text((2, 22),  'Please wait...',  font=font11, fill=255)

    # Check Backup...
 
    elif page_index==18:
        draw.text((2,2),'Last Backup:',font=font11,fill=255)
        cmd = "check_backup bkupdate"
        bkup = subprocess.check_output(cmd, shell = True )
        draw.text((2,16),str(bkup, encoding='utf-8', errors='ignore'),font=font11,fill=255)
        
        cmd = "ls -lh /root/nanohome_backup.img | cut -d' ' -f5"
        size = subprocess.check_output(cmd, shell = True )
        sizestr = "Size: " + str(size, encoding='utf-8', errors='ignore')
        draw.text((2,30),sizestr,font=font11,fill=255)
        
        cmd = "check_backup running"
        bkups = subprocess.check_output(cmd, shell = True )
        state = 'Status: ' + str(bkups, encoding='utf-8', errors='ignore')
        draw.text((2,44),state,font=font11,fill=255)

    # Check Update...
 
    elif page_index==19:

        cmd = "tail -1 /boot/update/nhupd.log"
        updlog = subprocess.check_output(cmd, shell = True )
        draw.text((2,8),str(updlog, encoding='utf-8', errors='ignore'),font=font11,fill=255)

        cmd = "stat -c '%.16y' /boot/update/nhupd.log"
        upddate = subprocess.check_output(cmd, shell = True )
        draw.text((2,30),'Last Update:',font=font11,fill=255)
        draw.text((2,44),str(upddate, encoding='utf-8', errors='ignore'),font=font11,fill=255)

    oled.drawImage(image)

    lock.acquire()
    drawing = False
    lock.release()


def is_showing_power_msgbox():
    global pageIndex
    lock.acquire()
    page_index = pageIndex
    lock.release()
    if page_index==3 or page_index==4:
        return True
    return False

def is_showing_wifi_msgbox():
    global pageIndex
    lock.acquire()
    page_index = pageIndex
    lock.release()
    if page_index==6 or page_index==7 or page_index==8:
        return True
    return False

def is_showing_backup_msgbox():
    global pageIndex
    lock.acquire()
    page_index = pageIndex
    lock.release()
    if page_index==1 or page_index==12 or page_index==13 or page_index==14:
        return True
    return False

def update_page_index(pi):
    global pageIndex
    lock.acquire()
    pageIndex = pi
    lock.release()


def receive_signal(signum, stack):
    global pageIndex
    global pageSleepCountdown
    global pageSleep

    lock.acquire()
    page_index = pageIndex
    lock.release()

    if page_index==5:
        return

    if signum == signal.SIGUSR1:
        print ('K1 pressed')
        if is_showing_power_msgbox(): # If Power Menu Open
            if page_index==3: # Shutdown - no
                update_page_index(4)
            else:
                update_page_index(3)
            draw_page()
        else:
            if page_index==0 and pageSleepCountdown>0: # Home
                update_page_index(6)
            else:
                pageIndex=0
        draw_page()

    if signum == signal.SIGUSR2:
        print ('K2 pressed')
        if is_showing_power_msgbox(): # If Power Menu Open
            if page_index==4: # Shutdown
                update_page_index(5)
            else:
                update_page_index(0)
            draw_page()

        elif is_showing_wifi_msgbox(): # If Wifi Menu Open
            if page_index==6: # Change Wifi to Wifi Client
                update_page_index(9)
            elif page_index==7: # Change Wifi to Hotspot
                update_page_index(10)
            elif page_index==8: # Change Wifi NanoGate
                update_page_index(11)
            else:
                update_page_index(0)
            draw_page()

        elif is_showing_backup_msgbox(): # Backup Menu Open
            if page_index==1: # Update
                update_page_index(15)
            elif page_index==12: # Backup
                update_page_index(16)
            elif page_index==13: # Restore
                update_page_index(17)
            elif page_index==14: # Check
                update_page_index(18)
            else:
                update_page_index(0)
            draw_page()    

        else:
            update_page_index(1)
        draw_page()

    if signum == signal.SIGALRM:
        print ('K3 pressed')
        if is_showing_power_msgbox(): # If Power Menu Open
            update_page_index(0)
            draw_page()

        elif is_showing_wifi_msgbox(): # If Wifi Menu Open
            if page_index==6: # Wifi Client
                update_page_index(7)
            elif page_index==7: # Hotspot
                update_page_index(8)
            elif page_index==8: # NanoGate
                update_page_index(6)
            draw_page()

        elif is_showing_backup_msgbox(): # Backup Menu Open
            if page_index==1: # Update
                update_page_index(12)
            elif page_index==12: # Backup
                update_page_index(13)
            elif page_index==13: # Restore
                update_page_index(14)
            elif page_index==14: # Check
                update_page_index(1)
            draw_page()            

        else:
            update_page_index(3)
        draw_page()

    pageSleepCountdown = pageSleep #user pressed a button, reset the sleep counter

image0 = Image.open('nano_home_logo_oled.png').convert('1')
oled.drawImage(image0)
time.sleep(5)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGALRM, receive_signal)

while True:
    try:
        draw_page()

        lock.acquire()
        page_index = pageIndex
        lock.release()

        if page_index==5:
            while True:
                lock.acquire()
                is_drawing = drawing
                lock.release()
                if not is_drawing:
                    lock.acquire()
                    drawing = True
                    lock.release()
                    oled.clearDisplay()
                    break
                else:
                    time.sleep(.1)
                    continue
            time.sleep(0.2)
            os.system('systemctl poweroff') # Poweroff
            break
        elif page_index==9:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('mount_emmc root') # mount emmc
            os.system('cp -rf /mnt/emmc_root/etc/wpa_supplicant/wpa_supplicant.conf.wificlient /etc/wpa_supplicant/wpa_supplicant.conf.wificlient') # copy wifclient config
            os.system('wmod -wificlient') # Change Wifi Mode - Wifi Client
            os.system('mount_emmc unmount') # unmount emmc
            update_page_index(0)
            draw_page()
        elif page_index==10:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('wmod -hotspot &') # Change Wifi Mode - Hotspot
            time.sleep(2)
            update_page_index(0)
            draw_page()
        elif page_index==11:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('mount_emmc root') # mount emmc
            os.system('cp -rf /mnt/emmc_root/etc/wpa_supplicant/wpa_supplicant.conf.nanogate /etc/wpa_supplicant/wpa_supplicant.conf.nanogate') # copy wifclient config
            os.system('wmod -nanogate') # Change Wifi Mode - NanoGate
            os.system('mount_emmc unmount') # unmount emmc
            time.sleep(2)
            update_page_index(0)
            draw_page()
        elif page_index==15:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('nanohome_update &') # Update
            time.sleep(2)
            update_page_index(19)
            draw_page()
        elif page_index==16:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('system-backup &') # Backup
            time.sleep(2)
            update_page_index(18)
            draw_page()
        elif page_index==17:
            lock.acquire()
            is_drawing = drawing
            lock.release()
            os.system('system-restore &') # Restore
            time.sleep(2)
            update_page_index(18)
            draw_page()
        time.sleep(0.2)
    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
