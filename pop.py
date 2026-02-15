import customtkinter as CTk

# Настройка темы
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

root = CTk.CTk()
root.geometry("640x480")
root.title("hi")


tabview = CTk.CTkTabview(root)
tabview.pack(padx=20, pady=20, fill="both", expand=True)
tab_doc = tabview.add("Привет!")
tab_grv = tabview.add("сила тяжести")
tab_wpr = tabview.add("давление воды")


# grv
def grv():
    val = en_grv.get()
    num = float(val)
    res = num * 9.81

    lab_grv.configure(text= f"Результат: {res:.2f}")

en_grv = CTk.CTkEntry(tab_grv, justify="left", width=200, height=30, placeholder_text="введите массу", placeholder_text_color="gray")
en_grv.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

btn_grv = CTk.CTkButton(tab_grv, text="расчитать", command=grv, width=200, height=30)
btn_grv.grid(row= 1, column=0, columnspan=4, padx=10, pady=10)

lab_grv = CTk.CTkLabel(tab_grv,text="", width=200, height=30)
lab_grv.grid(row=2, column=0, columnspan=4, padx=10, pady=10)


# wpr 
def wpr():
    val1 = en_wpr.get()
    val2 = en2_wpr.get()
    num1 = float(val1)
    num2 = float(val2)
    res = num1 * num2 * 9.81

    lab_wpr.configure(text= f"Результат: {res}(Паскаль)")


en_wpr = CTk.CTkEntry(tab_wpr, justify="left", width=200, height=30, placeholder_text="введите высоту", placeholder_text_color="gray")
en_wpr.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
en2_wpr = CTk.CTkEntry(tab_wpr, justify="left", width=200, height=30, placeholder_text="введите плотсноть", placeholder_text_color="gray")
en2_wpr.grid(row=1, column=0, columnspan=4, padx=10, pady=20)

btn_wpr = CTk.CTkButton(tab_wpr, text="расчитать", command=wpr, width=200, height=30)
btn_wpr.grid(row=2, column=0, columnspan=4, padx=10, pady=10)


lab_wpr = CTk.CTkLabel(tab_wpr, text="", width=200, height=30)
lab_wpr.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# doc
my_font = CTk.CTkFont(family="Arial", size=24, weight="bold")

Lab_doc = CTk.CTkLabel(tab_doc, text="Привет!", width=300, height=10, font=my_font, anchor="w")
Lab_doc.grid(row=6, column=1, columnspan=4, padx=10, pady=10, sticky="nsew")

lab_doc2 = CTk.CTkLabel(tab_doc, text="Это мой калькулятор по физике", anchor="w")
lab_doc2.grid(row=7 ,column=1, columnspan=4, padx=3, pady=3, sticky="nsew")

lab_doc3 = CTk.CTkLabel(tab_doc, text="формулы которые используються: P=pgh,F=mg", anchor="w")
lab_doc3.grid(row=8 ,column=1, columnspan=4, padx=3, pady=3, sticky="nsew")






