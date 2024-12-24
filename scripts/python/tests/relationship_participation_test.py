import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery

from python.tests.utils import load_reasoner

class TestRelationshipParticipation(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("Pellet")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)
    
    def test_given_thing_hasParticipationEntity_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationEntity",
            "employee"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_thing_hasParticipationCardinality_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationCardinality",
            "one"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_thing_hasParticipationLevel_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationLevel",
            "total"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))












