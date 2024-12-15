from owlapy.owl_reasoner import SyncReasoner

from ontology_query import OntologyQuery
from ontology_assert import OntologyAssert

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
reasoner = SyncReasoner(ontology=ontology_path, reasoner="HermiT")

ontology_assert = OntologyAssert(reasoner)
ontology_question = OntologyQuery(reasoner.ontology)

scenario = (
    ontology_assert
        .object_property_assertion("employee", "hasKey", "employeeSSN")
        .object_property_assertion("dependent", "hasPartialKey", "dependentGender")
        .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
        .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
        .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
        .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
)

question = ontology_question.object_property_question("employeeSSN", "isForeignKeyOf", "dependent")

print(scenario.evaluate(question))





