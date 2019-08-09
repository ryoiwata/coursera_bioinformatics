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
    

text = "TTGCAAACCCTCCGCTCCTTGCAAACCCTTGCAAACCCTTGGAACCTTGCAAACCCTTGCAAACCCTTGGAACCTTGCAAACCCTTGGAACCTCCGCTCCGGTGGGAGAATGGCAGGCGGTGGGAGTCCGCTCCTTGGAACCTTGCAAACCCAATGGCAGGCTCCGCTCCAATGGCAGGCGGTGGGAGTTGCAAACCCTTGCAAACCCAATGGCAGGCTTGGAACCTTGGAACCTCCGCTCCTTGGAACCTTGGAACCTTGGAACCTTGGAACCGGTGGGAGTCCGCTCCTCCGCTCCGGTGGGAGAATGGCAGGCTCCGCTCCTTGGAACCGGTGGGAGTTGGAACCTCCGCTCCAATGGCAGGCTTGCAAACCCAATGGCAGGCAATGGCAGGCTTGGAACCAATGGCAGGCAATGGCAGGCTCCGCTCCTTGGAACCTCCGCTCCAATGGCAGGCAATGGCAGGCTTGCAAACCCGGTGGGAGTCCGCTCCAATGGCAGGCTCCGCTCCGGTGGGAGTTGCAAACCCAATGGCAGGCTTGCAAACCCAATGGCAGGCTCCGCTCCTCCGCTCCAATGGCAGGCAATGGCAGGCTTGGAACCTCCGCTCCTTGCAAACCCGGTGGGAGTCCGCTCCAATGGCAGGCTCCGCTCCAATGGCAGGCTTGCAAACCCTTGGAACCAATGGCAGGCGGTGGGAGGGTGGGAGTTGCAAACCCTTGGAACCTTGCAAACCCTCCGCTCCTTGGAACCAATGGCAGGCTTGCAAACCCGGTGGGAGTCCGCTCCTTGCAAACCCTCCGCTCCTTGCAAACCCTTGCAAACCCTTGGAACCAATGGCAGGCTTGCAAACCCGGTGGGAGAATGGCAGGCTCCGCTCCTCCGCTCCTCCGCTCCAATGGCAGGCGGTGGGAGGGTGGGAGGGTGGGAGTCCGCTCCTTGCAAACCCTTGGAACCTCCGCTCCTTGCAAACCC"
pattern = "GCG"

print(frequent_words(text, 13))

# pattern = "CTTGATCAT"
# genome = open("../data/Vibrio_cholerae.txt")
# genome_str = genome.read()

# print(pattern_matching(pattern, genome_str))