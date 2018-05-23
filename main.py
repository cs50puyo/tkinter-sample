import tkinter as tk

from os import listdir
from os.path import isfile, join


from new_client import add_new_client


def show_clients():
    clients = tk.Toplevel()
    clients.title('Clients')

    label_clients = tk.Label(clients, text='Clients')
    label_clients.pack(fill=tk.X)

    records_path = 'clients/'
    records = [f for f in listdir(records_path) if isfile(join(records_path, f))]

    for record in records:
        with open(join(records_path, record)) as file:
            name = file.readline().strip()[6:]
            last_name = file.readline().strip()[11:]
            client_id = file.readline().strip()[4:]
            client_class = file.readline().strip()[11:]

        client_label = tk.Label(
            clients,
            text=f'{client_id} - {name} - {last_name} - {client_class}')
        client_label.pack(fill=tk.X)


def main():
    root = tk.Tk()
    root.title('Bar register')

    frame = tk.Frame(root)
    frame.pack(padx=100, pady=100)
    new_client_button = tk.Button(frame,
                                  text='Add New Client',
                                  command=add_new_client)
    new_client_button.pack()
    show_clients_button = tk.Button(frame,
                                    text='Show Clients',
                                    command=show_clients)
    show_clients_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
