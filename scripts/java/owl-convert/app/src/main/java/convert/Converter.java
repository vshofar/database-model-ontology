package convert;

import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLDocumentFormat;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.model.OWLOntologyStorageException;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.io.OWLXMLOntologyFormat;

public class Converter {    

    public static void main(String[] args) throws OWLOntologyCreationException, OWLOntologyStorageException {
        IRI origin  = IRI.create("file://"+args[0]);
        IRI dest  = IRI.create("file://"+args[1]);

        OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
        OWLOntology ontology = manager.loadOntology(origin);        
        OWLDocumentFormat originFormat = manager.getOntologyFormat(ontology);

        OWLXMLOntologyFormat destFormat = new OWLXMLOntologyFormat();
        if (originFormat.isPrefixOWLDocumentFormat()) {
            destFormat.copyPrefixesFrom(originFormat.asPrefixOWLDocumentFormat());
        }

        manager.saveOntology(ontology, destFormat, dest);
    }
}
