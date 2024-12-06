#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner
from owlready2 import Thing

class TestRelationshipParticipation(unittest.TestCase):

    def setUp(self):
        self.onto = load_ontology()
        remove_all_individuals(self.onto, [self.onto.simpleAttributeType])

    def tearDown(self):
        self.onto.destroy()
        
    def test_given_thing_hasRelationshipParticipation_thing_should_infer(self):

        dependsOfRelationship = Thing("dependsOfRelationship",self.onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", self.onto)
        dependsOfRelationship.hasParticipation.append(dependetsOfRelationshipParticipation)
        
        sync_reasoner()

        self.assertIn(dependsOfRelationship, self.onto.Relationship.instances())















