from .views import ping
from django.test import TestCase
from .models import *

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name='Rishiraj Singh',
                                email='rishi@gmail.com',
                                address='indore',
                                mobile='1234567890',
                                team='Python',
                                )
        Employee.objects.create(name='Rishiraj Singh2',
                                email='rishi@gmail.com',
                                address='indore2',
                                mobile='1234567890',
                                team='Python2',
                                )

    def test_12_employee_test(self):
        obj1 = Employee.objects.get(name='Rishiraj Singh')
        obj2 = Employee.objects.get(name='Rishiraj Singh2')
        obj3 = Employee.objects.get(address='indore')
        self.assertEqual(obj1.name, 'Rishiraj Singh')
        self.assertEqual(obj2.name, 'Rishiraj Singh2')
        self.assertEqual(obj3.address, 'indore')


# class DemoTestCase(TestCase):
    
#     # def test_1(self):
#     #     assert ping() == "data"

#     def test_1_get_method(request):
#         # import pdb;pdb.set_trace()
#         url = 'http://127.0.0.1:8000/ping/'
#         response = request.client.get(url)
#         request.assertEqual(ping(request), "data")


    
       