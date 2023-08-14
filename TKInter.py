from struct import pack
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json
def show_tab(tab_index):
    tab_control.select(tab_index)

def send_opening_request():
    url = "https://192.168.1.102/opening_request"  # Reemplaza con la URL de la API real
    data = {"code": input_text.get("1.0", "end-1c")}  # Obtiene el texto del cuadro de texto
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    json_data = json.dumps(data)
    response = requests.post(url, json=data,verify=False)
    
    if response.status_code == 200:
        response_label.config(text="Respuesta: " + response.text)
    else:
        response_label.config(text="Error en la solicitud POST")

def get_cell_state():
    url = "https://192.168.1.102/get_cell_state"  # Reemplaza con la URL de la API real
    data1 = {"cell": input_text1.get("1.0", "end-1c")}  # Obtiene el texto del cuadro de texto
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    json_data = json.dumps(data1)
    response = requests.post(url, json=data1,verify=False)
    print(data1)
    if response.status_code == 200:
        response_label1.config(text="Respuesta: " + response.text)
    else:
        response_label1.config(text="Error en la solicitud POST")

def get_code_request():
    url = "https://192.168.1.102/code_request"  # Reemplaza con la URL de la API real
    data2 = {"cell": input_text2.get("1.0", "end-1c")}  # Obtiene el texto del cuadro de texto
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    json_data = json.dumps(data2)
    response = requests.post(url, json=data2,verify=False)
    if response.status_code == 200:
        response_label2.config(text="Respuesta: " + response.text)
    else:
        response_label2.config(text="Error en la solicitud POST")

def update_code():
    url = "https://192.168.1.102/update_code"  # Reemplaza con la URL de la API real
    data2 = {"cell": input_text3.get("1.0", "end-1c"),"code":input_text4.get("1.0", "end-1c")}  # Obtiene el texto del cuadro de texto
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    json_data = json.dumps(data2)
    response = requests.post(url, json=data2,verify=False)
    if response.status_code == 200:
        response_label3.config(text="Respuesta: " + response.text)
    else:
        response_label3.config(text="Error en la solicitud POST")

def go_to_home():
    tab_control.select(0)  # Índice de la pestaña de inicio

root = tk.Tk()
root.title("Vending Machine")

# Ajustar el tamaño de la ventana principal
root.geometry("900x600")  # Ancho x Alto

tab_control = ttk.Notebook(root)

# Crear la pestaña de inicio
home_tab = ttk.Frame(tab_control)
tab_control.add(home_tab, text='Inicio')

# Personalización de colores y fuentes
style = ttk.Style()
style.configure("TNotebook", background="#f0f0f0")
style.configure("TNotebook.Tab", background="#a0a0a0", padding=[15, 5], font=("Helvetica", 14, "bold"))
style.map("TNotebook.Tab", background=[("selected", "#ffffff")])

# Agregar el título y la imagen en la pestaña de inicio
title_label = tk.Label(home_tab, text="Vending Machine", font=("Helvetica", 36, "bold"), fg="#333333", pady=20)
title_label.pack()

image = Image.open("MicrosoftTeams-image (18).jpg")  
image = image.resize((400, 400))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(home_tab, image=photo)
image_label.photo = photo
image_label.pack()

# Agregar pestañas adicionales y botones de imagen
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Abrir Locker')
tab_control.add(tab2, text='Estado de Locker')
tab_control.add(tab3, text='nombre del locker')
tab_control.add(tab4, text='update')

button_frame = tk.Frame(root)
button_frame.pack()
button_home_image = Image.open("MicrosoftTeams-image (14).png")  # Reemplaza con la ruta de tu imagen para el botón de inicio
button_home_image = button_home_image.resize((70, 70))
button_home_photo = ImageTk.PhotoImage(button_home_image)
button_home = tk.Button(button_frame, image=button_home_photo, command=go_to_home)
button_home.image = button_home_photo
button_home.pack(side="left", padx=10, pady=10)

button1_image = Image.open("MicrosoftTeams-image (17).png")  # Reemplaza con la ruta de tu imagen
button1_image = button1_image.resize((70, 70))
button1_photo = ImageTk.PhotoImage(button1_image)
button1 = tk.Button(button_frame, image=button1_photo, command=lambda: show_tab(1))  # Cambiado a 1
button1.image = button1_photo
button1.pack(side="left", padx=10, pady=10)

