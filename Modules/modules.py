#!/usr/bin/python3

import os 
import sys
import subprocess


def main():
  print('Linux')
  print('Mac')
  print('Windows')
  
  menu_input = int(input(":"))
  if menu_input==1:
    linux()
  elif menu_input==2:
    mac()
   elif menu_input==3:
    windows()
   else:
    print("Sorry!")
   
def linux():
  subprocess.call(['pip3','install','argparse'])
  subprocess.call(['pip3','install','colorama'])
  subprocess.call(['pip3','install','requests'])
  subprocess.call(['pip3','install','sys'])
  subprocess.call(['pip3','install','os'])
  
  
  
  
def mac():
  subprocess.call(['pip3','install','argparse'])
  subprocess.call(['pip3','install','colorama'])
  subprocess.call(['pip3','install','requests'])
  subprocess.call(['pip3','install','sys'])
  subprocess.call(['pip3','install','os'])
  
  
def windows():
  subprocess.call(['pip3','install','argparse'])
  subprocess.call(['pip3','install','colorama'])
  subprocess.call(['pip3','install','requests'])
  subprocess.call(['pip3','install','sys'])
  subprocess.call(['pip3','install','os'])
  
  
  
  
main()

  
