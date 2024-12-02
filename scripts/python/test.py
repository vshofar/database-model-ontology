from owlapy.iri import IRI
from owlapy.owl_ontology_manager import OntologyManager

manager = OntologyManager()
onto = manager.load_ontology(IRI.create("file:///home/vbatista/estudo/ontologias/datamodel/owl/owl-functional.ofn"))


'''
sync_reasoner = SyncReasoner(ontology = ontology_path, reasoner="HermiT")
onto = OntologyManager().load_ontology(ontology_path)

for i in onto.classes_in_signature():

    instances=sync_reasoner.instances(i,direct=False)
    print(f"Class:{i}\t Num instances:{len(instances)}")

stopJVM()
'''

