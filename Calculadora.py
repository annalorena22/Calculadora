from PIL import Image
import customtkinter

janelao = customtkinter.CTk()
janelao.configure(bg='#2E2E2E')
janelao.title("Calculadora")
janelao.geometry("370x600")
janelao.maxsize(370,600)
janelao.minsize(370,600)
customtkinter.set_appearance_mode("dark")

calculadora = customtkinter.CTkFrame(janelao)

janelao.mainloop()
