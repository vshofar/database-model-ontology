from owlapy.owl_reasoner import SyncReasoner

from python.experiment.owlapy.utils import remove_object_property_assertions


def load_reasoner(name):
    ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
    reasoner = SyncReasoner(ontology=ontology_path, reasoner=name)
    return reasoner