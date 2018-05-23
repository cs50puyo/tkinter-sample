import tkinter as tk

def add_new_client():
    new_client = tk.Toplevel()
    new_client.title('New Client')

    name_label = tk.Label(new_client, text='Name')
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(new_client)
    name_entry.grid(row=0, column=1)

    last_name_label = tk.Label(new_client, text='Last Name')
    last_name_label.grid(row=1, column=0)
    last_name_entry = tk.Entry(new_client)
    last_name_entry.grid(row=1, column=1)

    id_label = tk.Label(new_client, text='Name')
    id_label.grid(row=2, column=0)
    id_entry = tk.Entry(new_client)
    id_entry.grid(row=2, column=1)

    class_label = tk.Label(new_client, text='Class')
    class_label.grid(row=3, column=0)

    CLASSES = ('1A', '1B', '1C', '1D',
               '2A', '2B', '2C', '2D', '1IB',
               '3A', '3B', '3C', '2IB')
    selected_class = tk.StringVar()
    selected_class.set(CLASSES[0])
    class_option_menu = tk.OptionMenu(new_client, selected_class, *CLASSES)
    class_option_menu.grid(row=3, column=1)

    new_client_button = tk.Button(new_client, text='Create New Record')
    new_client_button.grid(row=4, column=1)


def show_clients():
    pass


def main():
    root = tk.Tk()
    root.title('Bar register')

    frame = tk.Frame(root)
    frame.pack(padx=100, pady=100)
    new_client_button = tk.Button(frame,
                                  text='Add New Client',
                                  command=add_new_client)
    new_client_button.pack()
    show_clients_button = tk.Button(frame, text='Show Clients')
    show_clients_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
