#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing


class TestRelationalRules(unittest.TestCase):

    def setUp(self):
        self.onto = load_ontology()
        remove_all_individuals(self.onto, [self.onto.simpleAttributeType])

    def tearDown(self):
        self.onto.destroy()

    def test_given_some_entity_map_to_relation(self):

        employee = Thing("employee",self.onto)
        gender = Thing("gender", self.onto)
        employee.hasAttribute.append(gender)

        sync_reasoner(self.onto)

        self.assertIn(employee, self.onto.Relation.instances())

    def test_given_some_entity_has_simple_attribute_map_it_to_attribute_relation(self):

        employee = Thing("employee", self.onto)
        gender = Thing("gender", self.onto)

        employee.hasAttribute.append(gender)
        gender.hasAttributeType.append(self.onto.simpleAttributeType)

        sync_reasoner(self.onto)

        self.assertIsInstance(employee,self.onto.Relation)
        self.assertIsInstance(gender,self.onto.RelationAttribute)
        self.assertIn(gender,employee.hasRelationAttribute)














