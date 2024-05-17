from django.test import TestCase
from .models import Member
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class NewApp(APITestCase):
    
    fixtures = ['main.json']
    
    def setUp(self):
        print("successfull")
    
    # def test_equal(self):
    #     self.assertEqual(1,1)
        
        
    def test_members(self):
        members = ['abx','xyz']
        for member in members:
            obj = Member.objects.create(
                firstname=member
            )
            self.assertEquals(member,obj.firstname)
            
        objs= Member.objects.all()
        
        self.assertEqual(objs.count(),3)
        
    def test_postapi(self):
        _data= {
            "firstname": 'abc',
            "lastname": 'xyz',
            "country" : "india"
        }
        
        _response = self.client.post('/add/',data= _data)
        print(_response.status_code)
        self.assertEquals(_response.status_code, status.HTTP_200_OK)
        
    def test_get_member(self):
        _reponse = self.client.get('',format = "json")
        _data = _reponse 
        print(_data.items)
        self.assertEqual(_reponse.status_code,status.HTTP_200_OK)