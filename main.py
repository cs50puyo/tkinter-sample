import tkinter as tk

def main():
    root = tk.Tk()

    new_record_button = tk.Button(root, text='New Record')
    new_record_button.pack()
    show_clients_button = tk.Button(root, text='Show Clients')
    show_clients_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
