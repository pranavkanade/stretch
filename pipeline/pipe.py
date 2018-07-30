import spacy

class Pipe(object):
    # This is static/class variable it contains the whole pipeline
    nlp = spacy.load("en")
    def __init__(self):
        pass

    def process_string(self, string):
        # TODO: use this function as a top level function for all the
        #       underlying low level processing.
        pass