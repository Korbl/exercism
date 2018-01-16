def to_rna(dna_strand):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    rna_string = ""

    for i in dna_strand:
        try:
            rna_string = rna_string + dna_to_rna[i]
        except:
            raise ValueError('Not a valid DNA string')

    return rna_string
