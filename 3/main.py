import re

def parse_and_sum_multiplications(file_path):
	try:
		with open(file_path, 'r') as file:
			content = file.read()

		mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
		do_pattern = r"do\(\)"
		dont_pattern = r"don't\(\)"

		is_enabled = True
		total = 0
		position = 0

		while position < len(content):
			if content[position:position + 4] == "do()":
				is_enabled = True
				position += 4

				continue

			elif content[position:position + 7] == "don't()":
				is_enabled = False
				position += 7

				continue

			match = re.match(mul_pattern, content[position:])

			if match:
				x, y = match.groups()
				if is_enabled:
					total += int(x) * int(y)
				position += len(match.group(0))
			else:
				position += 1

		return total

	except FileNotFoundError:
		return "File not found."
	except Exception as e:
		return f"An error occurred: {e}"

if __name__ == "__main__":

	result = parse_and_sum_multiplications('corrupted-memory.txt')
	print(f"Total sum of valid mul(X,Y) results: {result}")
