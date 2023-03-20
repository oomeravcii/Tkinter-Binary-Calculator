import tkinter as tk
import binary_calculator as binary

window = tk.Tk()

# Window
window.title("Binary Calculator")
window.geometry("500x600+500+150")
window.resizable(False,False)

# Title
text_title = tk.Label(window,text="Binary Calculator",font="Roboto 20 bold")
text_title.pack()

# Entry Box (Input)
entry_binary = tk.Entry(window)
entry_binary.place(x=100, y=150, width=300, height=25)

# Entry Box Title
text_binary = tk.Label(window,text="Entry binary number (Ex: 00001):",font="Roboto 10")
text_binary.place(x=100, y=128)

# Button (Enter)
def enter():
    try:
        binary_number = entry_binary.get()
        answer = binary.calculate(binary_number)
        text_answer.config(text=answer)
    except:
        text_answer.config(text="Error")
    finally:
        if binary_number == "":
            text_answer.config(text="")
        if "2" in binary_number or "3" in binary_number or "4" in binary_number or "5" in binary_number or "6" in binary_number or "7" in binary_number or "8" in binary_number or "9" in binary_number:
            text_answer.config(text="Error")
    
    
button_enter = tk.Button(text="Enter",fg="white",bg="black",activebackground="lime",command=enter)  #? veriyi almak için buton kullanıyoruz.
button_enter.place(x=300,y=180,width=100)

# Button (Clear)
def clear():
    entry_binary.delete(0,"end")
    text_answer.config(text="")

button_clear = tk.Button(text="Clear",fg="white",bg="black",activebackground="red",command=clear)
button_clear.place(x=100,y=180,width=100)


# Output
text_answer = tk.Label(window,text="",font="Roboto 20 bold")
text_answer.place(x=100, y=350)

text_line = tk.Label(window,text="___________________________________________________________")
text_line.place(x=100, y=380)

window.mainloop()