import spacy

class NLPEngine:
    def __init__(self):
        # Load the medium model for a good balance of speed and accuracy
        try:
            self.nlp = spacy.load("en_core_web_md")
        except OSError:
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_md"])
            self.nlp = spacy.load("en_core_web_md")

    def get_structure(self, text):
        doc = self.nlp(text.lower())
        # Dynamically extract nouns and entities to build the prompt
        return {
            "entities": [(ent.text, ent.label_) for ent in doc.ents],
            "nouns": [chunk.text for chunk in doc.noun_chunks],
            "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
        }