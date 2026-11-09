import tkinter as tk 
import pygame



window=tk.Tk()
window.title('random code')
window.geometry('405x400')
window.configure(bg='#14241b')
window.resizable(0,0)


img_for = tk.PhotoImage(file="4b1513017043b475cf86cd044e8b9071.png").subsample(8,7)

label_bg = tk.Label(window, image=img_for,bd=0)
label_bg.place(x=50, y=20)

spisok=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
         "U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

def generation_code():
    
    block_1 = entry_input.get().upper()

    
    if len(block_1) != 5:
        lbl_result.config(text="Ошибка: введите 5 знаков")
        return

    
    block_2 = ""
    block_3 = ""

    
    for char in block_1:
        if char not in spisok:
            lbl_result.config(text="Недопустимый символ!")
            return

        index = spisok.index(char) 
        new_index = (index + 3) % len(spisok) 
        block_2 = block_2 + spisok[new_index] 

    
    for char in block_1:
        index = spisok.index(char)
        new_index = (index - 5) % len(spisok) 
        block_3 = block_3 + spisok[new_index]

    
    full_key = block_1 + "-" + block_2 + "-" + block_3
    lbl_result.config(text=full_key)




lbl_input = tk.Label(
    window,
    text="Введите 1-й блок",
    font=("Consolas", 11, "bold"),
    bg="#111111",
    fg="#2ed573",
)
lbl_input.place(x=120, y=300)

entry_input = tk.Entry(
    window,
    font=("Consolas", 14, "bold"),
    justify="center",
    width=10,
    bg="#111111",
    fg="#2ed573",
    insertbackground="white",
)
entry_input.place(x=140, y=330)

btn = tk.Button(
    window,
    text="Сгенерировать ключ",
    font=("Consolas", 12, "bold"),
    bg="#111111",
    fg="#2ed573",command=generation_code, 
    
)
btn.place(x=105, y=360)


lbl_result = tk.Label(
    window,
    text="XXXXX-XXXXX-XXXXX",
    font=("Consolas", 25, "bold"),
    bg="#111111",
    fg="#2ed573",
    padx=10,
    pady=5,
)
lbl_result.place(x=35, y=245)


pygame.mixer.init()
pygame.mixer.music.load("Bad Piggies .mp3")
pygame.mixer.music.play(-1)


window.mainloop()
