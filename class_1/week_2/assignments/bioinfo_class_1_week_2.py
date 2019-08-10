def pattern_count(text, pattern):
    #returns the count of occurances of a pattern in a sequence
    count = 0
    for i in range(len(text)):
        #iterate through each nucleotide of the sequence
        if pattern == text[i:i+len(pattern)]:
            #add one if the current sub-sequence is the same as the pattern in question
            count += 1
    return count

def frequent_words(text, k):
    #returns the most frequent subsequence that is length k

    #counting the frequency of every subsequence that is length k
    frequent_patterns = {}
    for i in range(len(text) - k + 1):
        #iterating through each subsequence that is the length k
        subsequence = text[i:i+k]
        if subsequence in frequent_patterns:
            frequent_patterns[subsequence] += 1
        else:
            frequent_patterns[subsequence] = 1

    #iterating through every subsequence, and only keeping the one that has the highest current frequency
    result = []
    for pattern in frequent_patterns:
        if result == []:
            result.append(pattern)
        else:
            if frequent_patterns[pattern] > frequent_patterns[result[0]]:
                result = [pattern]
            elif frequent_patterns[pattern] == frequent_patterns[result[0]]:
                result.append(pattern)
            else:
                pass
    return result

def number_base_convertor(number,base):
    #converts a base 10 number to a number of an identified base
    single_digit_numbers = "0123456789abcdefghijklmnopqrstuvwxyz"
    if number < base:
        return single_digit_numbers[number]
    else:
        return number_base_convertor(number // base, base) + single_digit_numbers[number % base]

def number_base_reverse_convertor(number,base):
    #converts a number with an identified base back to a base 10 number
    print(int(str(number), base))

def number_to_pattern(number):
    #converts a base 10 number to a number of an identified base
    single_digit_numbers = "ACGT"
    if number < 4:
        return single_digit_numbers[number]
    else:
        return number_to_pattern(number // 4) + single_digit_numbers[number % 4]

def pattern_to_number(pattern):
    #converts a pattern to a base 4 number then back to a base 10 number
    base_4_number = ""
    ranking_dict = {"A": "0", "C": "1", "G": "2", "T": "3"}
    
    for letter in pattern:
        base_4_number += ranking_dict[letter]
    return number_base_reverse_convertor(base_4_number, 4)

def computing_frequencies(Text, k):
    #finds the frequency of all k-mer subsequences in the text
    frequency_array = {}

    #step 1 create frequency dictionary
    #initializes a dictionary with all k-mer subsequences in alphabetical order with a value of 0
    for i in range(4 ** k):
        pattern = number_to_pattern(i)
        while len(pattern) < k:
            pattern = "A" + pattern
        frequency_array[pattern] = 0
    
    #step 2 update the frequencies
    #iterates through each k-mer subsequence of the text and updating the frequence dictionary
    for i in range(len(Text) - k + 1):
        subsequence = Text[i: i + k]
        if subsequence in frequency_array:
            frequency_array[subsequence] += 1
    
    #return as a list
    return list(frequency_array.values())
    #return as a dictionary
    return frequency_array

def skew_G_minus_C(text):
    #return the skew 
    # skew is defined as the number of G nucleotides minue C nucleotides for each location of the sequence 
    result = []
    current_skew = 0
    #iterate through each nucleotide of the sequence
    for nucleotide in text:
        result.append(current_skew)
        #change the skew depending on if the nucleotide is G or C
        if nucleotide == "C":
            current_skew -= 1
        elif nucleotide == "G":
            current_skew += 1
    result.append(current_skew)
    return result

def skew_minimum(skew_list):
    #returns the index where the skew is the lowest
    result = []
    i = 0
    for skew in skew_list:
        if result == []:
            result = [i]
        elif skew < skew_list[result[0]]:
            result = [i]
        elif skew == skew_list[result[0]]:
            result.append(i)
        i += 1
    return result

def reverse_compliment(input_string):
    result = ""
    compliment_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    for nucleotide in input_string[::-1]:
        result += compliment_dict[nucleotide]
    return result

def pattern_matching(pattern, genome):
    result = []
    result_str = ""
    for index in range(len(genome) - 1):
        if genome[index:index + len(pattern)] == pattern:
            result.append(index)
            result_str += str(index) + " "
    # return result_str
    return result
    
skew_list = skew_G_minus_C("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
print(skew_minimum(skew_list))