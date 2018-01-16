def to_rna(dna_strand):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    try:
        return "".join(dna_to_rna[x] for x in dna_strand)
    except:
        raise ValueError('Not a valid DNA string')
