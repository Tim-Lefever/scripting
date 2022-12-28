from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 12)
assert_lines_match_regex(output_file, r'\s+[A-Z][a-z]+ \**')
assert_file_contents_hash_to(output_file, '0e8c5801a9e24ffe6738f9bffe58ecd6b7611707ddec3ec59ebf5511d72f680e1924a5343733b2607e0f0e992dd18b188555845c9b66de981f97abf224ce497a')
compute_code_for_file(output_file)
