# MyText module
def word_count(text):
    return len(text.split())

def words_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words)

text = "An apple a day keeps the doctor away"
print("Text:", text)
print("Number of words:", word_count(text))
print("Words from the longest:", ",".join(words_by_length(text)))
print("Words ordered alphabetically:", ",".join(words_alphabetically(text)))
