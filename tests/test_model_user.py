# run these tests:  python -m unittest tests/test_model_user.py

import os
from unittest import TestCase
from sqlalchemy import exc

from models import *

os.environ['DATABASE_URL'] = "postgresql:///fun_dad-test"

from app import app

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()

        self.client = app.test_client()

        self.un_hashed = "TEST_PASSWORD"

        user = User.signup("test_first_name", "test_last_name", "test@test.com",  self.un_hashed)
        user.id = 1234

        db.session.add(user)
        db.session.commit()

        u = User.query.get(user.id)

        self.u = u

    def tearDown(self):
        """Clean up any fowled transactions."""

        db.session.rollback()


    ############################################################
    # User.signup class-method tests 

    def test_signup_class_method(self):
        """Test 'signup', a class method on User."""

        user = User.signup("signup_first_name", "signup_last_name", "signup@test.com", "SIGNUP_TEST_PASSWORD")

        db.session.commit()

        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, "signup_first_name")
        self.assertEqual(user.last_name, "signup_last_name")
        self.assertEqual(user.username_email, "signup@test.com")
        self.assertIsNot(user.password, "SIGNUP_TEST_PASSWORD")
      

    def test_signup_class_method_invalid(self):
        """Does signup class method fail to create a new User if any of the validations (e.g. uniqueness, non-nullable fields) fail?"""
        
        with self.assertRaises(exc.IntegrityError):
            # no first name
            u1 = User.signup(None, "test_last_name", "test1@test.com",  self.un_hashed)
            db.session.add(u1)

            db.session.commit()
        
        with self.assertRaises(exc.IntegrityError):
            db.session.rollback()

            # no last name
            u2 = User.signup("test_first_name", None, "test2@test.com",  self.un_hashed)
            db.session.add(u2)

            db.session.commit()
        
        with self.assertRaises(exc.IntegrityError):
            db.session.rollback()

            # not unique username/email
            u3 = User.signup("test_first_name", "test_last_name", self.u.username_email,  self.un_hashed)
            db.session.add(u3)

            db.session.commit()

        with self.assertRaises(ValueError):
            db.session.rollback()

            # missing password
            u4 = User.signup("test_first_name", "test_last_name", "test4@test.com", None)
            db.session.add(u4)

            db.session.commit()


    ############################################################
    # User.authenticate class-method tests

    def test_User_authenticate_valid(self):
        """Does User.authenticate successfully return a user when given a valid username and password?"""

        u = User.authenticate(self.u.username_email,  self.un_hashed)

        self.assertEqual(u.first_name, self.u.first_name)
        self.assertEqual(u.last_name, self.u.last_name)
        self.assertEqual(u.username_email, self.u.username_email)
        self.assertEqual(u.password, self.u.password)
        # Bcrypt strings should start with $2b$
        self.assertTrue(u.password.startswith("$2b$"))
    
    
    def test_User_authenticate_invalid(self):
        """Does User.authenticate successfully return a user when given a valid username and password?"""

        u1 = User.authenticate(self.u.username_email, "INVALID_PW")

        self.assertFalse(u1)
        db.session.rollback()

        u2 = User.authenticate("INVALID_UN",  self.un_hashed)

        self.assertFalse(u2)
    
    