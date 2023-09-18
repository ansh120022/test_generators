def compare_tsv_structure(file1_path, file2_path):
    # Read the header (first line) of the first TSV file
    with open(file1_path, 'r') as file1:
        header1 = file1.readline().strip().split('\t')

    # Read the header (first line) of the second TSV file
    with open(file2_path, 'r') as file2:
        header2 = file2.readline().strip().split('\t')

    # Compare the headers to check if they have the same structure
    if header1 == header2:
        return True
    else:
        return False


def compare_tsv_data(file1_path, file2_path):
    # Read the contents of the first TSV file
    with open(file1_path, 'r') as file1:
        lines1 = file1.readlines()

    # Read the contents of the second TSV file
    with open(file2_path, 'r') as file2:
        lines2 = file2.readlines()

    # Initialize a list to store the differing lines
    differing_lines = []

    # Compare the content line by line
    for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        # Split each line into fields using tab as the delimiter
        fields1 = line1.strip().split('\t')
        fields2 = line2.strip().split('\t')

        # Check if the number of fields in both lines is the same
        if len(fields1) != len(fields2):
            differing_lines.append(f"Line {line_num}: Number of fields is different")
        else:
            # Compare each field in the lines
            for field_num, (field1, field2) in enumerate(zip(fields1, fields2), start=1):
                if field1 != field2:
                    differing_lines.append(f"Line {line_num}, Field {field_num}: '{field1}' != '{field2}'")

    return differing_lines


file1_path = '15.tsv'
file2_path = '16.tsv'


is_structure_equal = compare_tsv_structure(file1_path, file2_path)
if is_structure_equal is True:
    differences = compare_tsv_data(file1_path, file2_path)
    if differences:
        print("Differences found between the TSV files:")
        for diff in differences:
            print(diff)
    else:
        print("No differences found between the TSV files.")
else:
    print("The TSV files have different structure (headers).")

