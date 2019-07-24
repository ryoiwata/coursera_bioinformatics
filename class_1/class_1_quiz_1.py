import operator



def PatternCount(Text, Pattern):
    # fill in your function here
    result = 0
    genome_dic = {}
    
    for num in range(len(Text) - len(Pattern) + 1):
        k_mer = Text[num: num+len(Pattern)]
        # print(three_mer)
        if k_mer == Pattern:
            result += 1
    return result


def FrequentWords(Text, k):
    import operator
    k = int(k)
    result = {}
    genome = Text
    
    for num in range(len(genome) - k + 1):
        k_mer = genome[num: num + k]
        if k_mer in result:
            result[k_mer] += 1
        else: 
            result[k_mer] = 1
    max_occurence = result[max(result.items(), key=operator.itemgetter(1))[0]]
    return [k for k in result if result[k] == max_occurence]

def ReverseComplement(Pattern):
    result = ""
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for char in Pattern:
        result += complement_dict[char]
    return result[::-1]

def PatternMatching(Pattern, Genome):
    """
    Pattern Matching Problem: Find all occurrences of a pattern in a string.
        Input: Two strings, Pattern and Genome.
        Output: All starting positions where Pattern appears as a substring of Genome.
    """
    result = []
    for num in range(len(Genome) - len(Pattern ) + 1):
        k_mer = Genome[num: num + len(Pattern)]
        if k_mer == Pattern:
            result.append(num)
    return result

def ClumpFinding(genome, k, L, t):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    result = []
    for num in range(len(genome) - L + 1):
        k_mer_dict = {}
        window = genome[num:num+L]  
        for num_ in range(len(window) - k + 1):
            k_mer = window[num_: num_ + k]
            if k_mer in k_mer_dict:
                k_mer_dict[k_mer] += 1
            else: 
                k_mer_dict[k_mer] = 1
        result += [k for k in k_mer_dict if k_mer_dict[k] >= t]
    return set(result)

def pattern_to_number(pattern):
    pass


# genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
# print(ClumpFinding(genome, 5, 50, 4))

file = open("dataset_2_10.txt","r")
string = file.read()
string_list = string.split()
print(FrequentWords(string_list[0], string_list[1]))
file.close()
