import customtkinter as ctk
import binary_calculator as binary

window = ctk.CTk()

# Window
window.title("Binary Calculator")
window.geometry("500x600+500+150")
window.resizable(False,False)


# Title
text_title = ctk.CTkLabel(window,text="Binary Calculator",font=("Segoe UI",30,"bold"))
text_title.pack(pady = 10)

# Entry Box (Input)
entry_binary = ctk.CTkEntry(window, width=300, height=25)
entry_binary.place(x=100, y=150)

# Entry Box Title
text_binary = ctk.CTkLabel(window,text="Enter binary number (Ex: 00001):",font=("Segoe UI",16))
text_binary.place(x=100, y=120)

# Button (Enter)
def enter():
    try:
        binary_number = entry_binary.get()
        answer = binary.calculate(binary_number)
        text_answer.configure(text=answer)
    except:
        text_answer.configure(text="Error")
    finally:
        if binary_number == "":
            text_answer.configure(text="")
        if "2" in binary_number or "3" in binary_number or "4" in binary_number or "5" in binary_number or "6" in binary_number or "7" in binary_number or "8" in binary_number or "9" in binary_number:
            text_answer.configure(text="Error")
    
    
button_enter = ctk.CTkButton(text="Enter",fg_color="#0EEA00",hover_color=("#3CC600","#39BD00"),command=enter,master=window,width=100,font=("Segoe UI",15,"bold"))  #? veriyi almak için buton kullanıyoruz.
button_enter.place(x=300,y=180)

# Button (Clear)
def clear():
    entry_binary.delete(0,"end")
    text_answer.configure(text="")

button_clear = ctk.CTkButton(text="Clear",fg_color="red",hover_color="#BD0000",command=clear,master=window,width=100,font=("Segoe UI",15,"bold"))
button_clear.place(x=100,y=180)


# Output
text_answer = ctk.CTkLabel(window,text="",font=("Segoe UI",20,"bold"))
text_answer.place(relx=0.5, rely=0.6, anchor="center")

text_line = ctk.CTkLabel(window,text="___________________________________________________")
text_line.place(x=100, y=380)

frame = ctk.CTkFrame(window,corner_radius=10)
frame.place(x=140,y=410)

current_mode = ctk.IntVar()
current_mode.set(0)

# Karanlık mod için fonksiyon
def toggle_mode():
    if current_mode.get() == 0:
        ctk.set_appearance_mode("dark")
        current_mode.set(1)  # Karanlık Moda geçiş
    else:
        ctk.set_appearance_mode("light")
        current_mode.set(0)

switch = ctk.CTkSwitch(frame,
                       text="Turn On Dark Mode",
                       fg_color="red",
                       progress_color="lime",
                       switch_width= 50,
                       switch_height= 20,font=("Segoe UI",15),
                       command= toggle_mode)
switch.pack(padx = 10, pady = 7)

window.mainloop()