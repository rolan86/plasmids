import hashlib
import time

def minimum_lexicographic_rotation(s):
    """ Find the minimal lexicographic rotation using Booth's algorithm """
    s = s * 2
    f = [-1] * len(s)  # Failure function
    k = 0  # Least rotation of string found so far
    for j in range(1, len(s)):
        sj = s[j]
        i = f[j - k - 1]
        while i != -1 and sj != s[k + i + 1]:
            if sj < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != s[k + i + 1]:  # Mismatch after i matches.
            if sj < s[k]:  # Start new candidate.
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return s[k:k+len(s)//2]

def hash_plasmid(dna_sequence):
    """Hash a plasmid sequence, taking into account its circular nature."""
    canonical_sequence = minimum_lexicographic_rotation(dna_sequence)
    hash_object = hashlib.sha256(canonical_sequence.encode('utf-8'))
    return hash_object.hexdigest()

def test_circular_hash_invariance(dna_sequence):
    """ Test every rotation of the sequence and print the hash to verify invariance. """
    unique_hashes = set()
    sequence_length = len(dna_sequence)
    for i in range(sequence_length):
        rotated_sequence = dna_sequence[i:] + dna_sequence[:i]
        hash_result = hash_plasmid(rotated_sequence)
        unique_hashes.add(hash_result)
        print(f"Rotation {i}: Hash = {hash_result}")

    print("\nTotal unique hashes generated:", len(unique_hashes))
    if len(unique_hashes) == 1:
        print("Success: All rotations produce the same hash.")
    else:
        print("Failure: Different hashes were produced for different rotations, indicating a problem.")

# Example sequence
plasmid_sequence = "TTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAACAAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTCCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAGCAACGCGGCCTTTTTACGGTTCCTGGCCTTTTGCTGGCCTTTTGCTCACATGTTCTTTCCTGCGTTATCCCCTGATTCTGTGGATAACCGTATTACCGCCTTTGAGTGAGCTGATACCGCTCGCCGCAGCCGAACGACCGAGCGCAGCGAGTCAGTGAGCGAGGAAGCGGAAGAGCGCCTGATGCGGTATTTTCTCCTTACGCATCTGTGCGGTATTTCACACCGCAATGGTGCACTCTCAGTACAATCTGCTCTGATGCCGCATAGTTAAGCCAGTATACACTCCGCTATCGCTACGTGACTGGGTCATGGCTGCGCCCCGACACCCGCCAACACCCGCTGACGCGCCCTGACGGGCTTGTCTGCTCCCGGCATCCGCTTACAGACAAGCTGTGACCGTCTCCGGGAGCTGCATGTGTCAGAGGTTTTCACCGTCATCACCGAAACGCGCGAGGCAGCTGCGGTAAAGCTCATCAGCGTGGTCGTGAAGCGATTCACAGATGTCTGCCTGTTCATCCGCGTC"

# Run the test function
start = time.time()
print (hash_plasmid(plasmid_sequence))
test_circular_hash_invariance(plasmid_sequence)
print(len(plasmid_sequence))
end = time.time()

print((end - start)*10)
