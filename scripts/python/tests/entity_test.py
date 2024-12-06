#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing


class TestEntity(unittest.TestCase):

    def test_given_thing_has_attribute_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        employee = Thing("employee",onto)
        salary = Thing("salary", onto)
        employee.hasAttribute.append(salary)    

        sync_reasoner()        

        self.assertIn(salary, onto.Attribute.instances())        
        self.assertIn(employee, salary.isAttributeOf)        
        

    def test_given_thing_has_key_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        employee = Thing("employee",onto)
        ssn = Thing("ssn", onto)
        employee.hasKey.append(ssn)    

        sync_reasoner()        

        self.assertIn(employee, onto.Entity.instances())        
        self.assertIn(employee, onto.StrongEntity.instances())        
        self.assertIn(employee, ssn.isAttributeOf)
        self.assertIn(employee, ssn.isKeyOf )
        self.assertIn(ssn, employee.hasAttribute) 


    def test_given_thing_hasPartialKey_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        dependent = Thing("dependent",onto)
        dependentName = Thing("dependentName", onto)
        dependent.hasPartialKey.append(dependentName)    

        sync_reasoner()        

        self.assertIn(dependent, onto.Entity.instances())        
        self.assertIn(dependent, onto.WeakEntity.instances())        
        self.assertIn(dependent, dependentName.isAttributeOf)
        self.assertIn(dependent, dependentName.isPartialKeyOf )
        self.assertIn(dependentName, dependent.hasAttribute)         

    def test_given_thing_isAttributeOf_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        dependent = Thing("dependent",onto)
        dependentGender = Thing("dependentGender", onto)
        dependentGender.isAttributeOf.append(dependent)    

        sync_reasoner()        

        self.assertIn(dependent, onto.Entity.instances())                
        self.assertIn(dependentGender, dependent.hasAttribute)        
        self.assertIn(dependentGender, onto.Attribute.instances())    
        

if __name__ == '__main__':
    unittest.main()













