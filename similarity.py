def jaccard_similarity(seq1, seq2):
    """
    Computes Jaccard similarity between two AST node sequences
    """
    set1 = set(seq1)
    set2 = set(seq2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    if not union:
        return 0.0

    return round(len(intersection) / len(union) * 100, 2)
