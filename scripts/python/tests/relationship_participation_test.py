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
    
    def test_given_thing_hasParticipationEntity_thing_should_infer(self):

        employee = Thing("employee",self.onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", self.onto)
        dependetsOfRelationshipParticipation.hasParticipationEntity.append(employee)

        sync_reasoner(self.onto)

        self.assertIn(dependetsOfRelationshipParticipation, self.onto.RelationshipParticipation.instances())


    def test_given_thing_hasParticipationCardinality_thing_should_infer(self):

        one = Thing("one",self.onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", self.onto)
        dependetsOfRelationshipParticipation.hasParticipationCardinality.append(one)

        sync_reasoner(self.onto)

        self.assertIn(dependetsOfRelationshipParticipation, self.onto.RelationshipParticipation.instances())              


    def test_given_thing_hasParticipationLevel_thing_should_infer(self):

        total = Thing("total",self.onto)
        dependetsOfRelationshipParticipation = Thing("dependetsOfRelationshipParticipation", self.onto)
        dependetsOfRelationshipParticipation.hasParticipationLevel.append(total)

        sync_reasoner(self.onto)

        self.assertIn(dependetsOfRelationshipParticipation, self.onto.RelationshipParticipation.instances())












