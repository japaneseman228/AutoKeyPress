import tkinter as tk
import threading
import time
import keyboard
import pyautogui

running = False

def start_clicking():
    global running
    if running:
        running = False
        status_label.config(text="Остановлено", fg="red")
    else:
        running = True
        status_label.config(text="Работает...", fg="green")
        threading.Thread(target=click_loop, daemon=True).start()

def click_loop():
    global running
    key_a = entry_key1.get()
    key_b = entry_key2.get()
    while running:
        pyautogui.press(key_a)
        time.sleep(0.1)
        pyautogui.press(key_b)
        time.sleep(0.1)

def on_hotkey():
    start_clicking()

keyboard.add_hotkey("F6", on_hotkey)

root = tk.Tk()
root.title("Auto Key Presser")
root.geometry("300x200")

tk.Label(root, text="Клавиша A:").pack(pady=5)
entry_key1 = tk.Entry(root)
entry_key1.insert(0, "a")
entry_key1.pack()

tk.Label(root, text="Клавиша B:").pack(pady=5)
entry_key2 = tk.Entry(root)
entry_key2.insert(0, "d")
entry_key2.pack()

status_label = tk.Label(root, text="Ожидание...", fg="gray")
status_label.pack(pady=10)

tk.Label(root, text="Нажми F6 для Старт/Стоп").pack(pady=5)

root.mainloop()
