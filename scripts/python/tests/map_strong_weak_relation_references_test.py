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

    def test_given_relationship_between_strong_and_weak_entity_map_strong_primary_key_as_waeK_foreign_key(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasPropertyValue("ssn", "isForeignKeyOf", "dependent")

        self.assertTrue(scenario.evaluate(q1))

    def test_given_relationship_between_strong_and_weak_entity_map_reference_origin(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasType("dependsOfDependentParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationRelation", "dependent")
        q3 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationSide", "originReferenceParticipationSide")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))

    def test_given_relationship_between_strong_and_weak_entity_map_reference_target(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasType("dependsOfEmployeeParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationRelation", "employee")
        q3 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationSide", "targetReferenceParticipationSide")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))


    def test_given_weak_mapped_relation_with_foreign_key_map_foreign_key_as_composed_key_component(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasPropertyValue("dependent", "hasComposedKeyComponent", "ssn")

        self.assertTrue(scenario.evaluate(q1))

    def test_given_weak_mapped_relation_with_partial_key_map_partial_key_as_composed_key_component(self):
        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasPropertyValue("dependent", "hasComposedKeyComponent", "name")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_relationship_between_strong_and_weak_entity_infer(self):
        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        c = self._query.someClass("Relation")
        relations = scenario.search(c)

        print()
        for r in relations:
            print()
            print_ident("Relation = {relation}".format(relation=r.reminder), 0)

            print_ident("RelationAttributes...", 1)
            c = self._query.object_has_value("isRelationAttributeOf", r.reminder)
            attributes_of = scenario.search(c)
            print_query_result(attributes_of, only_name=True, ident=2)

            print_ident("PrimaryKey...", 1)
            c = self._query.object_has_value("isPrimaryKeyOf", r.reminder)
            primary_key_of = scenario.search(c)
            print_query_result(primary_key_of, only_name=True, ident=2)

            print_ident("ForeignKey...", 1)
            c = self._query.object_has_value("isForeignKeyOf", r.reminder)
            foreign_key_of = scenario.search(c)
            print_query_result(foreign_key_of, only_name=True, ident=2)

            print_ident("ComposedKey...", 1)
            c = self._query.object_has_value("isComposedKeyComponentOf", r.reminder)
            composed_key_of = scenario.search(c)
            print_query_result(composed_key_of, only_name=True, ident=2)

            print_ident("References...", 1)
            c = self._query.object_has_value("hasReferenceParticipationRelation", r.reminder)
            reference_participations = scenario.search(c)

            for rp in reference_participations:
                print_ident(rp.reminder, 2)
                c = self._query.object_has_value("isReferenceParticipationRelationAttributeOf", rp.reminder)
                participation_relation_attribute = scenario.search(c)
                print_query_result(participation_relation_attribute, only_name=True, ident=3)

                c = self._query.object_has_value("isReferenceParticipationSideOf", rp.reminder)
                reference_participation_side = scenario.search(c)
                print_query_result(reference_participation_side, only_name=True, ident=3)


















