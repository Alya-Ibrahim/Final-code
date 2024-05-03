#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing necessary files
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

class EventManagementSystemGUI:
    """ A GUI application for managing an event planning system using Tkinter. """
    def __init__(self, root):
        """Initialize the main application GUI and load data from files."""
        self.root = root
        self.root.title("Event Management System")

        #Loading data from binary files
        self.load_data()

        # Initializing data structures to store employees, events, clients, guests, suppliers and venues
        if not hasattr(self, 'employees'):
            self.employees = []
        if not hasattr(self, 'events'):
            self.events = []
        if not hasattr(self, 'clients'):
            self.clients = []
        if not hasattr(self, 'guests'):
            self.guests = []
        if not hasattr(self, 'suppliers'):
            self.suppliers = []
        if not hasattr(self, 'venues'):
            self.venues = []

        # Employee Details Frame
        self.employee_frame = ttk.LabelFrame(self.root, text="Employee Details")
        self.employee_frame.grid(row=0, column=0, padx=10, pady=5)

        self.employee_id_label = ttk.Label(self.employee_frame, text="Employee ID:")
        self.employee_id_label.grid(row=0, column=0, sticky="e")
        self.employee_id_entry = ttk.Entry(self.employee_frame)
        self.employee_id_entry.grid(row=0, column=1)

        self.display_employee_button = ttk.Button(self.employee_frame, text="Display Employee", command=self.display_employee)
        self.display_employee_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Add/Delete/Modify/Display buttons for employees
        self.add_employee_button = ttk.Button(self.employee_frame, text="Add Employee", command=self.add_employee_window)
        self.add_employee_button.grid(row=2, column=0, pady=5)

        self.delete_employee_button = ttk.Button(self.employee_frame, text="Delete Employee", command=self.delete_employee_window)
        self.delete_employee_button.grid(row=2, column=1, pady=5)

        self.modify_employee_button = ttk.Button(self.employee_frame, text="Modify Employee", command=self.modify_employee_window)
        self.modify_employee_button.grid(row=2, column=2, pady=5)

        # Event Details Frame
        self.event_frame = ttk.LabelFrame(self.root, text="Event Details")
        self.event_frame.grid(row=1, column=0, padx=10, pady=5)

        self.event_id_label = ttk.Label(self.event_frame, text="Event ID:")
        self.event_id_label.grid(row=0, column=0, sticky="e")
        self.event_id_entry = ttk.Entry(self.event_frame)
        self.event_id_entry.grid(row=0, column=1)

        self.display_event_button = ttk.Button(self.event_frame, text="Display Event", command=self.display_event)
        self.display_event_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Add/Delete/Modify/Display buttons for events
        self.add_event_button = ttk.Button(self.event_frame, text="Add Event", command=self.add_event_window)
        self.add_event_button.grid(row=2, column=0, pady=5)

        self.delete_event_button = ttk.Button(self.event_frame, text="Delete Event", command=self.delete_event_window)
        self.delete_event_button.grid(row=2, column=1, pady=5)

        self.modify_event_button = ttk.Button(self.event_frame, text="Modify Event", command=self.modify_event_window)
        self.modify_event_button.grid(row=2, column=2, pady=5)
        
        # Client Details Frame
        self.client_frame = ttk.LabelFrame(self.root, text="Client Details")
        self.client_frame.grid(row=2, column=0, padx=10, pady=5)

        self.client_id_label = ttk.Label(self.client_frame, text="Client ID:")
        self.client_id_label.grid(row=0, column=0, sticky="e")
        self.client_id_entry = ttk.Entry(self.client_frame)
        self.client_id_entry.grid(row=0, column=1)

        self.display_client_button = ttk.Button(self.client_frame, text="Display Client", command=self.display_client)
        self.display_client_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Add/Delete/Modify/Display buttons for clients
        self.add_client_button = ttk.Button(self.client_frame, text="Add Client", command=self.add_client_window)
        self.add_client_button.grid(row=2, column=0, pady=5)

        self.delete_client_button = ttk.Button(self.client_frame, text="Delete Client", command=self.delete_client_window)
        self.delete_client_button.grid(row=2, column=1, pady=5)

        self.modify_client_button = ttk.Button(self.client_frame, text="Modify Client", command=self.modify_client_window)
        self.modify_client_button.grid(row=2, column=2, pady=5)
        
        # Supplier Details Frame
        self.supplier_frame = ttk.LabelFrame(self.root, text="Supplier Details")
        self.supplier_frame.grid(row=3, column=0, padx=10, pady=5)

        self.supplier_id_label = ttk.Label(self.supplier_frame, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, sticky="e")
        self.supplier_id_entry = ttk.Entry(self.supplier_frame)
        self.supplier_id_entry.grid(row=0, column=1)

        self.display_supplier_button = ttk.Button(self.supplier_frame, text="Display Supplier", command=self.display_supplier)
        self.display_supplier_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Add/Delete/Modify/Display buttons for Suppliers
        self.add_supplier_button = ttk.Button(self.supplier_frame, text="Add Supplier", command=self.add_supplier_window)
        self.add_supplier_button.grid(row=2, column=0, pady=5)

        self.delete_supplier_button = ttk.Button(self.supplier_frame, text="Delete Supplier", command=self.delete_supplier_window)
        self.delete_supplier_button.grid(row=2, column=1, pady=5)

        self.modify_supplier_button = ttk.Button(self.supplier_frame, text="Modify Supplier", command=self.modify_supplier_window)
        self.modify_supplier_button.grid(row=2, column=2, pady=5)
       
        # Guest Details Frame
        self.guest_frame = ttk.LabelFrame(self.root, text="Guest Details")
        self.guest_frame.grid(row=4, column=0, padx=10, pady=5)

        self.guest_id_label = ttk.Label(self.guest_frame, text="Guest ID:")
        self.guest_id_label.grid(row=0, column=0, sticky="e")
        self.guest_id_entry = ttk.Entry(self.guest_frame)
        self.guest_id_entry.grid(row=0, column=1)

        self.display_guest_button = ttk.Button(self.guest_frame, text="Display Guest", command=self.display_guest)
        self.display_guest_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Add/Delete/Modify/Display buttons for Guests
        self.add_guest_button = ttk.Button(self.guest_frame, text="Add Guest", command=self.add_guest_window)
        self.add_guest_button.grid(row=2, column=0, pady=5)

        self.delete_guest_button = ttk.Button(self.guest_frame, text="Delete Guest", command=self.delete_guest_window)
        self.delete_guest_button.grid(row=2, column=1, pady=5)

        self.modify_guest_button = ttk.Button(self.guest_frame, text="Modify Guest", command=self.modify_guest_window)
        self.modify_guest_button.grid(row=2, column=2, pady=5)
        
        # Venue Details Frame
        self.venue_frame = ttk.LabelFrame(self.root, text="Venue Details")
        self.venue_frame.grid(row=5, column=0, padx=10, pady=5)
        
        self.venue_id_label = ttk.Label(self.venue_frame, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, sticky="e")
        self.venue_id_entry = ttk.Entry(self.venue_frame)
        self.venue_id_entry.grid(row=0, column=1)
        
        self.display_venue_button = ttk.Button(self.venue_frame, text="Display Venue", command=self.display_venue)
        self.display_venue_button.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Add/Delete/Modify/Display buttons for Venues
        self.add_venue_button = ttk.Button(self.venue_frame, text="Add Venue", command=self.add_venue_window)
        self.add_venue_button.grid(row=2, column=0, pady=5)
        
        self.delete_venue_button = ttk.Button(self.venue_frame, text="Delete Venue", command=self.delete_venue_window)
        self.delete_venue_button.grid(row=2, column=1, pady=5)
        
        self.modify_venue_button = ttk.Button(self.venue_frame, text="Modify Venue", command=self.modify_venue_window)
        self.modify_venue_button.grid(row=2, column=2, pady=5)


