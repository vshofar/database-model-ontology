import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery
from python.tests.utils import load_reasoner

class TestEntity(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("Pellet")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)

    def test_given_thing_has_attribute_thing_should_infer(self):

        scenario = self._assert.object_property_value("employee", "hasAttribute", "salary")

        q1 = self._query.hasPropertyValue("salary", "isAttributeOf", "employee")
        q2 = self._query.hasType("salary", "Attribute")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))


    def test_given_thing_has_key_thing_should_infer(self):

        scenario = self._assert.object_property_value("employee", "hasKey", "ssn")

        q1 = self._query.hasType("employee", "Entity")
        q2 = self._query.hasType("employee", "StrongEntity")
        q3 = self._query.hasPropertyValue("ssn", "isAttributeOf", "employee")
        q4 = self._query.hasPropertyValue("ssn", "isKeyOf", "employee")
        q5 = self._query.hasPropertyValue("employee", "hasAttribute", "ssn")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))
        self.assertTrue(scenario.evaluate(q5))


    def test_given_thing_hasPartialKey_thing_should_infer(self):

        scenario = self._assert.object_property_value("dependent", "hasPartialKey", "name")

        q1 = self._query.hasType("dependent", "Entity")
        q2 = self._query.hasType("dependent", "WeakEntity")
        q3 = self._query.hasPropertyValue("name", "isAttributeOf", "dependent")
        q4 = self._query.hasPropertyValue("name", "isPartialKeyOf", "dependent")
        q5 = self._query.hasPropertyValue("dependent", "hasAttribute", "name")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))
        self.assertTrue(scenario.evaluate(q5))


    def test_given_thing_isAttributeOf_thing_should_infer(self):

        scenario = self._assert.object_property_value("gender", "isAttributeOf", "dependent")

        q1 = self._query.hasType("dependent", "Entity")
        q2 = self._query.hasType("gender", "Attribute")
        q3 = self._query.hasPropertyValue("dependent", "hasAttribute", "gender")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))















