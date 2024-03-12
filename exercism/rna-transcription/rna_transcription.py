def to_rna(dna_strand):
    dna_letters = ["G", "C", "T", "A"]
    rna_letters = ["C", "G", "A", "U"]
    rna = ""
    for letter in dna_strand:
        rna += rna_letters[dna_letters.index(letter)]
    return rna