import unittest

from funowl import ClassAxiom
from owlapy.class_expression import OWLClassExpression, OWLClass, OWLObjectSomeValuesFrom

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery
from python.experiment.owlapy.utils import print_query_result, print_ident

from python.tests.utils import load_reasoner

class TestRelationalRules(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("HermiT")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)

    def test_given_one_to_many_relationship_relation_foreign_key(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasAttribute", "name")
            .object_type("dependsOfDependentParticipation", "ManyCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q0 = self._query.hasPropertyValue("ssn", "isForeignKeyOf", "dependent")

        self.assertTrue(scenario.evaluate(q0))




















