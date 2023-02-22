#!/usr/bin/python3
"""Module test_base_model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing BaseModel functionality """

    def test_id(self):
        """Test id"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """Test created_at"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_updated_at(self):
        """Test updated_at"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str(self):
        """Test str"""
        bm1 = BaseModel()
        self.assertEqual(str(bm1), f"[BaseModel] ({bm1.id}) {bm1.__dict__}")

    def test_save(self):
        """Test save"""
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['created_at'],
                         bm1.created_at.isoformat())
        self.assertEqual(bm1_dict['updated_at'],
                         bm1.updated_at.isoformat())

    def test_kwargs(self):
        """Test kwargs"""
        bm1 = BaseModel()
        bm1.save()
        bm1_dict = bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.created_at, bm2.created_at)
        self.assertEqual(bm1.updated_at, bm2.updated_at)
        self.assertEqual(bm1.__dict__, bm2.__dict__)


if __name__ == '__main__':
    unittest.main()
