

##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    >>> clean_up('!!!!Anniversary: July 10')
    'anniversary: july 10'
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


def convert_list_to_string(text):
    """ (list of str) -> str
    
    Return a new string which joins all the elements in the list text. All
    characters including punctuations are preserved.
    
    >>> text = ['Brave Old World\n', 'Bob, Dragon and Mary\n']
    >>> convert_list_to_string(text)
    'Brave Old World\nBob, Dragon and Mary\n'
    >>> text = ['Old Macdonald\n', 'in Phoenix, Had a Great life\n', 'Bye\n']
    >>> convert_list_to_string(text)
    'Old Macdonald\nin Phoenix, Had a Great life\nBye\n'
    >>> text = ['Choose\n', 'Red Pill, or\n', 'Blue Pill.\n']
    >>> convert_list_to_string(text)
    'Choose\nRed Pill, or\nBlue Pill.\n'   
    """
    
    string = ''
        
    for word in text:
        string = string + word
        
    return string


def num_words(text):
    """ (list of str) -> float
    
    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.
    
    Return the total number of words in the list of strings text.
    
    >>> text = ['Brave Old World\n', 'Bob, Dragon and Mary\n']
    >>> num_words(text)
    7.0
    >>> example = ['Old Macdonald\n', 'in Phoenix, Had a Great life\n', 'Bye\n']
    >>> num_words(example)
    9.0
    >>> database = ['Choose\n', 'Red Pill, or\n', 'Blue Pill.\n']
    >>> num_words(database)
    6.0
    """
    
    string = ''
    
    for word in text:
        string = string + word

    string_text = clean_up(string)
    new_string_list = string_text.split()
    s = 0
    
    for word in new_string_list:
        if word not in """!"',;:.-?)([]<>*#\n\t\r""":
            s = s + 1    
    
    f = float(s)
    
    return f


def num_sentences(text):
    """ (list of str) -> float
    
    Precondition: text contains at least one sentence. A sentence is defined
    as a non-empty string of non-terminating punctuation surrounded by 
    terminating punctuation or beginning or end of file. Terminating 
    punctuation is defined as !?.
    
    Return the number of sentences in the list of strings text.
    
    >>> text = ['Brave Old World\n', 'Bob, Dragon and Mary.\n']
    >>> num_sentences(text)
    1.0
    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> num_sentences(text)
    2.0
    >>> text = ['Alcohol is my friend.\n', 'Can I abandon a friend?\n', 
         'You are hopeless.\n']
    >>> num_sentences(text)
    3.0    
    """
    
    string = convert_list_to_string(text)
        
    clean_string = clean_up(string)
        
    new_text = split_on_separators(clean_string, '!?.')
        
    k = 0
        
    for element in new_text:
        k = k + 1
            
    number_of_sentences = float(k)
    
    return number_of_sentences


