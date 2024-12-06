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

        depends_of_relationship = Thing("dependsOfRelationship",self.onto)
        dependents_of_relationship_participation = Thing("dependetsOfRelationshipParticipation", self.onto)
        depends_of_relationship.hasParticipation.append(dependents_of_relationship_participation)
        
        sync_reasoner()

        self.assertIn(depends_of_relationship, self.onto.Relationship.instances())















