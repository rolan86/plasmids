import hashlib
import time

def canonical_form(dna_sequence):
    """Generate the canonical form of a circular DNA sequence for consistent hashing."""
    rotations = [dna_sequence[i:] + dna_sequence[:i] for i in range(len(dna_sequence))]
    return min(rotations)  # Returns the lexicographically smallest rotation

def hash_plasmid(dna_sequence):
    """Hash a plasmid sequence, taking into account its circular nature."""
    start_time = time.time()  # Start timing before processing
    # Convert the sequence to its canonical form
    canonical_sequence = canonical_form(dna_sequence)
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Update the hash object with the canonical form of the sequence
    hash_object.update(canonical_sequence.encode('utf-8'))
    # Calculate the hash
    hash_value = hash_object.hexdigest()
    end_time = time.time()  # End timing after processing
    # Calculate total duration in seconds
    duration = end_time - start_time
    return hash_value, duration

# Example sequence
plasmid_sequence = "TTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAACAAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTCCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAGCAACGCGGCCTTTTTACGGTTCCTGGCCTTTTGCTGGCCTTTTGCTCACATGTTCTTTCCTGCGTTATCCCCTGATTCTGTGGATAACCGTATTACCGCCTTTGAGTGAGCTGATACCGCTCGCCGCAGCCGAACGACCGAGCGCAGCGAGTCAGTGAGCGAGGAAGCGGAAGAGCGCCTGATGCGGTATTTTCTCCTTACGCATCTGTGCGGTATTTCACACCGCAATGGTGCACTCTCAGTACAATCTGCTCTGATGCCGCATAGTTAAGCCAGTATACACTCCGCTATCGCTACGTGACTGGGTCATGGCTGCGCCCCGACACCCGCCAACACCCGCTGACGCGCCCTGACGGGCTTGTCTGCTCCCGGCATCCGCTTACAGACAAGCTGTGACCGTCTCCGGGAGCTGCATGTGTCAGAGGTTTTCACCGTCATCACCGAAACGCGCGAGGCAGCTGCGGTAAAGCTCATCAGCGTGGTCGTGAAGCGATTCACAGATGTCTGCCTGTTCATCCGCGTC"

# Calculate the hash and measure the time
hash_value, time_taken = hash_plasmid(plasmid_sequence)
print("Hash of the plasmid sequence:", hash_value)
print("Time taken to generate the hash:", time_taken, "seconds")

