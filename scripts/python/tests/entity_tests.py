#!/usr/bin/env -S python -W "ignore"

import unittest 
from utils import *

class TestEntity(unittest.TestCase):

    def test_given_employee_haskey_ssn_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        entity = onto.Entity
        strongEntity = onto.StrongEntity
        employee = Thing("employee",onto)
        ssn = Thing("ssn", onto)
        employee.hasKey.append(ssn)    

        sync_reasoner()        

        self.assertIn(employee, entity.instances())        
        self.assertIn(employee, strongEntity.instances())        
        self.assertIn(employee, ssn.isAttributeOf)
        self.assertIn(employee, ssn.isKeyOf )
        self.assertIn(ssn, employee.hasAttribute) 
        

if __name__ == '__main__':
    unittest.main()













