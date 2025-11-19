import string
print ("Welcome to Muiz's text analyser")
sentence = input("Enter the sentence you would like analysed: ")
# Removes any and all punctuations
clean_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

#Makes a list of words given a sentence without any punctuation
words = clean_sentence.split(sep = " ")

#Removes any extra white spaces
while '' in words:
   words.remove('')

def word_stats():
    """This function returns a dictionary given a list as input with  
    the word as the key and the frequency as the value"""
    word_count = {}
    for word in words:
        if word in word_count:
          word_count[word] = word_count[word] + 1
        else:
           word_count[word] = 1
    return word_count
def character_length():
   """This character counts the total number of characters in
   a list of characters"""
   characters = 0
   for word in words:
      characters += len(word)
   print(f"Characters: {characters}")
def no_of_words():
   """This function returns the number of words given a list of words"""
   print(f"Words: {len(words) + 1}")
def unique_words():
   """This function prints the  the number of unique words """
   print(f"Unique Words: {len(word_stats())}")   
def most_common():
   """This function returns the most common word in the sentence"""
   maximum = 0
   most = ""
   for word in word_stats().keys():
      if word_stats()[word] > maximum:
         most = word
         maximum = word_stats()[word]
   print(f"Most common word: {most} ({maximum} times)")
print("--- Text Analysis ---")
character_length()
no_of_words()
unique_words()  
most_common()
      

