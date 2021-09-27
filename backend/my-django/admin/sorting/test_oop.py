import unittest
from admin.sorting.models_oop import Calculator,Contacts, Grade

class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        instance = Calculator(15,5)
        a = instance.add()
        s = instance.subtract()
        m = instance.mulitple()
        d = instance.divice()

        self.assertEqual(a,20)
        self.assertEqual(s,10)
        self.assertEqual(m, 75)
        self.assertEqual(d,3)

class TestContacts(unittest.TestCase):

    def test_get_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom','010-1234','tom@test.com','Seoul'))
        ls.append(Contacts.set_contact('Jane', '010-3334', 'jane@test.com', 'Incheon'))
        ls.append(Contacts.set_contact('Kim', '010-7734', 'kim@test.com', 'Busan'))
        ls = Contacts.get_contacts(ls)
        self.assertEqual(ls[0].name, 'Tom')

    def test_del_contact(self):
        ls = []
        ls.append(Contacts.set_contact('Tom','010-1234','tom@test.com','Seoul'))
        ls.append(Contacts.set_contact('Jane', '010-3334', 'jane@test.com', 'Incheon'))
        ls.append(Contacts.set_contact('Kim', '010-7734', 'kim@test.com', 'Busan'))
        ls = Contacts.del_contact(ls, 'Tom')
        print([x.to_string() for x in ls])
        self.assertEqual(len(ls), 2)


class TestGrade(unittest.TestCase):
    def test_avg(self):
        grade = Grade('Han',60,80,70)
        # print(grade.return_grade())
        self.assertEqual(grade.name, 'Han')
        self.assertEqual(grade.return_grade(), 'C')







if __name__ == '__main__':
    unittest.main