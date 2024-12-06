#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing


class TestRelationalRules(unittest.TestCase):

    def test_given_some_entity_map_to_relation(self):

        onto = load_ontology()

        remove_all_individuals(onto, [onto.simpleAttributeType])
        
        employee = Thing("employee",onto)
        gender = Thing("gender", onto)
        employee.hasAttribute.append(gender)

        sync_reasoner()        

        self.assertIn(employee, onto.Relation.instances())              

    def test_given_some_entity_has_simple_attribute_map_it_to_attribute_relation(self):

        onto = load_ontology()

        remove_all_individuals(onto,[onto.simpleAttributeType])        
        
        employee = Thing("employee",onto)
        gender = Thing("gender", onto)
        simpleAttributeType = Thing("simpleAttributeType",onto)

        employee.hasAttribute.append(gender)
        gender.hasAttributeType.append(simpleAttributeType)

        sync_reasoner()        

        self.assertIn(employee, onto.Relation.instances())              
        self.assertIn(gender, onto.RelationAttribute.instances())              
        self.assertIn(gender, employee.hasRelationAttribute)              
        

        

if __name__ == '__main__':
    unittest.main()













