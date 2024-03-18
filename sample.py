from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{500}x{450}")

        self.task_entry = customtkinter.CTkEntry(self, width=300, placeholder_text="Add new Task")
        self.task_entry.grid(row=0, column=0, padx=(20, 0), pady=(20, 20))

        self.main_button_1 = customtkinter.CTkButton(master=self, border_width=2, text="Add Task", command=self.addTask)
        self.main_button_1.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.listbox = customtkinter.CTkScrollableFrame(self, width=350)
        self.listbox.grid(row=4, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

    def addTask(self):
        if self.task_entry.get() == "":
            messagebox.showerror("Input Error", "Invalid Task Entry")
            return 0
        else:
            task = self.task_entry.get()
            self.task_entry.delete(0, customtkinter.END)

            self.todo = customtkinter.CTkLabel(self.listbox, text=task, cursor="hand2")
            self.todo.grid(sticky="w", column=0, pady=(10, 0))

            with open("tasklist.txt", 'a') as taskfile:
                taskfile.write(f"\n{task}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
