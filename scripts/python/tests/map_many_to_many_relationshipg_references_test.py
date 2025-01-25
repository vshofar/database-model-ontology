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

    def test_given_many_to_many_relationship_map_relationship_relation(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasKey", "name")
            .object_type("dependsOfDependentParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q0 = self._query.hasType("dependsOf", "Relation")

        self.assertTrue(scenario.evaluate(q0))

    def test_given_many_to_many_relationship_map_relationship_relation_composed_key_parts(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasKey", "name")
            .object_type("dependsOfDependentParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q0 = self._query.hasPropertyValue("dependsOf", "hasComposedKeyComponent", "ssn")
        q1 = self._query.hasPropertyValue("dependsOf", "hasComposedKeyComponent", "name")

        self.assertTrue(scenario.evaluate(q0))
        self.assertTrue(scenario.evaluate(q1))

    def test_given_many_to_many_relationship_map_relationship_relation_foreign_keys(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasKey", "name")
            .object_type("dependsOfDependentParticipation", "ManyCardinalityRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q0 = self._query.hasPropertyValue("dependsOf", "hasForeignKey", "ssn")
        q1 = self._query.hasPropertyValue("dependsOf", "hasForeignKey", "name")

        self.assertTrue(scenario.evaluate(q0))
        self.assertTrue(scenario.evaluate(q1))



















