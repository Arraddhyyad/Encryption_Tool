import tkinter as tk
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = tk.Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        message = text1.get(1.0, tk.END).strip()
        print(f"Original message: {message}")  

        try:
           
            while len(message) % 4 != 0:
                message += "="
                
            decode_message = message.encode("utf-8")
            base64_bytes = base64.b64decode(decode_message)
            decrypted_message = base64_bytes.decode("utf-8")
            print(f"Decrypted message: {decrypted_message}") 

            tk.Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = tk.Text(screen2, font="Roboto 10", bg="white", fg="black", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(tk.END, decrypted_message)
        except Exception as e:
            messagebox.showerror("Decryption", f"An error occurred during decryption: {str(e)}")
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = tk.Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#00bd56")

        message = text1.get(1.0, tk.END).strip()
        print(f"Original message: {message}") 

        try:
            encode_message = message.encode("utf-8")
            base64_bytes = base64.b64encode(encode_message)
            encrypted_message = base64_bytes.decode("utf-8")
            print(f"Encrypted message: {encrypted_message}")  

            tk.Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = tk.Text(screen1, font="Roboto 10", bg="white", fg="black", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(tk.END, encrypted_message)
        except Exception as e:
            messagebox.showerror("Encryption", f"An error occurred during encryption: {str(e)}")
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")

def create_custom_button(canvas, text, command, x, y, width, height, bg, fg):
    button = canvas.create_rectangle(x, y, x + width, y + height, fill=bg, outline=bg)
    label = canvas.create_text(x + width / 2, y + height / 2, text=text, fill=fg, font=("georgia", 12))
    canvas.tag_bind(button, "<Button-1>", lambda event: command())
    canvas.tag_bind(label, "<Button-1>", lambda event: command())

def reset():
    code.set("")
    text1.delete(1.0, tk.END)

def main_screen():
    global screen, code, text1

    screen = tk.Tk()
    screen.geometry("500x500")
    screen.title("KeyIt")

    try:
        image_icon = tk.PhotoImage(file="image.jpeg")
        screen.iconphoto(False, image_icon)
    except tk.TclError:
        print("Icon file not found, skipping icon setting.")

    canvas = tk.Canvas(screen, width=500, height=500)
    canvas.place(x=0, y=0)

    tk.Label(text="Enter text for encryption and decryption", fg="black", font=("georgia", 13)).place(x=10, y=10)
    text1 = tk.Text(font="Roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text1.place(x=10, y=50, width=480, height=100)

    tk.Label(text="Enter secret key for encryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = tk.StringVar()
    tk.Entry(textvariable=code, width=19, bd=0, font=("georgia", 25), show="*").place(x=10, y=200)

    create_custom_button(canvas, 'ENCRYPT', encrypt, 10, 250, 150, 50, "#ed3833", "white")
    create_custom_button(canvas, 'DECRYPT', decrypt, 200, 250, 150, 50, "#00bd56", "white")
    create_custom_button(canvas, 'RESET', reset, 10, 310, 460, 50, "#1089ff", "white")

    screen.mainloop()

print(tk.TkVersion)

main_screen()
