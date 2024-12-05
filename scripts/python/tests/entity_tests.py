#!/usr/bin/env -S python -W "ignore"

import unittest 
from utils import *

class TestEntity(unittest.TestCase):

    def test_given_thing_hasAttribute_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        employee = Thing("employee",onto)
        salary = Thing("salary", onto)
        employee.hasAttribute.append(salary)    

        sync_reasoner()        

        self.assertIn(salary, onto.Attribute.instances())        
        self.assertIn(employee, salary.isAttributeOf)        
        

    def test_given_thing_haskey_thing_should_infer(self):

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
        

if __name__ == '__main__':
    unittest.main()













