from collections import Counter

def read_numbers_from_file(file_path):
	left_numbers = []
	right_numbers = []

	with open(file_path, "r") as input_file:
		for line in input_file:
			left_number, right_number = map(int, line.strip().split())
			left_numbers.append(left_number)
			right_numbers.append(right_number)

	return left_numbers, right_numbers

def calculate_total_distance(left_numbers, right_numbers):
	result = 0
	for left, right in zip(left_numbers, right_numbers):
		result += abs(left - right)
	return result

def calculate_similarity_score(left_numbers, right_numbers):
	right_count = Counter(right_numbers)
	total_similarity_score = 0

	for left in left_numbers:
		total_similarity_score += left * right_count[left]

	return total_similarity_score

def main():

	left_numbers, right_numbers = read_numbers_from_file("input-list.txt")

	left_numbers.sort()
	right_numbers.sort()

	total_distance = calculate_total_distance(left_numbers, right_numbers)

	print("Total Distance:", total_distance)

	total_similarity_score = calculate_similarity_score(left_numbers, right_numbers)
	print("Total Similarity Score:", total_similarity_score)

if __name__ == "__main__":
	main()
