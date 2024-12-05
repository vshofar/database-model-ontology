#!/usr/bin/env -S python -W "ignore"

import unittest 
from utils import *

class TestRelationshipParticipation(unittest.TestCase):

    def test_given_thing_hasRelationshipParticipation_thing_should_infer(self):

        onto = load_ontology()

        remove_all_individuals(onto)        
        
        dependsOfRelationship = Thing("dependsOfRelationship",onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", onto)
        dependsOfRelationship.hasParticipation.append(dependetsOfRelationshipParticipation)
        

        sync_reasoner()        

        self.assertIn(dependsOfRelationship, onto.Relationship.instances())


if __name__ == '__main__':
    unittest.main()













