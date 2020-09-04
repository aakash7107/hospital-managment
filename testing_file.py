import unittest
from final import*
class Testing(unittest.TestCase):

    def test_case(self):

        login = Gui()
        result = login.login_user('aakash','aakash@10')
        self.assertTrue(result)

    def test_case1(self):

        login = Gui()
        result = login.login_user('aakas','aakash@1')
        self.assertFalse(result)

    def test_case3(self):
        register = Gui()
        result = register.register_user('','ads','dsad','sad','da')
        self.assertFalse(result)

    def test_case4(self):
        register = Gui()
        result = register.register_user('sdf','ads','dsad','sad','da')
        self.assertTrue(result)

    def test_case5(self):
        add_patient = Patient()
        result = add_patient.patient_user('','','','','','','','')
        self.assertFalse(result)

    def test_case6(self):
        add_patient = Patient()
        result = add_patient.patient_user('sda', 'cs', 'sad', 'dsaw', 'wd', 'wd', 'qqw', 'dd')
        self.assertTrue(result)

    def test_case7(self):
        add_patient = Patient()
        result = add_patient.delete_user('id')
        self.assertTrue(result)

    def test_case8(self):
        add_patient = Patient()
        result = add_patient.delete_user('')
        self.assertFalse(result)

    def test_case9(self):
        add_patient = Patient()
        result = add_patient.update_user('','','','','','','','','')
        self.assertFalse(result)

    def test_case10(self):
        add_patient = Patient()
        result = add_patient.update_user('das', 'dsad', 'dsad', 'sd', 'dsa', 'das', 'sad', 'saew', 'wew')
        self.assertTrue(result)




