from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *
from datetime import date




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

            self.prakash = Button(self.ns1, text='Save', font=('Ariel', 14, 'italic'), command=self.patient_user)
            self.prakash.place(x=20, y=500)
            self.prakash1 = Button(self.ns1, text='Update', font=('Ariel', 14, 'italic'), command=self.update_user)
            self.prakash1.place(x=130, y=500)
            self.prakash2 = Button(self.ns1, text='Delete', font=('Ariel', 14, 'italic'), command=self.delete_user)
            self.prakash2.place(x=250, y=500)
            self.prakash9 = Button(self.ns1, text='Back', font=('Ariel', 14, 'italic'), command=self.back_button)
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




        self.ns1.destroy()


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

