import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    # TODO: Read database file into a variable

    data = []
    opjct = {}
    with open(sys.argv[1]) as file:
        opjct = csv.DictReader(file)
        for row in opjct:
            row["AGATC"] = int(row["AGATC"])
            row["AATG"] = int(row["AATG"])
            row["TATC"] = int(row["TATC"])
            data.append(row)

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2]) as file:
        text = file.read()
    # TODO: Find longest match of each STR in DNA sequence
    max_aatg = 0
    max_tatc = 0
    max_agatc = 0
    temp = 0
    start = 0
    while start < len(text):
        subseq1 = text[start: start + 4]
        if (subseq1 == "AATG"):
            temp = longest_match(text[start:], subseq1)
            if (temp > max_aatg):
                max_aatg = temp
            start += temp * 4
            continue
        if (subseq1 == "TATC"):
            temp = longest_match(text[start:], subseq1)
            if (temp > max_tatc):
                max_tatc = temp
            start += temp * 4
            continue
        subseq1 = text[start: start + 5]
        if (subseq1 == "AGATC"):
            temp = longest_match(text[start:], subseq1)
            if (temp > max_agatc):
                max_agatc = temp
            start += temp * 5
            continue
        start += 1
    # TODO: Check database for matching profiles
    for name in data:
        if (name["AGATC"] == max_agatc and name["TATC"] == max_tatc and name["AATG"] == max_aatg):
            print(name["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
