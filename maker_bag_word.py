input_file_path = "mot_vide.txt"
output_file_path = "mot_vide2.txt"

unique_lines = set()

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        unique_lines.add(line.strip())

with open(output_file_path, 'w') as output_file:
    output_file.write("\n".join(unique_lines))
