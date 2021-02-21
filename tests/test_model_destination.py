# run these tests:  python -m unittest tests/test_model_destination.py

import os
from unittest import TestCase
from sqlalchemy import exc

from models import *

os.environ['DATABASE_URL'] = "postgresql:///fun_dad-test"

from app import app

db.drop_all()
db.create_all()


class DestinationModelTestCase(TestCase):
    """Test Destination model."""

    def setUp(self):
        """Create test client, add sample data."""

        Destination.query.delete()

        self.client = app.test_client()

        dest = Destination(name="test_destination", place_id="test_place_id", latitude=1.0, longitude=2.0)
        dest.id = 1234

        db.session.add(dest)
        db.session.commit()

        d = Destination.query.get(dest.id)

        self.d = d

    def tearDown(self):
        """Clean up any fowled transactions."""

        db.session.rollback()


    ############################################################
    # Destination model tests 

    def test_Destination_model_valid(self):
        """Test if model successfully creates a new row."""

        dest = Destination(name="test_destination", place_id="test_place_id_1", latitude=1.0, longitude=2.0)
        db.session.add(dest)
        db.session.commit()

        self.assertIsInstance(dest, Destination)
        self.assertEqual(dest.name, "test_destination")
        self.assertEqual(dest.place_id, "test_place_id_1")
        self.assertEqual(dest.latitude, 1.0)
        self.assertIsNot(dest.longitude, 2.0)
      

    def test_Destination_model_invalid(self):
        """Does destination model fail to create a new row if any of the validations (e.g. uniqueness, non-nullable fields) are invalid?"""
        
        with self.assertRaises(exc.IntegrityError):
            # missing name
            d1 = Destination(name=None, place_id="test_place_id_1", latitude=1.0, longitude=2.0)
            db.session.add(d1)

            db.session.commit()
        
        with self.assertRaises(exc.IntegrityError):
            db.session.rollback()

            # missing place id
            d2 = Destination(name="test_destination", place_id=None, latitude=1.0, longitude=2.0)
            db.session.add(d2)

            db.session.commit()
        
        with self.assertRaises(exc.IntegrityError):
            db.session.rollback()

            # missing latitude
            d3 = Destination(name="test_destination", place_id="test_place_id_3", latitude=None, longitude=2.0)
            db.session.add(d3)

            db.session.commit()

        with self.assertRaises(exc.IntegrityError):
            db.session.rollback()

            # missing longitude
            d4 = Destination(name="test_destination", place_id="test_place_id_4", latitude=1.0, longitude=None)
            db.session.add(d4)

            db.session.commit()


    