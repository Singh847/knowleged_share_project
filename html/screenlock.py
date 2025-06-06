import tkinter as tk

class ScreenLock9x9:
    def __init__(self, root):
        self.root = root
        self.root.title("9x9 Screen Lock Pattern")
        self.size = 9
        self.buttons = []
        self.pattern = []

        self.create_grid()

    def create_grid(self):
        for row in range(self.size):
            row_buttons = []
            for col in range(self.size):
                btn = tk.Button(
                    self.root, text="", width=3, height=1,
                    command=lambda r=row, c=col: self.select_point(r, c),
                    font=("Arial", 12, "bold"),
                    relief="raised",
                    bg="lightgray"
                )
                btn.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def select_point(self, row, col):
        point_num = row * self.size + col + 1
        if point_num not in self.pattern:
            self.pattern.append(point_num)
            btn = self.buttons[row][col]
            btn.config(bg="skyblue", text=str(len(self.pattern)))
        else:
            # If clicked again, remove the point and update
            self.pattern.remove(point_num)
            self.update_buttons()

    def update_buttons(self):
        for row in range(self.size):
            for col in range(self.size):
                point_num = row * self.size + col + 1
                btn = self.buttons[row][col]
                if point_num in self.pattern:
                    idx = self.pattern.index(point_num) + 1
                    btn.config(bg="skyblue", text=str(idx))
                else:
                    btn.config(bg="lightgray", text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenLock9x9(root)
    root.mainloop()
