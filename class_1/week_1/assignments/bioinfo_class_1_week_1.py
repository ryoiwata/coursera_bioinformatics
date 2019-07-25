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
    

pattern = "CTTGATCAT"
genome = open("../data/Vibrio_cholerae.txt")
genome_str = genome.read()

print(pattern_matching(pattern, genome_str))