def different_words(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.
    
    Return the number of different words in list of str text. This includes
    words that have appeared only once and words that have appeared more than
    once in text. For words that have appeared more than once, each word is 
    counted exactly once.
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> different_words(text)
    8.0
    >>> text = ['Dragon is\n', 'coming, please\n', 'hurry\n']
    >>> different_words(text)
    5.0
    >>> text = ['A\n', 'Ta Ta Ta Ta Ta Ta Ta Ta\n']
    >>> different_words(text)
    2.0
    """
    
    string = convert_list_to_string(text)
    string_text = clean_up(string)
    new_string_list = string_text.split()
    s = 0
    k = 0
    sort_list = []
    unique_list = []
    
    for word in new_string_list:
        if new_string_list.count(word) == 1:
            s = s + 1
        # For words that occur more than once, they are appended to the 
        # sort_list.
        if new_string_list.count(word) > 1:
            sort_list.append(word)
    
    # Append the words that have occurred more than once into unique_list. Each
    # word in unique_list is different from each other.
    for i in range(len(sort_list)):
        if i == 0:
            unique_list.append(sort_list[0])
        elif sort_list[i] not in unique_list:
            unique_list.append(sort_list[i])
    
    # Count the number of words that have appeared more than once and each of
    # them is only counted once.    
    for special in unique_list:
        k = k + 1
    
    number_of_different_words = s + k
    
    float_of_different_words = float(number_of_different_words)
    
    return float_of_different_words


def unique_word(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.
    
    Return the number of words that occur exactly once in list of strings text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> unique_word(text)
    7.0
    >>> text = ['Dragon is\n', 'coming, please\n', 'hurry\n']
    >>> unique_word(text)
    5.0
    >>> text = ['A\n', 'Ta Ta Ta Ta Ta Ta Ta Ta\n']
    >>> unique_word(text)
    1.0    
    """
    
    string = convert_list_to_string(text)
    string_text = clean_up(string)
    new_string_list = string_text.split()
    minimum_once_list = []
    minimum_twice_list = []
        
    i = 0
        
    for word in new_string_list:
        # News words are appended to the minimum_once_list
        if word not in minimum_once_list:
                minimum_once_list.append(word)
        # Words that are already in minimum_once_list are put into the 
        # minimum_twice_list.
        elif word in minimum_once_list:
                minimum_twice_list.append(word)
    
    # Count the number of words that occur exactly once in text.    
    for char in minimum_once_list:
        if char not in minimum_twice_list:
            i += 1
    
    num_unique_words = float(i)
    
    return num_unique_words


##########  Complete the following functions. ############

def average_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.

    Return the average length of all words in text. Surrounding punctuation
    is not counted as part of the words. 

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> average_word_length(text)
    5.142857142857143
    >>> text = ['Dragon is\n', 'coming, please\n', 'hurry\n']
    >>> average_word_length(text)
    5.0
    >>> text = ['Ohaiyo,\n', 'watashi wa ika musume\n']
    >>> average_word_length(text)
    4.8
    """
    
    # To do: Fill in this function's body to meet its specification.
    string = convert_list_to_string(text)   
    string_text = clean_up(string)
    characters = "abcdefghijklmnopqrstuvwxyz-_"
    num_char = 0
    number_of_words = num_words(text)
    
    for s in string_text:
        if s in characters:
            num_char = num_char + 1      
    
    word_length = num_char / number_of_words
        
    return word_length
   
       
def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    >>> text = ['Dragon is\n', 'coming, please\n', 'hurry\n']
    >>> type_token_ratio(text)
    1.0
    >>> text = ['Ohaiyo,\n', 'watashi wa ika musume\n', 'boku wa gozaimasu']
    >>> type_token_ratio(text)
    0.875
    """
  
    # To do: Fill-in this function's body to meet its specification.
    number_of_words = num_words(text)
        
    number_of_different_words = different_words(text)
    
    type_token = number_of_different_words / number_of_words
    
    return type_token
    
                
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and at
    least one str in text contains more than just \n.

    Return the hapax_legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    >>> text = ['A\n', 'TA TA TA TA TA TA TA\n']
    >>> hapax_legomena_ratio(text)
    0.125
    >>> text = ['Ohaiyo,\n', 'watashi wa ika musume\n', 'boku wa gozaimasu']
    >>> hapax_legomena_ratio(text)
    0.75
    """
 
    # To do: Fill-in this function's body to meet its specification.
    number_of_words = num_words(text)
    
    exactly_once_word = unique_word(text)
    
    ratio = exactly_once_word / number_of_words
    
    return ratio
  
    
def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    >>> split_on_separators("Look! What a wonderful, wonderful world.", "!,")
    ['Look', ' What a wonderful', ' wonderful world.']
    >>> split_on_separators("Twinkle, twinkle, little star.", ",")
    ['Twinkle', ' twinkle', ' little star.']
    """
    
    # To do: Complete this function's body to meet its specification.
    # You are not required to keep the two lines below but you may find
    # them helpful. (Hint)
    split_list = []
    accumulate_text = ''
    
    # When a separator or the end of text is reached, the loop will append 
    # the string accumulated thus far to split_list.
    for i in range(len(original)):
        # Accumulate_text will get an empty string after its previous string
        # has been appended to the split_list.
        if original[i] in separators or i == len(original) - 1:
            split_list.append(accumulate_text)
            accumulate_text = ''       
        else:
            accumulate_text = accumulate_text + original[i]
    
    # Add the last character in the string original to the last string element 
    # in split_list.    
    last_item = split_list.pop()
    last_char = original[-1]
    complete = last_item + last_char
    split_list.append(complete)
                        
    return split_list
            
           
def average_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence. A sentence is defined
    as a non-empty string of non-terminating punctuation surrounded by 
    terminating punctuation or beginning or end of file. Terminating 
    punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> average_sentence_length(text)
    17.5
    >>> text = ['Ohaiyo,\n', 'watashi wa ika musume.\n', 'Boku wa gozaimasu.']
    >>> average_sentence_length(text)
    4.0
    >>> text = ['Pierre was right when he said that one must believe in the\n',
            'possibility of happiness in order to be happy,\n', 
            'and I now believe in it.\n', 'Let the dead bury the dead,\n', 
            'but while I am alive,\n', 'I must live and be happy.\n']
    >>> average_sentence_length(text)
    21.5    
    """
    
    # To do: Fill in this function's body to meet its specification.
    number_of_words = num_words(text)
    
    string = convert_list_to_string(text)
    
    clean_string = clean_up(string)
    
    new_text = split_on_separators(clean_string, '!?.')
    
    k = 0
    
    for word in new_text:
        k = k + 1
        
    num_sentences = k
    
    return number_of_words / num_sentences


def avg_sentence_complexity(text):
    """ (list of str) -> float

    Return the average number of phrases per sentence.
    
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of the
    following delimiters ,;: 

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    >>> text = ['Ohaiyo,\n', 'watashi wa ika musume.\n', 'Boku wa gozaimasu.']
    >>> avg_sentence_complexity(text)
    1.5
    >>> text = ['Pierre was right when he said that one must believe in the\n',
            'possibility of happiness in order to be happy,\n', 
            'and I now believe in it.\n', 'Let the dead bury the dead,\n', 
            'but while I am alive,\n', 'I must live and be happy.\n']
    >>> avg_sentence_complexity(text)
    2.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    number_of_sentences = num_sentences(text)
    string = convert_list_to_string(text)
    clean_string = clean_up(string)
    
    # Split the clean_string using the punctuation separators for sentences and
    # phrases.
    phrases = split_on_separators(clean_string, '!?.,;:')
    
    i = 0
    
    for element in phrases:
        i = i + 1
    
    average = i / number_of_sentences
    
    return average
        
        
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative real number indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    >>> sig1 = ["a_string" , 10.0, 0.5, 0.10, 12.9, 8.0]
    >>> sig2 = ["a_string2", 10.0, 0.5, 0.10, 12.9, 8.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    0.0
    >>> sig1 = ["a_string" , 10.6, 0.8, 0.19, 12.8, 8.3]
    >>> sig2 = ["a_string2", 20.1, 3.7, 9.9, 15.0, 8.9]
    >>> weight = [0, 12.5, 12.5, 50.0, 12.5, 12.5]
    >>> compare_signatures(sig1, sig2, weight)
    675.5000000000001
    """
    
    # To do: Fill in this function's body to meet its specification.
    
    s = 0
    
    # Sums up each contribution calculated from the provided equation.
    for i in range(1, len(sig1)):
        s = s + abs(sig2[i] - sig1[i]) * weight[i]
    
    return s

