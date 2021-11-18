import time #importa a data do sistema
import pyautogui
import threading # fazer com que a sua aplicação execute tarefas de forma assíncrona
from pynput.keyboard import Listener, KeyCode #controlar e monitorar o teclado

start_stop_key = KeyCode(char='.') # é a chave para iniciar e parar o auto clicker
exit_key = KeyCode(char=',') # é a chave para fechar o programa
palavras = "vai se fude gustavo"
delay = 0.5

class spamfodase(threading.Thread):
	def __init__ (self, delay): 
		super().__init__()
		self.delay = delay
		self.running = False
		self.program_running = True
	def start_spam(self):
		self.running = True
	def stop_spam(self):
		self.running = False
	def exit(self):
		self.stop_spam()
		self.program_running = False
	def run(self):
		while self.program_running:
			while self.running:
				time.sleep(self.delay)
				pyautogui.typewrite(palavras)
				pyautogui.press("enter")

spam_thread = spamfodase(delay)
spam_thread.start()

def on_press(key):
	if key == start_stop_key:
		if spam_thread.running:
			spam_thread.stop_spam()
		else:
			spam_thread.start_spam()
	elif key == exit_key:
		spam_thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()