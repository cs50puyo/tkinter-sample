import tkinter as tk

def add_new_record():
    pass


def show_clients():
    pass


def main():
    root = tk.Tk()
    root.title('Bar register')

    frame = tk.Frame(root)
    frame.pack(padx=100, pady=100)
    new_record_button = tk.Button(frame,
                                  text='Add New Client',
                                  command=add_new_record)
    new_record_button.pack()
    show_clients_button = tk.Button(frame, text='Show Clients')
    show_clients_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
