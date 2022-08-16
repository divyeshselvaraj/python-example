import yake

def runModel(full_text):
	max_ngram_size = 1
	
	kw_extractor = yake.KeywordExtractor(top=10, stopwords=None, n=max_ngram_size)
	keywords = kw_extractor.extract_keywords(full_text)
	for kw, v in keywords:
	  print("Keyphrase: ",kw, ": score", v)