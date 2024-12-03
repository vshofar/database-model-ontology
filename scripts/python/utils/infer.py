#!/usr/bin/env python 

from owlapy.iri import IRI
from owlapy.owl_ontology_manager import OntologyManager
from owlapy.owl_reasoner import SyncReasoner
from owlapy.static_funcs import stopJVM

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl"
sync_reasoner = SyncReasoner(ontology = ontology_path, reasoner="HermiT")
onto = OntologyManager().load_ontology(ontology_path)

onto.save(IRI.create("/home/vbatista/estudo/ontologias/datamodel/owl/original.ofn"))


'''
sync_reasoner.infer_axioms_and_save(output_path="/home/vbatista/estudo/ontologias/datamodel/owl/inferred.ofn",
                       output_format="rdf/xml",
                       inference_types=[
                           "InferredClassAssertionAxiomGenerator",
                           "InferredEquivalentClassAxiomGenerator",
                           "InferredDisjointClassesAxiomGenerator",
                                        "InferredSubClassAxiomGenerator",
                                        "InferredInverseObjectPropertiesAxiomGenerator",
                                        "InferredEquivalentClassAxiomGenerator"])
'''


