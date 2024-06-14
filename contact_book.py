import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create Add Contact button
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)

        # Create View Contacts button
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=10)

        # Create Delete Contact button
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        if not phone:
            messagebox.showerror("Error", "Phone number cannot be empty!")
            return

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
        else:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
            return

        contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        messagebox.showinfo("Contacts", contact_list)

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
