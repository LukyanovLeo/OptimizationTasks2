import tkinter as tk
from moderator import select_operation
from builder import set_geometry


class Main(tk.Frame):

    task_list = ['Поиск безусловного экстремума',
                 'Наискорейший спуск',
                 'Метод Лагранжа',
                 'Симплекс-метод',
                 'Графический метод',
                 'Игровая задача']

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        label_greetings = tk.Label(self, text='КУРСОВАЯ РАБОТА', font=('Arial', 20), height=3)
        label_greetings.pack(side=tk.TOP)

        label_input = tk.Label(self, pady=10, text='Выберите метод оптимизации:', font=('Arial', 14))
        label_input.pack(side=tk.TOP)

        btn1 = tk.Button(self, text='Нахождение безусловного экстремума', command=self.call_unconditional_extremum)
        btn1.pack(pady=5)

        btn2 = tk.Button(self, text='Метод наискорейшего спуска', command=self.call_steepest_descend)
        btn2.pack(pady=5)

        btn3 = tk.Button(self, text='Метод Лагранжа', command=self.call_lagrange)
        btn3.pack(pady=5)

        btn4 = tk.Button(self, text='Симплекс-метод', command=self.call_simplex_alg)
        btn4.pack(pady=5)

        btn5 = tk.Button(self, text='Графический метод', command=self.call_graphical)
        btn5.pack(pady=5)

        btn6 = tk.Button(self, text='Игровые задачи', command=self.call_game_task)
        btn6.pack(pady=5)

    def call_unconditional_extremum(self):
        Unconditional()

    def call_steepest_descend(self):
        SteepestDescend()

    def call_lagrange(self):
        Lagrange()

    def call_simplex_alg(self):
        SimplexAlg()

    def call_graphical(self):
        Graphical()

    def call_game_task(self):
        GameTask()

# ОКНА ВВОДА
# Нахождение безусловного экстремума
class Unconditional(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_unconditional()

    def init_unconditional(self):
        self.title('Задачи безусловной оптимизации')
        label_input = tk.Label(self, text='ВВЕДИТЕ ДАННЫЕ:', font=('Arial', 12), height=3)
        label_input.pack(side=tk.TOP)

        label_exp = tk.Label(self, text='Выражение: *')
        label_exp.pack(side=tk.LEFT)

        entry_exp = tk.Entry(self, width=40)
        entry_exp.pack(side=tk.RIGHT)

        btn_solve = tk.Button(self, text='Решить')
        btn_solve.bind('<Button-1>', lambda event: select_operation(1))
        btn_solve.pack(side=tk.BOTTOM)

        set_geometry(self, 350, 150)

#
class SteepestDescend(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

    def init_unconditional(self):
        self.title('sasasasas')


#
class Lagrange(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

    def init_unconditional(self):
        self.title('sasasasas')


#
class SimplexAlg(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

    def init_unconditional(self):
        self.title('sasasasas')


#
class Graphical(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

    def init_unconditional(self):
        self.title('sasasasas')


#
class GameTask(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

    def init_unconditional(self):
        self.title('sasasasas')


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()

    set_geometry(widget=root, X=400, Y=400)
    root.title("Методы оптимизации принятия решений")
    root.resizable(False, False)

    root.mainloop()