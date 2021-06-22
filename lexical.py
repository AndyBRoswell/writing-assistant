import synonyms


def get_synonyms(word, count = 1):
	return synonyms.nearby(word, count)


def tokenize(text):
	return synonyms.seg(text)
