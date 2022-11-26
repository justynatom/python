import unittest

from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        print("***setUp***")

    @classmethod
    def setUpClass(cls):
        print("------setupclass--------\n")
        cls.studentA = Student('ana', 'smith', 4.6, None)


    def test_email_on_change_name(self):
        studentA = Student('ana','smith', 4.7, None)
        self.assertEqual(cls.studentA.email, 'ana.smith@university.com')

        cls.studentA.name = 'anna'
        self.assertEqual(cls.studentA.email, 'anna.smith@university.com')


    def test_fullname_on_lastname_change(self):
        studentA = Student('Anna', 'Smith', 4.7, None)
        self.assertEqual(studentA.fullname, 'Anna Smith')

        studentA.last = "Kowal"
        self.assertEqual(studentA.fullname, 'Anna Kowal')

    def test_grand_scholarship(self):
        student_granted = Student('Anna', 'Smith', 4.7, None)
        student_ungranted = Student('jon', 'Snow', 3.7, None)

        student_granted.grant_scholarship()
        self.assertTrue(student_granted, True)

        student_ungranted.grant_scholarship()
        self.assertFalse(student_ungranted)


    def tearDown(self):
        print()


if __name__ == "__main__":
    unittest.main()


