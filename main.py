#! python3

import warnings, cv2, time, sys, pyautogui, traceback
from time import sleep, perf_counter
warnings.filterwarnings("ignore")
import os
import pydirectinput

def locate_and_click_once(_image_path_):
  #print(_image_path_)
  _location_ = pyautogui.locateCenterOnScreen(_image_path_)
  pyautogui.click(_location_)

def locate_and_click(_image_path_):
  #print(_image_path_)
  _location_ = None
  while _location_ == None:
    _location_ = pyautogui.locateCenterOnScreen(_image_path_, confidence=0.8)
  pyautogui.click(_location_)

def bring_nfs_foreground():
  _found_window_ = False
  while not _found_window_ :
    time.sleep(5)
    if pyautogui.getWindowsWithTitle("Need for Speed™"):
      pyautogui.getWindowsWithTitle("Need for Speed™")[0].activate()
      print('found NFS window')
      _found_window_ = True    

def d3d_hotkey(key):
  pydirectinput.keyDown(key)
  time.sleep(0.1)
  pydirectinput.keyUp(key)
  time.sleep(0.25)
 
def wait_for_login_screen():
  print_notice('Waiting for Press to continue screen')
  bring_nfs_foreground()
  
  locate_and_click('nfs_1.png')
  d3d_hotkey('space')

def wait_for_play_screen():
  print_notice('Waiting for Play menu screen')
  bring_nfs_foreground()
  
  locate_and_click('nfs_2.png')
  d3d_hotkey('enter')
  d3d_hotkey('enter')

def wait_for_garage():
  print_notice('Waiting for Garage screen')
  bring_nfs_foreground()
  locate_and_click('nfs_3.png')
  d3d_hotkey('enter')
  d3d_hotkey('left')
  d3d_hotkey('left')
  d3d_hotkey('enter')
  for _ in range(15):
    print('trying to sell this part')
    d3d_hotkey('enter')
    if pyautogui.locateCenterOnScreen('sell.png', confidence=0.8) == None:
      print('moved to sell button')
      d3d_hotkey('down')
    
    d3d_hotkey('enter')
    d3d_hotkey('enter')
    print_notice('sold this part')
    time.sleep(3)

def launch_nfs_steam():
   os.startfile('steam://rungameid/1262540')  

def close_nfs():
   os.system("taskkill /im NFS16.exe")
   print_notice('waiting 15s for nfs to close')
   time.sleep(15)

def send_notice(string):
   import subprocess
   cmd = f'[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms");$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon;$objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information;$objNotifyIcon.BalloonTipIcon = "Info";$objNotifyIcon.BalloonTipText = "{string}";$objNotifyIcon.BalloonTipTitle = "Python3";$objNotifyIcon.Visible = $True;$objNotifyIcon.ShowBalloonTip(10000)'
   subprocess.run(["powershell", "-Command", cmd], capture_output=True)

def print_notice(string):
  print(string)
  send_notice(string) 

def is_root():
   return os.getuid() == 0

# Main function
if __name__=='__main__':
    from elevate import elevate
    elevate()
    pyautogui.FAILSAFE = False
    while True:
      launch_nfs_steam()
      wait_for_login_screen()
      wait_for_play_screen()
      wait_for_garage()
      close_nfs()

    sys.exit()