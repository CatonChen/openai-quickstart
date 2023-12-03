'''
通过gpt-3.5-turbo生成的代码
使用tk库生成图形化界面
'''

import tkinter as tk
from tkinter import filedialog
import subprocess



def translate():
    api_key = api_key_entry.get()
    model_type = model_type_combobox.get()
  
    if model_type == "OpenAIModel":
        openai_model = openai_model_combobox.get()
        model_url = ""
    else:
        openai_model = ""
        model_url = model_url_entry.get()
        
    file_format = file_format_combobox.get()
    book = book_entry.get()

    # 生成执行程序的命令
    command = f'python ai_translator/main.py --model_type {model_type} --openai_api_key $OPENAI_API_KEY --file_format {file_format} --book {book} --openai_model {openai_model}'
    
    # 执行命令
    subprocess.run(command, shell=True)
    
def browse_file():
    book = filedialog.askopenfilename()
    book_entry.delete(0, tk.END)
    book_entry.insert(tk.END, book)
    
def show_api_key():
    api_key = api_key_entry.get()
    masked_api_key_label.configure(text="API Key: "+"*" * len(api_key))
    
root = tk.Tk()
root.title("AI Translator")

# 创建控件并放置在窗口中
api_key_label = tk.Label(root, text="API Key:")
api_key_label.pack()
api_key_entry = tk.Entry(root, show='*')
api_key_entry.pack()
api_key_show_button = tk.Button(root, text="Show", command=show_api_key)
api_key_show_button.pack()
masked_api_key_label = tk.Label(root, text="API Key: ")
masked_api_key_label.pack()

model_type_label = tk.Label(root, text="Model Type:")
model_type_label.pack()
model_type_combobox = tk.ttk.Combobox(root, values=["OpenAIModel", "GLMModel"])
model_type_combobox.pack()
model_type_combobox.bind("<<ComboboxSelected>>", lambda event: openai_model_combobox.configure(state=tk.NORMAL) if model_type_combobox.get() == "OpenAIModel" else openai_model_combobox.configure(state=tk.DISABLED))

openai_model_label = tk.Label(root, text="OpenAI Model:")
openai_model_label.pack()
openai_model_combobox = tk.ttk.Combobox(root, state=tk.DISABLED, values=["gpt-3.5-turbo", "gpt-4.0"])
openai_model_combobox.pack()

model_url_label = tk.Label(root, text="Model URL:")
model_url_label.pack()
model_url_entry = tk.Entry(root, state=tk.DISABLED)
model_url_entry.pack()

file_format_label = tk.Label(root, text="File Format:")
file_format_label.pack()
file_format_combobox = tk.ttk.Combobox(root, values=["markdown", "PDF"])
file_format_combobox.pack()

book_label = tk.Label(root, text="Book:")
book_label.pack()
book_entry = tk.Entry(root)
book_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

translate_button = tk.Button(root, text="开始翻译", command=translate)
translate_button.pack()

def quit_program():
    root.quit()

quit_button = tk.Button(root, text="退出程序", command=quit_program)
quit_button.pack()

root.mainloop()