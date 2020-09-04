from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *
from datetime import date



class Gui:
    def __init__(self):
        self.pat = Patient()
        self.db = Aakash()
        self.update_index = ''

    def login(self):
        try:
            self.wn1 = Tk()
            self.wn1.geometry('400x400')
            self.wn1.title('Hospital management system')
            self.wn1.configure(bg='red')
            self.system_login = Label(self.wn1, text=" Enter the details for system login",
                                      font=('Ariel', 14, 'italic'))
            self.system_login.place(x=50, y=30)
            self.user_name1 = Label(self.wn1, text=" User Name", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.user_name1.place(x=30, y=70)
            self.user_name_ent1 = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.user_name_ent1.place(x=170, y=70)
            self.password1 = Label(self.wn1, text="Password", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.password1.place(x=30, y=100)
            self.password_ent1 = Entry(self.wn1, show='%', font=('Ariel', 14, 'italic'))
            self.password_ent1.place(x=170, y=100)

            self.submit = Button(self.wn1, text='Login', font=('Ariel', 14, 'italic'), bg='green',
                                 command=self.login_user)
            self.submit.place(x=170, y=150)

            self.wn1.mainloop()
        except Exception as e:
            print(e)
    def ap(self):
        try:

            self.wn = Tk()
            self.wn.geometry('400x400')
            self.wn.title('Hospital management system')
            self.wn.configure(bg='red')
            self.Dashboard = Label(self.wn, text="Dashboard", font=('Ariel', 14, 'italic',))
            self.Dashboard.pack(padx=10, pady=30)
            self.register1 = Button(self.wn, text="Register", bg='green', fg='blue', font=('Ariel', 14),
                                   command=self.reg1)

            self.register1.pack(padx=10, pady=10)
            self.login1 = Button(self.wn, text="Login", bg='green', fg='blue', font=('Ariel', 14), command=self.log1)
            self.login1.pack(padx=10, pady=10)
            self.wn.mainloop()
        except Exception as e:
            print(e)



    def register(self):
        try:
            self.wn2 = Tk()
            self.wn2.geometry('400x400')
            self.wn2.title('registration')
            self.wn2.configure(bg='red')
            self.system_login = Label(self.wn2, text="Admin Registration", font=('Ariel', 14, 'italic'))
            self.system_login.place(x=150, y=30)
            self.name = Label(self.wn2, text=" name", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.name.place(x=30, y=70)
            self.name_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.name_ent.place(x=170, y=70)
            self.email = Label(self.wn2, text=" email", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.email.place(x=30, y=100)
            self.email_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.email_ent.place(x=170, y=100)

            self.contact = Label(self.wn2, text=" contact", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.contact.place(x=30, y=130)
            self.contact_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.contact_ent.place(x=170, y=130)

            self.user_name = Label(self.wn2, text="user name", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.user_name.place(x=30, y=160)
            self.user_name_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.user_name_ent.place(x=170, y=160)
            self.password = Label(self.wn2, text="Password", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.password.place(x=30, y=190)
            self.password_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.password_ent.place(x=170, y=190)
            self.submit = Button(self.wn2, text='Save', font=('Ariel', 14, 'italic'), bg='green',
                                 command=self.register_user)
            self.submit.place(x=140, y=240)
            self.submit = Button(self.wn2, text='Login', font=('Ariel', 14, 'italic'), bg='red', command=self.login2)
            self.submit.place(x=220, y=240)

            self.wn2.mainloop()

        except Exception as e:
            print(e)

    def login2(self):
        self.wn2.destroy()
        self.login()


    def register_user(self):
        try:

            self.db = Aakash()
            name = self.name_ent.get()
            email = self.email_ent.get()
            contact = self.contact_ent.get()

            un = self.user_name_ent.get()
            pw = self.password_ent.get()
            if name == '' or email == '' or contact == '' or un == '' or pw == '':
                messagebox.showerror('Error', 'Fill up all entries!')

            else:
                qry = '''select username from admin_reg order by username '''
                list = self.db.get_data(qry)
                ad = self.binary_search_iterative(list, un)
                print(list)
                if ad != -1:
                    messagebox.showerror('Error', 'use another username')
                else:
                    qry = '''insert into admin_reg (name, email, contact, username, password) values(%s,%s,%s,%s,%s)'''
                    vals = (name, email, contact, un, pw)
                    self.db.iud(qry, vals)
                    messagebox.showinfo('Done', 'Register Successful!')
                    self.login2()
        except Exception as e:
            print(e)

    def login_user(self):
        try:
            self.db = Aakash()
            username1 = self.user_name_ent1.get()

            password1 = self.password_ent1.get()
            if username1 == '' or password1 == '':
                messagebox.showerror('Error', 'Enter username or password')
            else:
                qry = '''select * from admin_reg where username=%s and password=%s'''
                vals = (username1, password1)
                data_return = self.db.get_data_p(qry, vals)
                print(len(data_return))
                print(data_return)

                if len(data_return) == 0:
                    messagebox.showerror('Error', 'Wrong username or password')
                else:
                    messagebox.showinfo('Done', 'Login Successful')
                    self.wn1.destroy()
                    self.dashboard()

        except Exception as e:
            print(e)

    def dashboard(self):
        try:
            self.pat = Patient()
            self.doc = Doctor()
            self.app = Appoint()

            self.ns = Tk()
            self.ns.geometry('400x400')
            self.ns.title('Hospital management system')
            self.ns.configure(bg='red')
            self.Dashboard = Label(self.ns, text="Dashboard", font=('Ariel', 14, 'italic'))
            self.Dashboard.pack(padx=10, pady=30)

            self.patient = Button(self.ns, text="Patient", bg='orange', fg='blue', font=('Ariel', 14),
                                  command=self.pat1)
            self.patient.pack(padx=10, pady=10)
            self.doctor = Button(self.ns, text="Doctor", bg='orange', fg='blue', font=('Ariel', 14),
                                 command=self.doc1)
            self.doctor.pack(padx=10, pady=10)
            self.appointment = Button(self.ns, text="Appointment", bg='orange', fg='blue', font=('Ariel', 14),
                                      command=self.app1)
            self.appointment.pack(padx=10, pady=10)

            self.ns.mainloop()
        except Exception as e:
            print(e)

    def pat1(self):
        self.pat=Patient()
        self.ns.destroy()
        self.pat.patient1()

    def doc1(self):
        self.doc=Doctor()
        self.ns.destroy()
        self.doc.doctor1()

    def app1(self):
        self.app=Appoint()
        self.ns.destroy()
        self.app.appoint()


    def binary_search_iterative(self, list, key):
        try:
            start = 0

            end = len(list) - 1
            while start <= end:
                mid = (start + end) // 2
                if list[mid][0] == key:
                    return mid
                elif list[mid][0] > key:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        except Exception as e:
            print(e)

    def reg1(self):
        self.wn.destroy()
        self.register()


    def log1(self):
        self.wn.destroy()
        self.login()



class Patient:
    def __init__(self):
        pass
    def patient1(self):
        try:
            self.ns1 = Tk()
            self.ns1.geometry('1900x600')
            self.ns1.title('Hospital management system')
            self.ns1.configure(bg='red')
            self.doctor_detail = Label(self.ns1, text="Patient details", font=('Ariel', 14, 'italic'))
            self.doctor_detail.place(x=30, y=30)
            self.name = Label(self.ns1, text=" Patient Name", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.name.place(x=30, y=70)

            self.name_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.name_ent.place(x=170, y=70)
            self.add = Label(self.ns1, text="Address", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.add.place(x=30, y=100)
            self.add_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.add_ent.place(x=170, y=100)
            self.age = Label(self.ns1, text="age", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.age.place(x=30, y=160)
            self.age_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.age_ent.place(x=170, y=160)
            self.phone = Label(self.ns1, text="phone number", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.phone.place(x=30, y=220)
            self.phone_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.phone_ent.place(x=170, y=221)
            self.admit = Label(self.ns1, text="Admitted date", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.admit.place(x=30, y=280)
            self.admit_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.admit_ent.place(x=170, y=281)

            today = date.today()
            self.admit_ent.insert(0, today)

            self.disease = Label(self.ns1, text="Patient diseases", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.disease.place(x=30, y=340)
            self.disease_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.disease_ent.place(x=190, y=341)
            self.ward = Label(self.ns1, text="patient ward no:", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.ward.place(x=30, y=400)
            self.ward_ent = Entry(self.ns1, font=('Ariel', 14, 'italic'))
            self.ward_ent.place(x=190, y=401)
            self.gender = Label(self.ns1, text="Gender", bg='red', fg='white', font=('Ariel', 14, 'italic'))
            self.gender.place(x=30, y=461)
            self.gender_ent = ttk.Combobox(self.ns1, font=('Ariel', 14, 'italic'), width=14)
            self.gender_ent['values'] = ['Male', 'Female']
            # self.doc_degree.set('--choose---')
            self.gender_ent.place(x=190, y=461)

            self.prakash = Button(self.ns1, text='Save', font=('Ariel', 14, 'italic'), bg='green',
                                  command=self.patient_user)
            self.prakash.place(x=20, y=500)
            self.prakash1 = Button(self.ns1, text='Update', font=('Ariel', 14, 'italic'), bg='yellow',
                                   command=self.update_user)
            self.prakash1.place(x=130, y=500)
            self.prakash2 = Button(self.ns1, text='Delete', font=('Ariel', 14, 'italic'), bg='red',
                                   command=self.delete_user)
            self.prakash2.place(x=250, y=500)
            self.prakash9 = Button(self.ns1, text='Back', font=('Ariel', 14, 'italic'), bg='red',
                                   command=self.back_button)
            self.prakash9.place(x=1300, y=500)

            self.lbl1 = Label(self.ns1, text='Search', font=('Ariel', 14, 'italic'))
            self.lbl1.place(x=500, y=500)

            ss = ['Patient Name', 'Admitted date', 'Ward', 'Phone']
            self.prakash43 = ttk.Combobox(self.ns1, font=('Ariel', 14, 'italic'), values=ss)
            self.prakash43.place(x=600, y=450)

            self.prakash4 = Button(self.ns1, text='Select', font=('Ariel', 12, 'italic'), bg='yellow',
                                   command=self.search)
            self.prakash4.place(x=850, y=450)

            self.add_tree = ttk.Treeview(self.ns1, column=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',), height=17)
            self.add_tree.place(x=480, y=50)
            self.add_tree['show'] = 'headings'
            self.add_tree.column('a', width=200)
            self.add_tree.column('b', width=200)
            self.add_tree.column('c', width=50)
            self.add_tree.column('d', width=100)
            self.add_tree.column('e', width=100)
            self.add_tree.column('f', width=200)
            self.add_tree.column('g', width=70)
            self.add_tree.column('h', width=100)
            self.add_tree.heading('a', text='Name')
            self.add_tree.heading('b', text='Address')
            self.add_tree.heading('c', text='Age')
            self.add_tree.heading('d', text='Phone no.')
            self.add_tree.heading('e', text='Admitted date')
            self.add_tree.heading('f', text='Diseases')
            self.add_tree.heading('g', text='Ward no.')
            self.add_tree.heading('h', text='Gender')
            self.showdata()
            self.ns1.mainloop()
        except Exception as e:
            print(e)

    def back_button(self):
        self.gui=Gui()
        self.ns1.destroy()
        self.gui.dashboard()

    def patient_user(self):

        try:
            self.db = Aakash()
            patient_name = self.name_ent.get()
            address = self.add_ent.get()

            age = self.age_ent.get()
            phone_number = self.phone_ent.get()

            admitted_date = self.admit_ent.get()
            diseases = self.disease_ent.get()

            ward_number = self.ward_ent.get()
            gender = self.gender_ent.get()

            if patient_name == '' or address == '' or age == '' or phone_number == '' or admitted_date == '' or diseases == '' or ward_number == '' or gender == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''insert into patient_details (patient_name, address, age, gender, phone_number, admitted_date, diseases, ward_number) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
                vals = (patient_name, address, age, gender, phone_number, admitted_date, diseases, ward_number)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'patient details saved')
                self.showdata()
        except Exception as e:
            print(e)

    def button(self):
        try:
            aa = self.name_ent.get()

            self.bipin1 = Label(self.ns1, text=aa, bg='yellow', fg='blue', font=('Ariel', 14, 'bold'))
            self.bipin1.place(x=30, y=100)
            self.ns1.mainloop()
        except Exception as e:
            print(e)

    def update_user(self):
        try:
            self.db = Aakash()
            name = self.name_ent.get()
            add = self.add_ent.get()
            age = self.age_ent.get()
            gender = self.gender_ent.get()
            admit_date = self.admit_ent.get()
            disease = self.disease_ent.get()
            ward = self.ward_ent.get()
            phone = self.phone_ent.get()

            id = (self.update_index)
            print(type(id))
            if name == '' or add == '' or age == '' or gender == '' or admit_date == '' or disease == '' or ward == '' or phone == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''update patient_details SET patient_name=%s, address=%s, age=%s, gender=%s, admitted_date=%s, diseases=%s, 
                ward_number=%s,phone_number=%s WHERE id=%s'''
                vals = (name, add, age, gender, admit_date, disease, ward, phone, id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Update Successful!')
                self.showdata()
        except Exception as e:
            print(e)

    def delete_user(self):
        try:
            self.db = Aakash()

            id = [(self.update_index)]
            print(type(id))
            if id == '':
                messagebox.showerror('Error', 'select item first')
            else:
                qry = '''delete from patient_details where id=%s'''
                vals = (id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Delete Successful!')
                self.showdata()
        except Exception as e:
            print(e)

    def showdata(self):
        self.db = Aakash()
        qry = '''select * from patient_details'''
        getresult = self.db.get_data(qry)
        print(getresult)
        self.add_tree.delete(*self.add_tree.get_children())
        for i in getresult:
            self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            self.add_tree.bind('<Double-1>', self.select_patient)

    def select_patient(self, event):
        try:
            row_selected = self.add_tree.selection()[0]
            select_p = self.add_tree.item(row_selected)
            self.update_index = self.add_tree.item(row_selected, 'text')
            selected_data = self.add_tree.item(row_selected, 'values')
            self.name_ent.delete(0, 'end')
            self.name_ent.insert(0, selected_data[0])
            self.add_ent.delete(0, 'end')
            self.add_ent.insert(0, selected_data[1])

            self.age_ent.delete(0, 'end')
            self.age_ent.insert(0, selected_data[2])
            self.phone_ent.delete(0, 'end')
            self.phone_ent.insert(0, selected_data[3])

            self.admit_ent.delete(0, 'end')
            self.admit_ent.insert(0, selected_data[4])
            self.disease_ent.delete(0, 'end')
            self.disease_ent.insert(0, selected_data[5])

            self.ward_ent.delete(0, 'end')
            self.ward_ent.insert(0, selected_data[6])
            self.gender_ent.delete(0, 'end')
            self.gender_ent.insert(0, selected_data[7])
        except Exception as e:
            print(e)

    def search(self):
        try:
            data = self.prakash43.get()

            if data == '':
                messagebox.showerror('error', 'Select first!')
            elif data == 'Patient Name':

                self.ent1 = Entry(self.ns1, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=490)
                self.ent2 = Button(self.ns1, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_patient_name)
                self.ent2.place(x=850, y=490)
            elif data == 'Admitted date':

                self.ent1 = Entry(self.ns1, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=490)
                self.ent2 = Button(self.ns1, text='Search', font=('Ariel', 14, 'italic'), command=self.searchby_date)
                self.ent2.place(x=850, y=490)

            elif data == 'Ward':

                self.ent1 = Entry(self.ns1, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=490)
                self.ent2 = Button(self.ns1, text='Search', font=('Ariel', 14, 'italic'), command=self.searchby_ward)
                self.ent2.place(x=850, y=490)

            elif data == 'Phone':

                self.ent1 = Entry(self.ns1, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=490)
                self.ent2 = Button(self.ns1, text='Search', font=('Ariel', 14, 'italic'), command=self.searchby_phone)
                self.ent2.place(x=850, y=490)
        except Exception as e:
            print(e)

    def searchby_patient_name(self):
        try:
            self.db = Aakash()

            keyword = self.ent1.get()
            qry = "SELECT * FROM patient_details WHERE patient_name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in data:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                self.add_tree.bind('<Double-1>', self.select_patient)
        except Exception as e:
            print(e)

    def searchby_date(self):
        try:
            self.db = Aakash()

            keyword = self.ent1.get()
            qry = "SELECT * FROM patient_details WHERE admitted_date LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in data:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                self.add_tree.bind('<Double-1>', self.select_patient)
        except Exception as e:
            print(e)

    def searchby_ward(self):
        try:
            self.db = Aakash()

            keyword = self.ent1.get()
            if keyword == '':
                messagebox.showerror('error', 'write some words')
            else:
                qry = "SELECT * FROM patient_details WHERE ward_number LIKE '" + keyword + "%'"
                values = (keyword)
                data = self.db.get_data_p(qry, values)
                self.add_tree.delete(*self.add_tree.get_children())
                for i in data:
                    self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                    self.add_tree.bind('<Double-1>', self.select_patient)
        except Exception as e:
            print(e)

    def searchby_phone(self):
        try:
            self.db = Aakash()

            keyword = self.ent1.get()
            qry = "SELECT * FROM patient_details WHERE phone_number LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in data:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                self.add_tree.bind('<Double-1>', self.select_patient)
        except Exception as e:
            print(e)


class Doctor:
    def __init__(self):
        pass
    def doctor1(self):
        try:
            self.ns2 = Tk()
            self.ns2.geometry('1400x500')
            self.ns2.title('Hospital management system')
            self.ns2.configure(bg='red')
            self.doctor_detail = Label(self.ns2, text="Doctor details", font=('Ariel', 14, 'italic'))
            self.doctor_detail.place(x=30, y=30)
            self.name = Label(self.ns2, text="Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.name.place(x=30, y=70)
            self.name_ent = Entry(self.ns2, font=('Ariel', 14, 'italic'))
            self.name_ent.place(x=170, y=70)

            self.add = Label(self.ns2, text="Address", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.add.place(x=30, y=100)
            self.add_ent = Entry(self.ns2, font=('Ariel', 14, 'italic'))
            self.add_ent.place(x=170, y=100)
            self.phone = Label(self.ns2, text="Phone Number", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.phone.place(x=30, y=140)
            self.phone_ent = Entry(self.ns2, font=('Ariel', 14, 'italic'))
            self.phone_ent.place(x=170, y=140)
            self.available_time = Label(self.ns2, text="Available Time", bg='yellow', fg='blue',
                                        font=('Ariel', 14, 'italic'))
            self.available_time.place(x=30, y=180)
            self.available_time_ent = Entry(self.ns2, font=('Ariel', 14, 'italic'))
            self.available_time_ent.place(x=170, y=180)
            self.doc_specialist = Label(self.ns2, text="specialist", bg='yellow', fg='blue',
                                        font=('Ariel', 14, 'italic'))
            self.doc_specialist.place(x=30, y=220)

            self.doc_specialist_ent = ttk.Combobox(self.ns2, font=('Ariel', 14, 'italic'), width=14)
            self.doc_specialist_ent['values'] = ['Neurologist', 'Cardiologist', 'Endocrinologist', 'Dermatologist',
                                                 'Pathologist']
            # self.doc_degree.set('--choose---')
            self.doc_specialist_ent.place(x=170, y=220)
            self.prakash = Button(self.ns2, text='Save', font=('Ariel', 14, 'italic'), bg='green',
                                  command=self.doctor_user)
            self.prakash.place(x=170, y=250)
            self.prak = Button(self.ns2, text='Back', font=('Ariel', 14, 'italic'), bg='red', command=self.back12)
            self.prak.place(x=170, y=300)
            self.prakash3 = Button(self.ns2, text='Update', font=('Ariel', 14, 'italic'), bg='yellow',
                                   command=self.update_user1)
            self.prakash3.place(x=50, y=250)
            self.prakash4 = Button(self.ns2, text='Delete', font=('Ariel', 14, 'italic'), bg='red',
                                   command=self.delete_user1)
            self.prakash4.place(x=300, y=250)

            self.lbl2 = Label(self.ns2, text='Search', font=('Ariel', 14, 'italic'))
            self.lbl2.place(x=50, y=400)

            self.prakash6 = Button(self.ns2, text='Select', font=('Ariel', 12, 'italic'), bg='blue',
                                   command=self.search1)
            self.prakash6.place(x=350, y=350)
            ss = ['Doctor Name', 'specialist']
            self.prakash65 = ttk.Combobox(self.ns2, font=('Ariel', 14, 'italic'), values=ss)
            self.prakash65.place(x=60, y=350)

            self.app_tree = ttk.Treeview(self.ns2, column=('a', 'b', 'c', 'd', 'e'), height=17)
            self.app_tree.place(x=450, y=20)
            self.app_tree['show'] = 'headings'
            self.app_tree.column('a', width=200)
            self.app_tree.column('b', width=200)
            self.app_tree.column('c', width=100)
            self.app_tree.column('d', width=200)
            self.app_tree.column('e', width=200)
            self.app_tree.heading('a', text='Name')
            self.app_tree.heading('b', text='Address')
            self.app_tree.heading('c', text='Phone')
            self.app_tree.heading('d', text='Available Time')
            self.app_tree.heading('e', text='Specialist')
            self.showdata1()

            self.ns2.mainloop()
        except Exception as e:
            print(e)

    def back12(self):
        self.gui = Gui()
        self.ns2.destroy()
        self.gui.dashboard()

    def doctor_user(self):
        try:
            self.db = Aakash()
            doctor_name = self.name_ent.get()
            address = self.add_ent.get()

            phone = self.phone_ent.get()
            available_time = self.available_time_ent.get()
            specialist = self.doc_specialist_ent.get()

            if doctor_name == '' or address == '' or phone == '' or available_time == '' or specialist == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''insert into doctor_details (name, address, phone,available_time,specialist) values(%s,%s,%s,%s,%s)'''
                vals = (doctor_name, address, phone, available_time, specialist)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'doctor details saved!')
                self.showdata1()
        except Exception as e:
            print(e)

    def button2(self):
        try:
            ab = self.name_ent.get()

            self.bipin2 = Label(self.ns2, text=ab, bg='yellow', fg='blue', font=('Ariel', 14, 'bold'))
            self.bipin2.place(x=30, y=100)
            self.ns2.mainloop()
        except Exception as e:
            print(e)

    def update_user1(self):
        try:
            self.db = Aakash()
            name = self.name_ent.get()
            add = self.add_ent.get()

            phone = self.phone_ent.get()
            available_time = self.available_time_ent.get()
            doc_specialist = self.doc_specialist_ent.get()
            id = (self.update_index)
            print(type(id))
            if name == '' or add == '' or phone == '' or available_time == '' or doc_specialist == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''update doctor_details SET name=%s, address=%s,  phone=%s,  available_time=%s,specialist=%s
                       WHERE id=%s'''
                vals = (name, add, phone, available_time, doc_specialist, id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Update Successful!')
                self.showdata1()
        except Exception as e:
            print(e)

    def delete_user1(self):
        try:
            self.db = Aakash()

            id = [(self.update_index)]
            print(type(id))
            if id == '':
                messagebox.showerror('Error', 'select item first')
            else:
                qry = '''delete from doctor_details where id=%s'''
                vals = (id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Delete Successful!')
                self.showdata1()
        except Exception as e:
            print(e)

    def showdata1(self):
        try:
            self.db = Aakash()
            qry = '''select * from doctor_details'''
            getresult1 = self.db.get_data(qry)
            print(getresult1)

            self.app_tree.delete(*self.app_tree.get_children())
            for i in getresult1:
                self.app_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.app_tree.bind('<Double-1>', self.select_doctor)
        except Exception as e:
            print(e)

    def select_doctor(self, event):
        try:
            row_selected = self.app_tree.selection()[0]
            select_p = self.app_tree.item(row_selected)
            self.update_index = self.app_tree.item(row_selected, 'text')
            selected_data = self.app_tree.item(row_selected, 'values')
            self.name_ent.delete(0, 'end')
            self.name_ent.insert(0, selected_data[0])
            self.add_ent.delete(0, 'end')
            self.add_ent.insert(0, selected_data[1])

            self.phone_ent.delete(0, 'end')
            self.phone_ent.insert(0, selected_data[2])
            self.available_time_ent.delete(0, 'end')
            self.available_time_ent.insert(0, selected_data[3])

            self.doc_specialist_ent.delete(0, 'end')
            self.doc_specialist_ent.insert(0, selected_data[4])
        except Exception as e:
            print(e)

    def search1(self):
        try:
            data = self.prakash65.get()

            if data == '':
                messagebox.showerror('error', 'Select first!')
            elif data == 'Doctor Name':
                self.ent2 = Entry(self.ns2, font=('Ariel', 14, 'italic'))
                self.ent2.place(x=125, y=400)
                self.ent3 = Button(self.ns2, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_doctor_name)
                self.ent3.place(x=360, y=400)

            elif data == 'specialist':

                self.ent2 = Entry(self.ns2, font=('Ariel', 14, 'italic'))
                self.ent2.place(x=125, y=400)
                self.ent3 = Button(self.ns2, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_specialist)
                self.ent3.place(x=360, y=400)
        except Exception as e:
            print(e)

    def searchby_doctor_name(self):
        try:
            self.db = Aakash()

            keyword = self.ent2.get()
            qry = "SELECT * FROM doctor_details WHERE name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.app_tree.delete(*self.app_tree.get_children())
            for i in data:
                self.app_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.app_tree.bind('<Double-1>', self.select_doctor)
        except Exception as e:
            print(e)

    def searchby_specialist(self):
        try:
            self.db = Aakash()

            keyword = self.ent2.get()
            qry = "SELECT * FROM doctor_details WHERE specialist LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.app_tree.delete(*self.app_tree.get_children())
            for i in data:
                self.app_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.app_tree.bind('<Double-1>', self.select_doctor)
        except Exception as e:
            print(e)


class Appoint:
    def __init__(self):
        pass
    def appoint(self):
        try:
            self.ns3 = Tk()
            self.ns3.geometry('1300x400')
            self.ns3.title('Hospital management system')
            self.ns3.configure(bg='red')
            self.appointment = Label(self.ns3, text="Appointment", font=('Ariel', 14, 'italic'))
            self.appointment.place(x=30, y=30)
            self.doc_name = Label(self.ns3, text=" Doctor Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.doc_name.place(x=30, y=70)
            self.doc_name_ent = Entry(self.ns3, font=('Ariel', 14, 'italic'))
            self.doc_name_ent.place(x=200, y=70)
            self.patient_name = Label(self.ns3, text=" Patient Name", bg='yellow', fg='blue',
                                      font=('Ariel', 14, 'italic'))
            self.patient_name.place(x=30, y=100)
            self.patient_name_ent = Entry(self.ns3, font=('Ariel', 14, 'italic'))
            self.patient_name_ent.place(x=200, y=100)
            self.appointment_date = Label(self.ns3, text=" Appointment date", bg='yellow', fg='blue',
                                          font=('Ariel', 14, 'italic'))
            self.appointment_date.place(x=30, y=140)
            self.appointment_date_ent = Entry(self.ns3, font=('Ariel', 14, 'italic'))
            self.appointment_date_ent.place(x=200, y=140)
            self.appointment_time = Label(self.ns3, text=" Appointment time", bg='yellow', fg='blue',
                                          font=('Ariel', 14, 'italic'))
            self.appointment_time.place(x=30, y=180)
            self.appointment_time_ent = Entry(self.ns3, font=('Ariel', 14, 'italic'))
            self.appointment_time_ent.place(x=200, y=180)

            self.prakash = Button(self.ns3, text='Save', font=('Ariel', 14, 'italic'), bg='green',
                                  command=self.appoint_user)
            self.prakash.place(x=170, y=215)
            self.pra = Button(self.ns3, text='Back', font=('Ariel', 14, 'italic'), bg='red', command=self.back11)
            self.pra.place(x=170, y=260)
            self.prakash = Button(self.ns3, text='Update', font=('Ariel', 14, 'italic'), bg='yellow',
                                  command=self.update_user2)
            self.prakash.place(x=50, y=220)
            self.prakash = Button(self.ns3, text='Delete', font=('Ariel', 14, 'italic'), bg='green',
                                  command=self.delete_user2)
            self.prakash.place(x=300, y=220)

            self.lbl3 = Label(self.ns3, text='Search', font=('Ariel', 14, 'italic'))
            self.lbl3.place(x=20, y=350)

            self.prakash8 = Button(self.ns3, text='Select', font=('Ariel', 14, 'italic'), bg='green',
                                   command=self.search2)
            self.prakash8.place(x=320, y=300)
            sp = ['Doctor Name', 'Patient Name']
            self.prakash87 = ttk.Combobox(self.ns3, font=('Ariel', 14, 'italic'), values=sp)
            self.prakash87.place(x=60, y=300)

            self.abc_tree = ttk.Treeview(self.ns3, column=('a', 'b', 'c', 'd'), height=17)
            self.abc_tree.place(x=450, y=20)
            self.abc_tree['show'] = 'headings'
            self.abc_tree.column('a', width=200)
            self.abc_tree.column('b', width=200)
            self.abc_tree.column('c', width=200)
            self.abc_tree.column('d', width=200)
            self.abc_tree.heading('a', text='Doctor Name')
            self.abc_tree.heading('b', text='Patient Name')
            self.abc_tree.heading('c', text='Appointment Date')
            self.abc_tree.heading('d', text='Appointment time')
            self.showdata2()

            self.ns3.mainloop()
        except Exception as e:
            print(e)


    def back11(self):
        self.gui = Gui()
        self.ns3.destroy()
        self.gui.dashboard()

    def appoint_user(self):
        try:
            self.db = Aakash()
            doc_name = self.doc_name_ent.get()
            patient_name = self.patient_name_ent.get()

            appointment_date = self.appointment_date_ent.get()
            appointment_time = self.appointment_time_ent.get()

            if doc_name == '' or patient_name == '' or appointment_date == '' or appointment_time == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''insert into appointment (doc_name, patient_name,appointment_date,appointment_time) values(%s,%s,%s,%s)'''
                vals = (doc_name, patient_name, appointment_date, appointment_time)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'appointment saved!')
                self.showdata2()
        except Exception as e:
            print(e)

    def button3(self):
        try:
            ac = self.doc_name_ent.get()

            self.bipin3 = Label(self.ns3, text=ac, bg='yellow', fg='blue', font=('Ariel', 14, 'bold'))
            self.bipin3.place(x=30, y=100)
            self.ns3.mainloop()
        except Exception as e:
            print(e)

    def showdata2(self):
        try:
            self.db = Aakash()
            qry = '''select * from appointment'''
            getresult2 = self.db.get_data(qry)
            print(getresult2)

            self.abc_tree.delete(*self.abc_tree.get_children())
            for i in getresult2:
                self.abc_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4]))
                self.abc_tree.bind('<Double-1>', self.select_appoint)
        except Exception as e:
            print(e)

    def select_appoint(self, event):
        try:
            row_selected = self.abc_tree.selection()[0]
            select_p = self.abc_tree.item(row_selected)
            self.update_index = self.abc_tree.item(row_selected, 'text')
            selected_data = self.abc_tree.item(row_selected, 'values')
            self.doc_name_ent.delete(0, 'end')
            self.doc_name_ent.insert(0, selected_data[0])
            self.patient_name_ent.delete(0, 'end')
            self.patient_name_ent.insert(0, selected_data[1])

            self.appointment_date_ent.delete(0, 'end')
            self.appointment_date_ent.insert(0, selected_data[2])
            self.appointment_time_ent.delete(0, 'end')
            self.appointment_time_ent.insert(0, selected_data[3])
        except Exception as e:
            print(e)

    def update_user2(self):
        try:
            self.db = Aakash()
            doc_name = self.doc_name_ent.get()
            patient_name = self.patient_name_ent.get()
            appointment_date = self.appointment_date_ent.get()

            appointment_time = self.appointment_time_ent.get()

            id = (self.update_index)
            print(type(id))
            if doc_name == '' or patient_name == '' or appointment_date == '' or appointment_time == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''update appointment SET doc_name=%s, patient_name=%s, appointment_time=%s, appointment_date=%s  
                        WHERE id=%s'''
                vals = (doc_name, patient_name, appointment_date, appointment_time, id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Update Successful!')
                self.showdata2()
        except Exception as e:
            print(e)

    def delete_user2(self):
        try:
            self.db = Aakash()

            id = [(self.update_index)]
            print(type(id))
            if id == '':
                messagebox.showerror('Error', 'select item first')
            else:
                qry = '''delete from appointment where id=%s'''
                vals = (id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Delete Successful!')
                self.showdata2()
        except Exception as e:
            print(e)

    def search2(self):
        try:
            data = self.prakash87.get()

            if data == '':
                messagebox.showerror('error', 'Select first!')
            elif data == 'Doctor Name':

                self.ent3 = Entry(self.ns3, font=('Ariel', 14, 'italic'))
                self.ent3.place(x=95, y=350)
                self.ent4 = Button(self.ns3, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_doc)
                self.ent4.place(x=340, y=350)

            elif data == 'Patient Name':

                self.ent3 = Entry(self.ns3, font=('Ariel', 14, 'italic'))
                self.ent3.place(x=95, y=350)
                self.ent4 = Button(self.ns3, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_pat)
                self.ent4.place(x=340, y=350)
        except Exception as e:
            print(e)

    def searchby_doc(self):
        try:
            self.db = Aakash()

            keyword = self.ent3.get()
            qry = "SELECT * FROM appointment WHERE  doc_name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.abc_tree.delete(*self.abc_tree.get_children())
            for i in data:
                self.abc_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4]))
                self.abc_tree.bind('<Double-1>', self.select_appoint)
        except Exception as e:
            print(e)

    def searchby_pat(self):
        try:
            self.db = Aakash()

            keyword = self.ent3.get()
            qry = "SELECT * FROM appointment WHERE patient_name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.abc_tree.delete(*self.abc_tree.get_children())
            for i in data:
                self.abc_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4]))
                self.abc_tree.bind('<Double-1>', self.select_appoint)
        except Exception as e:
            print(e)


aa = Gui()
aa.ap()
