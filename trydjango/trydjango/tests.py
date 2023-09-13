from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
    
    def test_secret_key_strength(self):

        SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

        # self.assertEqual( SECRET_KEY , 'abc')
        
        is_strong = validate_password(SECRET_KEY)

        print(is_strong)
    # try:
    #     do_smt
        
    # except Exception as e:
    #     self.fail(e)

