import sys

def swap_ie(text):
	translation_table = str.maketrans('ieIE', 'eiEI')
	return text.translate(translation_table)

for line in sys.stdin:
	sys.stdout.write(swap_ie(line))