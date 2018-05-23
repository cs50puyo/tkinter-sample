import tkinter as tk

from new_client import add_new_client


def show_clients():
    clients = tk.Toplevel()
    clients.title('Clients')

    label_clients = tk.Label(clients, text='Clients')
    label_clients.pack(fill=tk.X)

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
