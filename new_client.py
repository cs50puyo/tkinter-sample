import tkinter as tk

def create_new_client():
    pass


def add_new_client():
    new_client = tk.Toplevel()
    new_client.title('New Client')

    name_label = tk.Label(new_client, text='Name')
    name_label.grid(row=0, column=0)
    name_var = tk.StringVar()
    name_entry = tk.Entry(new_client, textvariable=name_var)
    name_entry.grid(row=0, column=1)

    last_name_label = tk.Label(new_client, text='Last Name')
    last_name_label.grid(row=1, column=0)
    last_name_var = tk.StringVar()
    last_name_entry = tk.Entry(new_client, textvariable=last_name_var)
    last_name_entry.grid(row=1, column=1)

    id_label = tk.Label(new_client, text='Id')
    id_label.grid(row=2, column=0)
    id_var = tk.StringVar()
    id_entry = tk.Entry(new_client, textvariable=id_var)
    id_entry.grid(row=2, column=1)

    class_label = tk.Label(new_client, text='Class')
    class_label.grid(row=3, column=0)

    CLASSROOMS = ('1A', '1B', '1C', '1D',
               '2A', '2B', '2C', '2D', '1IB',
               '3A', '3B', '3C', '2IB')
    classroom_var = tk.StringVar()
    classroom_var.set(CLASSROOMS[0])
    class_option_menu = tk.OptionMenu(new_client, classroom_var, *CLASSROOMS)
    class_option_menu.grid(row=3, column=1)

    new_client_button = tk.Button(new_client,
        text='Create New Client',
                                  command=create_new_client)
    new_client_button.grid(row=4, column=1)
