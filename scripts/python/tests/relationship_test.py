import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery

from python.tests.utils import load_reasoner

class TestRelationshipParticipation(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("Pellet")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)
        
    def test_given_thing_hasRelationshipParticipation_thing_should_infer(self):
        scenario = self._assert.object_property_assertion(
            "dependsOfRelationship",
            "hasParticipation",
            "dependentsOfRelationshipParticipation"
        )

        q1 = self._query.hasType("dependsOfRelationship", "Relationship")
        
        self.assertTrue(scenario.evaluate(q1))















