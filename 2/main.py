def read_layers(file_path):
	with open(file_path, 'r') as file:
		layers = []
		for line in file:
			layers.append(list(map(int, line.split())))
	return layers

def is_increasing(list):
	return all(list[i] <= list[i+1] for i in range(len(list)-1))

def is_decreasing(list):
	return all(list[i] >= list[i+1] for i in range(len(list)-1))

def is_step_within_range(list):
	return all(1 <= abs(list[i] - list[i+1]) <= 3 for i in range(len(list)-1))

def is_safe_without_removal(layer):
	return (is_increasing(layer) or is_decreasing(layer)) and is_step_within_range(layer)

def is_safe(layer):
	if is_safe_without_removal(layer):
		return True

	for i in range(len(layer)):
		modified_layer = layer[:i] + layer[i+1:]
		if is_safe_without_removal(modified_layer):
			return True

	return False

def filter_layers(layers):
	return [layer for layer in layers if is_safe(layer)]

def main():

	layers = read_layers("unusual-data.txt")
	safe_layers = filter_layers(layers)
	safe_count = len(safe_layers)

	print("Safe layers:")
	for layer in safe_layers:
		print(layer)

	print(f"Number of safe layers: {safe_count}")

if __name__ == "__main__":
	main()
