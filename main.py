import tkinter as tk

def on_button_click():
    print("Кнопка нажата!")

root = tk.Tk()
root.title("Простое приложение на Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Привет, мир!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()

root.mainloop()
