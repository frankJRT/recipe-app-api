from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    
    def test_create_user_with_email_successful(self):
        """validacion de usuario"""
        username ='frank'
        email = 'tets@prueba.com'
        password = 'TestPass123'

        user = get_user_model().objects.create_user(
            #username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        #self.assertEqual(user.username, username)

    def test_new_user_email_normalized(self):
        """test the email for new user is normalizae"""
        email = 'test@PRUEBA.com'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
        

    def tests_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'tets@prueba.com',
            'TestPass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        