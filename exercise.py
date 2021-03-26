
class Profiler:
    """Encapsulate a DNA sequence.

    >>> p = Profiler('CTAGATAGATAGATAGATGACTA')
    >>> p.longest_run('AGAT')
    4
    >>> p.match_suspect('Ada', {'AGAT': 4})
    True
    >>> p.match_suspect('Bia', {'AGAT': 5})
    False

    Using a DNA database (in CSV format):

    >>> with open('sequence.txt') as seq_file:
    ...     s = seq_file.read()
    ...     p = Profiler(s)
    ...     with open('data.csv') as dna_db:
    ...             keys = dna_db.readline().strip().split(',')[1:]
    ...             fpr = {k: 0 for k in keys}
    ...             results = []
    ...             for row in dna_db:
    ...                     cols = row.strip().split(',')
    ...                     for i, k in enumerate(keys):
    ...                             fpr[k] = int(cols[i+1])
    ...                     if p.match_suspect(cols[0], fpr):
    ...                             results.append(cols[0] + " guilty")
    ...                     else:
    ...                             results.append(cols[0] + " innocent")
    ...             results
    ['Andrew innocent', 'Athena innocent', 'Brian innocent', 'Chad innocent', 'David innocent', 'Doug innocent', 'Erin guilty', 'Ian innocent', 'Jelle innocent', 'Kareem innocent', 'Meredith innocent', 'Rodrigo innocent', 'Tara innocent', 'Teagan innocent', 'Valerie innocent']
    """

    def __init__(self, sequence: str):
        """Create a Profiler with a sequence.

        >>> p = Profiler('AAGCT')
        >>> p.seq
        'AAGCT'
        """
        self.seq = sequence

    def longest_run(self, subseq: str) -> int:
        """Return the longest number of repetitions of subseq in the encapsulated DNA sequence.

        >>> p = Profiler('AACCCTGCGCGCGCGCGATCTATCTATCTATCTATCCAGCATTAGCTAGCATCAAGATAGATAGATGAATTTCGAAATGAATGAATGAATGAATGAATGAATG')
        >>> p.longest_run('AGAT')
        3
        >>> p.longest_run('AATG')
        7
        >>> p.longest_run('TATC')
        4
        >>> p = Profiler('CCAGATAGATAGATAGATAGATAGATGTCACAGGGATGCTGAGGGCTGCTTCGTACGTACTCCTGATTTCGGGGATCGCTGACACTAATGCGTGCGAGCGGATCGATCTCTATCTATCTATCTATCTATCCTATAGCATAGACATCCAGATAGATAGATC')
        >>> p.longest_run('AGAT')
        6
        >>> p.longest_run('AATG')
        1
        >>> p.longest_run('TATC')
        5
        """
        pass

    def match_suspect(self, suspect_name: str, dna_fpr: dict[str, int]) -> bool:
        """True if the dna_fpr associated to suspect_name can be found exactly in the DNA sequence. 

        >>> p = Profiler('AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA')
        >>> p.match_suspect('Cain', {'AGAT':5, 'AATG':2, 'TATC':8})
        True
        >>> p.match_suspect('Abel', {'AGAT':3, 'AATG':7, 'TATC':4})
        False
        """
        pass


# Do not change anything below
if __name__ == "__main__":
    import doctest, sys
    f_here, _ = doctest.testmod()
    f_file, _ = doctest.testfile('README.md')
    sys.exit(f_here + f_file)
