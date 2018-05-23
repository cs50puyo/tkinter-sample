import tkinter as tk

def main():
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack(padx=100, pady=100)
    new_record_button = tk.Button(frame, text='New Record')
    new_record_button.pack()
    show_clients_button = tk.Button(frame, text='Show Clients')
    show_clients_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
