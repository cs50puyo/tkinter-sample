import tkinter as tk

def add_new_record():
    new_record = tk.Toplevel()
    new_record.title('New Client')

    name_label = tk.Label(new_record, text='Name')
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(new_record)
    name_entry.grid(row=0, column=1)

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