#Section display employee Information
    def display_employee(self):
        employee_id = int(self.employee_id_entry.get())
        employee = None
        for emp in self.employees:
            if emp["employee_id"] == employee_id:
                employee = emp
                break
        if employee:
            self.display_details("Employee Details", [[
                "Employee ID", employee["employee_id"]],
                ["Name", employee["name"]],
                ["Department", employee["department"]],
                ["Job Title", employee["job_title"]],
                ["Basic Salary", employee["basic_salary"]],
                ["Age", employee["age"]],
                ["Date of Birth", employee["date_of_birth"]],
                ["Passport Details", employee["passport_details"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Employee not found.")

#Section display event Information
    def display_event(self):
        event_id = int(self.event_id_entry.get())
        event = None
        for ev in self.events:
            if ev["event_id"] == event_id:
                event = ev
                break
        if event:
            self.display_details("Event Details", [[
                "Event ID", event["event_id"]],
                ["Type", event["type"]],
                ["Theme", event["theme"]],
                ["Date", event["date"]],
                ["Time", event["time"]],
                ["Duration", event["duration"]],
                ["Venue", event["venue"]],
                ["Client", event["client"]],
                ["Guest List", event["guests"]],
                ["Suppliers", event["suppliers"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Event not found.")

#Section display client Information
    def display_client(self):
        client_id = int(self.client_id_entry.get())
        client = None
        for cl in self.clients:
            if "client_id" in cl and cl["client_id"] == client_id:
                client = cl
                break
        if client:
            self.display_details("Client Details", [[
                "Client ID", client["client_id"]],
                ["Name", client["name"]],
                ["Address", client["address"]],
                ["Contact Details", client["contact_details"]],
                ["Budget", client["budget"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Client not found or missing client ID.")

#Section display Supplier Information
    def display_supplier(self):
        supplier_id = int(self.supplier_id_entry.get())
        supplier = None
        for sp in self.suppliers:
            if "supplier_id" in sp and sp["supplier_id"] == supplier_id:
                supplier = sp
                break
        if supplier:
            self.display_details("Supplier Details", [[
                "Supplier ID", supplier["supplier_id"]],
                ["Name", supplier["name"]],
                ["Address", supplier["address"]],
                ["Contact Details", supplier["contact_details"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Supplier not found.")

#Section display guests Information
    def display_guest(self):
        guest_id = int(self.guest_id_entry.get())
        guest = None
        for gst in self.guests:
            if "guest_id" in gst and gst["guest_id"] == guest_id:
                guest = gst
                break
        if guest:
            self.display_details("Guest Details", [[
                "Guest ID", guest["guest_id"]],
                ["Name", guest["name"]],
                ["Address", guest["address"]],
                ["Contact Details", guest["contact_details"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Guest not found.")

#Section display venues Information
    def display_venue(self):
        venue_id = int(self.venue_id_entry.get())
        venue = None
        for vn in self.venues:
            if vn["venue_id"] == venue_id:
                venue = vn
                break
        if venue:
            self.display_details("Venue Details", [[
                "Venue ID", venue["venue_id"]],
                ["Name", venue["name"]],
                ["Address", venue["address"]],
                ["Contact Details", venue["contact_details"]],
                ["Minimum Guests", venue["min_guests"]],
                ["Maximum Guests", venue["max_guests"]]
            ])
        else:
            tk.messagebox.showinfo("Error", "Venue not found.")

#function to display details
    def display_details(self, title, data):
        window = tk.Toplevel(self.root)
        window.title(title)
        table = ttk.Treeview(window)
        table["columns"] = ("#1", "#2")
        table.heading("#0", text="Attribute")
        table.heading("#1", text="Value")

        for i, row in enumerate(data):
            table.insert("", tk.END, text=row[0], values=(row[1]))

        table.pack(expand=True, fill=tk.BOTH)
        
#Section to load data from pickle library
    def load_data(self):
        try:
            with open("employees.pkl", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

        try:
            with open("events.pkl", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []
        
        try:
            with open("clients.pkl", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []
        try:
            with open("suppliers.pkl", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []
        try:
            with open("guests.pkl", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []
        try:
            with open("venues.pkl", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = []

#Section to add, delete, modify employees
    def add_employee_window(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Add Employee")

        ttk.Label(employee_window, text="Employee ID:").grid(row=0, column=0, sticky="e")
        employee_id_entry = ttk.Entry(employee_window)
        employee_id_entry.grid(row=0, column=1)

        ttk.Label(employee_window, text="Name:").grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(employee_window)
        name_entry.grid(row=1, column=1)

        ttk.Label(employee_window, text="Department:").grid(row=2, column=0, sticky="e")
        department_entry = ttk.Entry(employee_window)
        department_entry.grid(row=2, column=1)

        ttk.Label(employee_window, text="Job Title:").grid(row=3, column=0, sticky="e")
        job_title_entry = ttk.Entry(employee_window)
        job_title_entry.grid(row=3, column=1)

        ttk.Label(employee_window, text="Basic Salary:").grid(row=4, column=0, sticky="e")
        basic_salary_entry = ttk.Entry(employee_window)
        basic_salary_entry.grid(row=4, column=1)

        ttk.Label(employee_window, text="Age:").grid(row=5, column=0, sticky="e")
        age_entry = ttk.Entry(employee_window)
        age_entry.grid(row=5, column=1)

        ttk.Label(employee_window, text="Date of Birth:").grid(row=6, column=0, sticky="e")
        dob_entry = ttk.Entry(employee_window)
        dob_entry.grid(row=6, column=1)

        ttk.Label(employee_window, text="Passport Details:").grid(row=7, column=0, sticky="e")
        passport_entry = ttk.Entry(employee_window)
        passport_entry.grid(row=7, column=1)

        add_button = ttk.Button(employee_window, text="Add Employee", command=lambda: self.add_employee(employee_id_entry.get(), name_entry.get(), department_entry.get(), job_title_entry.get(), basic_salary_entry.get(), age_entry.get(), dob_entry.get(), passport_entry.get(), employee_window))
        add_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_employee(self, emp_id, name, department, job_title, basic_salary, age, dob, passport, window):
        #adding employee details
        employee = {
            "employee_id": int(emp_id),
            "name": name,
            "department": department,
            "job_title": job_title,
            "basic_salary": float(basic_salary),
            "age": int(age),
            "date_of_birth": dob,
            "passport_details": passport
        }
        self.employees.append(employee)
        with open("employees.pkl", "wb") as file:
            pickle.dump(self.employees, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Employee added successfully.")

    def delete_employee_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Employee")

        ttk.Label(delete_window, text="Employee ID:").grid(row=0, column=0, sticky="e")
        employee_id_entry = ttk.Entry(delete_window)
        employee_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(delete_window, text="Delete Employee", command=lambda: self.delete_employee(employee_id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_employee(self, emp_id, window):
        emp_id = int(emp_id)
        for idx, emp in enumerate(self.employees):
            if emp["employee_id"] == emp_id:
                del self.employees[idx]
                with open("employees.pkl", "wb") as file:
                    pickle.dump(self.employees, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Employee deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Employee not found.")

    def modify_employee_window(self):
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Employee")

        ttk.Label(modify_window, text="Employee ID:").grid(row=0, column=0, sticky="e")
        employee_id_entry = ttk.Entry(modify_window)
        employee_id_entry.grid(row=0, column=1)

        ttk.Label(modify_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        attribute_combobox = ttk.Combobox(modify_window, values=["Name", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(modify_window, text="New Value:").grid(row=2, column=0, sticky="e")
        new_value_entry = ttk.Entry(modify_window)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(modify_window, text="Modify Employee", command=lambda: self.modify_employee(employee_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), modify_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_employee(self, emp_id, attribute, new_value, window):
        emp_id = int(emp_id)
        for emp in self.employees:
            if emp["employee_id"] == emp_id:
                emp[attribute.lower().replace(" ", "_")] = new_value
                with open("employees.pkl", "wb") as file:
                    pickle.dump(self.employees, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Employee modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Employee not found.")

#Section to add, delete, modify events
    def add_event_window(self):
        event_window = tk.Toplevel(self.root)
        event_window.title("Add Event")

        ttk.Label(event_window, text="Event ID:").grid(row=0, column=0, sticky="e")
        event_id_entry = ttk.Entry(event_window)
        event_id_entry.grid(row=0, column=1)

        ttk.Label(event_window, text="Type:").grid(row=1, column=0, sticky="e")
        type_entry = ttk.Entry(event_window)
        type_entry.grid(row=1, column=1)

        ttk.Label(event_window, text="Theme:").grid(row=2, column=0, sticky="e")
        theme_entry = ttk.Entry(event_window)
        theme_entry.grid(row=2, column=1)

        ttk.Label(event_window, text="Date:").grid(row=3, column=0, sticky="e")
        date_entry = ttk.Entry(event_window)
        date_entry.grid(row=3, column=1)

        ttk.Label(event_window, text="Time:").grid(row=4, column=0, sticky="e")
        time_entry = ttk.Entry(event_window)
        time_entry.grid(row=4, column=1)

        ttk.Label(event_window, text="Duration:").grid(row=5, column=0, sticky="e")
        duration_entry = ttk.Entry(event_window)
        duration_entry.grid(row=5, column=1)

        ttk.Label(event_window, text="Venue:").grid(row=6, column=0, sticky="e")
        venue_entry = ttk.Entry(event_window)
        venue_entry.grid(row=6, column=1)

        ttk.Label(event_window, text="Client:").grid(row=7, column=0, sticky="e")
        client_entry = ttk.Entry(event_window)
        client_entry.grid(row=7, column=1)

        ttk.Label(event_window, text="Guest List:").grid(row=8, column=0, sticky="e")
        guests_entry = ttk.Entry(event_window)
        guests_entry.grid(row=8, column=1)

        ttk.Label(event_window, text="Suppliers:").grid(row=9, column=0, sticky="e")
        suppliers_entry = ttk.Entry(event_window)
        suppliers_entry.grid(row=9, column=1)

        add_button = ttk.Button(event_window, text="Add Event", command=lambda: self.add_event(event_id_entry.get(), type_entry.get(), theme_entry.get(), date_entry.get(), time_entry.get(), duration_entry.get(), venue_entry.get(), client_entry.get(), guests_entry.get(), suppliers_entry.get(), event_window))
        add_button.grid(row=10, column=0, columnspan=2, pady=5)

    def add_event(self, event_id, type, theme, date, time, duration, venue, client, guests, suppliers, window):
        # Adding event details
        event = {
            "event_id": int(event_id),
            "type": type,
            "theme": theme,
            "date": date,
            "time": time,
            "duration": duration,
            "venue": venue,
            "client": client,
            "guests": guests,
            "suppliers": suppliers
        }
        self.events.append(event)
        with open("events.pkl", "wb") as file:
            pickle.dump(self.events, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Event added successfully.")

    def delete_event_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Event")

        ttk.Label(delete_window, text="Event ID:").grid(row=0, column=0, sticky="e")
        event_id_entry = ttk.Entry(delete_window)
        event_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(delete_window, text="Delete Event", command=lambda: self.delete_event(event_id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_event(self, event_id, window):
        event_id = int(event_id)
        for idx, event in enumerate(self.events):
            if event["event_id"] == event_id:
                del self.events[idx]
                with open("events.pkl", "wb") as file:
                    pickle.dump(self.events, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Event deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Event not found.")

    def modify_event_window(self):
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Event")

        ttk.Label(modify_window, text="Event ID:").grid(row=0, column=0, sticky="e")
        event_id_entry = ttk.Entry(modify_window)
        event_id_entry.grid(row=0, column=1)

        ttk.Label(modify_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        attribute_combobox = ttk.Combobox(modify_window, values=["Type", "Theme", "Date", "Time", "Duration", "Venue", "Client", "Guest List", "Suppliers"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(modify_window, text="New Value:").grid(row=2, column=0, sticky="e")
        new_value_entry = ttk.Entry(modify_window)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(modify_window, text="Modify Event", command=lambda: self.modify_event(event_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), modify_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_event(self, event_id, attribute, new_value, window):
        event_id = int(event_id)
        for event in self.events:
            if event["event_id"] == event_id:
                event[attribute.lower().replace(" ", "_")] = new_value
                with open("events.pkl", "wb") as file:
                    pickle.dump(self.events, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Event modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Event not found.")
        
#Section to add, delete, modify clients        
    def add_client_window(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Add Client")

        ttk.Label(client_window, text="Client ID:").grid(row=0, column=0, sticky="e")
        client_id_entry = ttk.Entry(client_window)
        client_id_entry.grid(row=0, column=1)

        ttk.Label(client_window, text="Name:").grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(client_window)
        name_entry.grid(row=1, column=1)

        ttk.Label(client_window, text="Address:").grid(row=2, column=0, sticky="e")
        address_entry = ttk.Entry(client_window)
        address_entry.grid(row=2, column=1)

        ttk.Label(client_window, text="Contact Details:").grid(row=3, column=0, sticky="e")
        contact_entry = ttk.Entry(client_window)
        contact_entry.grid(row=3, column=1)

        ttk.Label(client_window, text="Budget:").grid(row=4, column=0, sticky="e")
        budget_entry = ttk.Entry(client_window)
        budget_entry.grid(row=4, column=1)

        add_button = ttk.Button(client_window, text="Add Client", command=lambda: self.add_client(client_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), budget_entry.get(), client_window))
        add_button.grid(row=5, column=0, columnspan=2, pady=5)

    def add_client(self, client_id, name, address, contact, budget, window):
        # Adding clients
        client = {
            "client_id": int(client_id),
            "name": name,
            "address": address,
            "contact_details": contact,
            "budget": float(budget)
        }
        self.clients.append(client)
        with open("clients.pkl", "wb") as file:
            pickle.dump(self.clients, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Client added successfully.")
    def delete_client_window(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Delete Client")

        ttk.Label(client_window, text="Client ID:").grid(row=0, column=0, sticky="e")
        client_id_entry = ttk.Entry(client_window)
        client_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(client_window, text="Delete Client", command=lambda: self.delete_client(client_id_entry.get(), client_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_client(self, client_id, window):
        client_id = int(client_id)
        for i, client in enumerate(self.clients):
            if client.get("client_id") == client_id:
                del self.clients[i]
                with open("clients.pkl", "wb") as file:
                    pickle.dump(self.clients, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Client deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Client not found.")

    def modify_client_window(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Modify Client")

        ttk.Label(client_window, text="Client ID:").grid(row=0, column=0, sticky="e")
        self.client_id_var = tk.StringVar()
        client_id_entry = ttk.Entry(client_window, textvariable=self.client_id_var)
        client_id_entry.grid(row=0, column=1)

        ttk.Label(client_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        self.attribute_var = tk.StringVar()
        attribute_combobox = ttk.Combobox(client_window, textvariable=self.attribute_var, values=["Name", "Address", "Contact Details", "Budget"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(client_window, text="New Value:").grid(row=2, column=0, sticky="e")
        self.new_value_var = tk.StringVar()
        new_value_entry = ttk.Entry(client_window, textvariable=self.new_value_var)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(client_window, text="Modify Client", command=lambda: self.modify_client(client_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), client_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_client(self, client_id, attribute, new_value, window):
        client_id = int(client_id)
        for client in self.clients:
            if client.get("client_id") == client_id:
                if attribute == "Budget":
                    client[attribute.lower()] = float(new_value)
                else:
                    client[attribute.lower()] = new_value
                with open("clients.pkl", "wb") as file:
                    pickle.dump(self.clients, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Client modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Client not found.")

#Section to add, delete, modify suppliers        
    def add_supplier_window(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Add Supplier")

        ttk.Label(supplier_window, text="Supplier ID:").grid(row=0, column=0, sticky="e")
        supplier_id_entry = ttk.Entry(supplier_window)
        supplier_id_entry.grid(row=0, column=1)

        ttk.Label(supplier_window, text="Name:").grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(supplier_window)
        name_entry.grid(row=1, column=1)

        ttk.Label(supplier_window, text="Address:").grid(row=2, column=0, sticky="e")
        address_entry = ttk.Entry(supplier_window)
        address_entry.grid(row=2, column=1)

        ttk.Label(supplier_window, text="Contact Details:").grid(row=3, column=0, sticky="e")
        contact_entry = ttk.Entry(supplier_window)
        contact_entry.grid(row=3, column=1)

        add_button = ttk.Button(supplier_window, text="Add Supplier", command=lambda: self.add_supplier(supplier_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), supplier_window))
        add_button.grid(row=5, column=0, columnspan=2, pady=5)

    def add_supplier(self, supplier_id, name, address, contact, window):
        # Adding suppliers
        supplier = {
            "supplier_id": int(supplier_id),
            "name": name,
            "address": address,
            "contact_details": contact
        }
        self.suppliers.append(supplier)
        with open("suppliers.pkl", "wb") as file:
            pickle.dump(self.suppliers, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Supplier added successfully.")
    def delete_supplier_window(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Delete Supplier")

        ttk.Label(supplier_window, text="Supplier ID:").grid(row=0, column=0, sticky="e")
        supplier_id_entry = ttk.Entry(supplier_window)
        supplier_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(supplier_window, text="Delete Supplier", command=lambda: self.delete_supplier(supplier_id_entry.get(), supplier_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_supplier(self, supplier_id, window):
        supplier_id = int(supplier_id)
        for i, supplier in enumerate(self.suppliers):
            if supplier.get("supplier_id") == supplier_id:
                del self.suppliers[i]
                with open("suppliers.pkl", "wb") as file:
                    pickle.dump(self.suppliers, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Supplier deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Supplier not found.")

    def modify_supplier_window(self):
        supplier_window = tk.Toplevel(self.root)
        supplier_window.title("Modify Supplier")

        ttk.Label(supplier_window, text="Supplier ID:").grid(row=0, column=0, sticky="e")
        self.supplier_id_var = tk.StringVar()
        supplier_id_entry = ttk.Entry(supplier_window, textvariable=self.supplier_id_var)
        supplier_id_entry.grid(row=0, column=1)

        ttk.Label(supplier_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        self.attribute_var = tk.StringVar()
        attribute_combobox = ttk.Combobox(supplier_window, textvariable=self.attribute_var, values=["Name", "Address", "Contact Details"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(supplier_window, text="New Value:").grid(row=2, column=0, sticky="e")
        self.new_value_var = tk.StringVar()
        new_value_entry = ttk.Entry(supplier_window, textvariable=self.new_value_var)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(supplier_window, text="Modify Supplier", command=lambda: self.modify_supplier(supplier_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), supplier_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_supplier(self, supplier_id, attribute, new_value, window):
        supplier_id = int(supplier_id)
        for supplier in self.suppliers:
            if supplier.get("supplier_id") == supplier_id:
                supplier[attribute.lower()] = new_value
                with open("suppliers.pkl", "wb") as file:
                    pickle.dump(self.suppliers, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Supplier info modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Supplier not found.")

#Section to add, delete, modify guests        
    def add_guest_window(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Add Guest")

        ttk.Label(guest_window, text="Guest ID:").grid(row=0, column=0, sticky="e")
        guest_id_entry = ttk.Entry(guest_window)
        guest_id_entry.grid(row=0, column=1)

        ttk.Label(guest_window, text="Name:").grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(guest_window)
        name_entry.grid(row=1, column=1)

        ttk.Label(guest_window, text="Address:").grid(row=2, column=0, sticky="e")
        address_entry = ttk.Entry(guest_window)
        address_entry.grid(row=2, column=1)

        ttk.Label(guest_window, text="Contact Details:").grid(row=3, column=0, sticky="e")
        contact_entry = ttk.Entry(guest_window)
        contact_entry.grid(row=3, column=1)

        add_button = ttk.Button(guest_window, text="Add Guest", command=lambda: self.add_guest(guest_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), guest_window))
        add_button.grid(row=5, column=0, columnspan=2, pady=5)

    def add_guest(self, guest_id, name, address, contact, window):
        # adding guests
        guest = {
            "guest_id": int(guest_id),
            "name": name,
            "address": address,
            "contact_details": contact
        }
        self.guests.append(guest)
        with open("guests.pkl", "wb") as file:
            pickle.dump(self.guests, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Guest added successfully.")
    def delete_guest_window(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Delete Guest")

        ttk.Label(guest_window, text="Guest ID:").grid(row=0, column=0, sticky="e")
        guest_id_entry = ttk.Entry(guest_window)
        guest_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(guest_window, text="Delete Guest", command=lambda: self.delete_guest(guest_id_entry.get(), guest_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_guest(self, guest_id, window):
        guest_id = int(guest_id)
        for i, guest in enumerate(self.guests):
            if guest.get("guest_id") == guest_id:
                del self.guests[i]
                with open("guests.pkl", "wb") as file:
                    pickle.dump(self.guests, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Guest deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Guest not found.")

    def modify_guest_window(self):
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Guest")

        ttk.Label(modify_window, text="Guest ID:").grid(row=0, column=0, sticky="e")
        guest_id_entry = ttk.Entry(modify_window)
        guest_id_entry.grid(row=0, column=1)

        ttk.Label(modify_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        attribute_combobox = ttk.Combobox(modify_window, values=["Name", "Address", "Contact Details"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(modify_window, text="New Value:").grid(row=2, column=0, sticky="e")
        new_value_entry = ttk.Entry(modify_window)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(modify_window, text="Modify Guest", command=lambda: self.modify_guest(guest_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), modify_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_guest(self, gst_id, attribute, new_value, window):
        gst_id = int(gst_id)
        for gst in self.guests:
            if gst["guest_id"] == gst_id:
                gst[attribute.lower().replace(" ", "_")] = new_value
                with open("guests.pkl", "wb") as file:
                    pickle.dump(self.guests, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Guest modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Guest not found.")


#Section to add, delete, modify venues        
    def add_venue_window(self):
        venue_window = tk.Toplevel(self.root)
        venue_window.title("Add Venue")

        ttk.Label(venue_window, text="Venue ID:").grid(row=0, column=0, sticky="e")
        venue_id_entry = ttk.Entry(venue_window)
        venue_id_entry.grid(row=0, column=1)

        ttk.Label(venue_window, text="Name:").grid(row=1, column=0, sticky="e")
        name_entry = ttk.Entry(venue_window)
        name_entry.grid(row=1, column=1)

        ttk.Label(venue_window, text="Address:").grid(row=2, column=0, sticky="e")
        address_entry = ttk.Entry(venue_window)
        address_entry.grid(row=2, column=1)

        ttk.Label(venue_window, text="Contact Details:").grid(row=3, column=0, sticky="e")
        contact_entry = ttk.Entry(venue_window)
        contact_entry.grid(row=3, column=1)
        
        ttk.Label(venue_window, text="Minimum Guests:").grid(row=4, column=0, sticky="e")
        min_guests_entry = ttk.Entry(venue_window)
        min_guests_entry.grid(row=4, column=1)

        ttk.Label(venue_window, text="Maximum Guests:").grid(row=5, column=0, sticky="e")
        max_guests_entry = ttk.Entry(venue_window)
        max_guests_entry.grid(row=5, column=1)
        
        add_button = ttk.Button(venue_window, text="Add Venue", command=lambda: self.add_venue(venue_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), min_guests_entry.get(),max_guests_entry.get(),venue_window))
        add_button.grid(row=6, column=0, columnspan=2, pady=5)

    def add_venue(self, venue_id, name, address, contact, min_guests, max_guests,window):
        # Adding venues
        venue = {
            "venue_id": int(venue_id),
            "name": name,
            "address": address,
            "contact_details": contact,
            "min_guests": min_guests,
            "max_guests": max_guests
        }
        self.venues.append(venue)
        with open("venues.pkl", "wb") as file:
            pickle.dump(self.venues, file)
        window.destroy()
        tk.messagebox.showinfo("Info", "Venue added successfully.")
    def delete_venue_window(self):
        venue_window = tk.Toplevel(self.root)
        venue_window.title("Delete Venue")

        ttk.Label(venue_window, text="Venue ID:").grid(row=0, column=0, sticky="e")
        venue_id_entry = ttk.Entry(venue_window)
        venue_id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(venue_window, text="Delete Venue", command=lambda: self.delete_venue(venue_id_entry.get(), venue_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=5)

    def delete_venue(self, venue_id, window):
        venue_id = int(venue_id)
        for i, venue in enumerate(self.venues):
            if venue.get("venue_id") == venue_id:
                del self.venues[i]
                with open("venues.pkl", "wb") as file:
                    pickle.dump(self.venues, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Venue deleted successfully.")
                return
        tk.messagebox.showinfo("Error", "Venue not found.")


    def modify_venue_window(self):
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Venue")

        ttk.Label(modify_window, text="Venue ID:").grid(row=0, column=0, sticky="e")
        venue_id_entry = ttk.Entry(modify_window)
        venue_id_entry.grid(row=0, column=1)

        ttk.Label(modify_window, text="Attribute to Modify:").grid(row=1, column=0, sticky="e")
        attribute_combobox = ttk.Combobox(modify_window, values=["Name", "Address", "Contact Details","Minimum Guests","Maximum Guests"])
        attribute_combobox.grid(row=1, column=1)

        ttk.Label(modify_window, text="New Value:").grid(row=2, column=0, sticky="e")
        new_value_entry = ttk.Entry(modify_window)
        new_value_entry.grid(row=2, column=1)

        modify_button = ttk.Button(modify_window, text="Modify Venue", command=lambda: self.modify_venue(venue_id_entry.get(), attribute_combobox.get(), new_value_entry.get(), modify_window))
        modify_button.grid(row=3, column=0, columnspan=2, pady=5)

    def modify_venue(self, venue_id, attribute, new_value, window):
        venue_id = int(venue_id)
        for vn in self.venues:
            if vn["venue_id"] == venue_id:
                vn[attribute.lower().replace(" ", "_")] = new_value
                with open("venues.pkl", "wb") as file:
                    pickle.dump(self.venues, file)
                window.destroy()
                tk.messagebox.showinfo("Info", "Venue modified successfully.")
                return
        tk.messagebox.showinfo("Error", "Venue not found.")

        

def main():
    """Main function to create the root window and start the application."""
    root = tk.Tk()
    app = EventManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

