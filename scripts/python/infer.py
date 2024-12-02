from owlapy.iri import IRI
from owlapy.owl_ontology_manager import OntologyManager
from owlapy.owl_reasoner import SyncReasoner
from owlapy.static_funcs import stopJVM

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl//datamodel-owl.owl"
sync_reasoner = SyncReasoner(ontology = ontology_path, reasoner="HermiT")
onto = OntologyManager().load_ontology(ontology_path)

for i in onto.classes_in_signature():
    instances=sync_reasoner.instances(i,direct=False)
    print(f"Class:{i}\t Num instances:{len(instances)}")

stopJVM()
