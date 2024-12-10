#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.onto = load_ontology()
        remove_all_individuals(self.onto)

    def tearDown(self):
        self.onto.destroy()

    def test_given_thing_has_attribute_thing_should_infer(self):

        employee = Thing("employee",self.onto)
        salary = Thing("salary", self.onto)
        employee.hasAttribute.append(salary)    

        sync_reasoner(self.onto)

        self.assertIsInstance(salary, self.onto.Attribute)
        self.assertIn(employee, salary.isAttributeOf)

    def test_given_thing_has_key_thing_should_infer(self):

        employee = Thing("employee",self.onto)
        ssn = Thing("ssn", self.onto)
        employee.hasKey.append(ssn)    

        sync_reasoner(self.onto)

        self.assertIsInstance(employee, self.onto.Entity)
        self.assertIsInstance(employee, self.onto.StrongEntity)
        self.assertIn(employee, ssn.isAttributeOf)
        self.assertIn(employee, ssn.isKeyOf )
        self.assertIn(ssn, employee.hasAttribute) 


    def test_given_thing_hasPartialKey_thing_should_infer(self):

        dependent = Thing("dependent", self.onto)
        dependent_name = Thing("dependentName", self.onto)
        dependent.hasPartialKey.append(dependent_name)

        sync_reasoner(self.onto)

        self.assertIsInstance(dependent, self.onto.Entity)
        self.assertIsInstance(dependent, self.onto.WeakEntity)
        self.assertIn(dependent, dependent_name.isAttributeOf)
        self.assertIn(dependent, dependent_name.isPartialKeyOf)
        self.assertIn(dependent_name, dependent.hasAttribute)

    def test_given_thing_isAttributeOf_thing_should_infer(self):

        dependent = Thing("dependent", self.onto)
        dependent_gender = Thing("dependentGender", self.onto)
        dependent_gender.isAttributeOf.append(dependent)

        sync_reasoner(self.onto)

        self.assertIsInstance(dependent, self.onto.Entity)
        self.assertIsInstance(dependent_gender, self.onto.Attribute)
        self.assertIn(dependent_gender, dependent.hasAttribute)














