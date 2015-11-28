def extract_num(input_str):
	if input_str is None or input_str == '':
		return 0

	out_number = ''
	for ele in input_str:
        	if ele.isdigit():
			out_number += ele
        return float(out_number)