button2_image = Image.open("MicrosoftTeams-image (15).png")  # Reemplaza con la ruta de tu imagen
button2_image = button2_image.resize((70, 70))
button2_photo = ImageTk.PhotoImage(button2_image)
button2 = tk.Button(button_frame, image=button2_photo, command=lambda: show_tab(2))  # Cambiado a 2
button2.image = button2_photo
button2.pack(side="left", padx=10, pady=10)

button3_image = Image.open("MicrosoftTeams-image (16).png")  # Reemplaza con la ruta de tu imagen
button3_image = button3_image.resize((70, 70))
button3_photo = ImageTk.PhotoImage(button3_image)
button3 = tk.Button(button_frame, image=button3_photo, command=lambda: show_tab(3))  # Cambiado a 3
button3.image = button3_photo
button3.pack(side="left", padx=10, pady=10)

button4_image = Image.open("MicrosoftTeams-image (13).png")  # Reemplaza con la ruta de tu imagen
button4_image = button4_image.resize((70, 70))
button4_photo = ImageTk.PhotoImage(button4_image)
button4 = tk.Button(button_frame, image=button4_photo, command=lambda: show_tab(4))  # Cambiado a 4
button4.image = button4_photo
button4.pack(side="left", padx=10, pady=10)


tab_control.pack(expand=1, fill="both")

input_text = tk.Text(tab1, height=5, width=40, font=("Helvetica", 12))
input_text.pack(padx=10, pady=10)

send_button = tk.Button(tab1, text="Abrir Celda", command=send_opening_request, font=("Helvetica", 14), bg="#4CAF50", fg="white")
send_button.pack(padx=10, pady=10)

response_label = tk.Label(tab1, text="Confirmación aparecerá aquí", font=("Helvetica", 14), fg="#333333")
response_label.pack(padx=10, pady=10)

tab_control.pack(expand=1, fill="both")

input_text1 = tk.Text(tab2, height=5, width=40, font=("Helvetica", 12))
input_text1.pack(padx=10, pady=10)

send_button1 = tk.Button(tab2, text="saber estado de la celda", command=get_cell_state, font=("Helvetica", 14), bg="#4CAF50", fg="white")
send_button1.pack(padx=10, pady=10)

response_label1 = tk.Label(tab2, text="el estado de la celda aparecera", font=("Helvetica", 14), fg="#333333")
response_label1.pack(padx=10, pady=10)

tab_control.pack(expand=1, fill="both")

input_text2 = tk.Text(tab3, height=5, width=40, font=("Helvetica", 12))
input_text2.pack(padx=10, pady=10)

send_button2 = tk.Button(tab3, text="saber nombre de la celda", command=get_code_request, font=("Helvetica", 14), bg="#4CAF50", fg="white")
send_button2.pack(padx=10, pady=10)

response_label2 = tk.Label(tab3, text="el nombre de la celda aparecera aqui", font=("Helvetica", 14), fg="#333333")
response_label2.pack(padx=10, pady=10)

tab_control.pack(expand=1, fill="both")

label1 = tk.Label(tab4, text="Ingresa el numero celda que deseas actualizar:", font=("Helvetica", 12))
label1.pack(padx=10, pady=(10, 0))  # Se ajusta el relleno vertical para separar la etiqueta

input_text3 = tk.Text(tab4, height=5, width=40, font=("Helvetica", 12))
input_text3.pack(padx=10, pady=5)

# Agregar una etiqueta para el segundo cuadro de entrada
label2 = tk.Label(tab4, text="Ingresa el codigo nuevo:", font=("Helvetica", 12))
label2.pack(padx=10, pady=(10, 0))  # Se ajusta el relleno vertical para separar la etiqueta

input_text4 = tk.Text(tab4, height=5, width=40, font=("Helvetica", 12))
input_text4.pack(padx=10, pady=5)

send_button3 = tk.Button(tab4, text="actualizar", command=update_code, font=("Helvetica", 14), bg="#4CAF50", fg="white")
send_button3.pack(padx=10, pady=10)

response_label3 = tk.Label(tab4, text="nombre actualizado", font=("Helvetica", 14), fg="#333333")
response_label3.pack(padx=10, pady=10)


root.mainloop()
