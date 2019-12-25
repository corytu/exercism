def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strand 1 and strand 2 have unequal lengths")
    strand_a_list = list(strand_a)
    strand_b_list = list(strand_b)
    return sum([i != j for i, j in zip(strand_a_list, strand_b_list)])
