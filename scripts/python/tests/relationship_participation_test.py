#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing


class TestRelationshipParticipation(unittest.TestCase):

    def test_given_thing_hasParticipationEntity_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        employee = Thing("employee",onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", onto)
        dependetsOfRelationshipParticipation.hasParticipationEntity.append(employee)
        

        sync_reasoner()        

        self.assertIn(dependetsOfRelationshipParticipation, onto.RelationshipParticipation.instances())


    def test_given_thing_hasParticipationCardinality_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        one = Thing("one",onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", onto)
        dependetsOfRelationshipParticipation.hasParticipationCardinality.append(one)
        

        sync_reasoner()        

        self.assertIn(dependetsOfRelationshipParticipation, onto.RelationshipParticipation.instances())              


    def test_given_thing_hasParticipationLevel_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        total = Thing("total",onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", onto)
        dependetsOfRelationshipParticipation.hasParticipationLevel.append(total)
        

        sync_reasoner()        

        self.assertIn(dependetsOfRelationshipParticipation, onto.RelationshipParticipation.instances())              

    
        

if __name__ == '__main__':
    unittest.main()













