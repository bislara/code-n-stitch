from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  

def summarize_text(raw_text:str,sentence_count:int) -> str:
    """
    Summarizes a text into a specified number of sentences.

    This function uses the NLTK library to tokenize the text into sentences,
    then uses the sentence tokenizer to tokenize each sentence into words.
    Then, it uses the stopwords library to remove stopwords from the text.
    Then it finds the word frequencey of each word in the text.
    Finally, it uses the heapq library to find the top n sentences in the text.


    Parameters
    ----------
    raw_text : int
        Text to be summarized.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.
    """

    stop_words = set(stopwords.words("english"))
    word_frequencies = {}  
    # Tokenize the text into sentences.
    for word in word_tokenize(raw_text):  
        # Remove all the stopwords from the text.
	    if word not in stop_words:
            # Add the word to the word frequencies.
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1
    
    maximum_frequncy = max(word_frequencies.values())

    # Calculate a weighted count for each word.
    for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_list = sent_tokenize(raw_text)
    sent_scores = {}  
    # Find the score for each sentence.
    for sentence in sentence_list:  
	    for w in word_tokenize(sentence.lower()):
	        if w in word_frequencies.keys():
	            if len(sentence.split(' ')) < 30:
	                if sentence not in sent_scores.keys():
	                    sent_scores[sentence] = word_frequencies[word]
	                else:
	                    sent_scores[sentence] += word_frequencies[word]


    # Find the top n sentences with the highest scores.
    summary_sentences = heapq.nlargest(sentence_count, sent_scores, key=sent_scores.get)

    summary = ' '.join(summary_sentences)  
    return summary
