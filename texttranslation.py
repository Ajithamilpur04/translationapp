from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")  # Get the input text
    cl = choose_language1.get()  # Get the chosen input language
    tl = choose_language2.get()  # Get the chosen output language
    
    if lang_1 == '':
        # Show error message if no text is entered
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        # Clear the output text entry
        text_entry2.delete("1.0", "end")
        
        # Translate the text
        translator = Translator()
        output = translator.translate(lang_1, src=cl, dest=tl)
        
        # Insert the translated text into the output text entry
        text_entry2.insert("end", output.text)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

root = tk.Tk()
root.title('Language Translator')
root.geometry('800x370')

label_title = Label(root, text="Language Translator", font=("Helvetica", 20, "bold"), fg="#248aa2")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

frame1 = tk.Frame(root, relief='ridge', borderwidth=5, bg="#f5f5f5")
frame1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add labels for input and output
label_input = Label(frame1, text="Input Text:", font=('Verdana', 12, 'bold'))
label_input.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

label_output = Label(frame1, text="Translated Text:", font=('Verdana', 12, 'bold'))
label_output.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")

text_entry1 = Text(frame1, width=40, height=10, borderwidth=5, relief='ridge', font=('verdana', 15))
text_entry1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

text_entry2 = Text(frame1, width=40, height=10, borderwidth=5, relief='ridge', font=('verdana', 15))
text_entry2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

languages_list = list(LANGUAGES.values())
languages_list.insert(0, 'Choose language')

choose_language1 = ttk.Combobox(frame1, width=30, values=languages_list, state='readonly', font=('Verdana', 10, 'bold'))
choose_language1.current(0)
choose_language1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

choose_language2 = ttk.Combobox(frame1, width=30, values=languages_list, state='readonly', font=('Verdana', 10, 'bold'))
choose_language2.current(0)
choose_language2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

btn1 = tk.Button(frame1, command=translate, text="Translate", relief='raised', font=('verdana', 10, 'bold'), bg='#248aa2', fg="white", width=20)
btn1.grid(row=2, column=0, padx=10, pady=10)

btn2 = tk.Button(frame1, command=clear, text="Clear", relief='raised', font=('verdana', 10, 'bold'), bg='#248aa2', fg="white", width=20)
btn2.grid(row=2, column=1, padx=10, pady=10)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)

root.mainloop()
