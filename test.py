def read_coordinate_lists_from_file(file_path):
    coordinate_lists = []
    with open(file_path, 'r') as file:
        coordinate_list = []
        for line in file:
            if line.strip():  # Check if the line is not empty
                # Parse the line to extract coordinates
                coordinates = tuple(map(float, line.split()))
                coordinate_list.append(coordinates)
            else:
                # Append the current coordinate list and reset for the next list
                if coordinate_list:
                    coordinate_lists.append(coordinate_list)
                    coordinate_list = []
        # Append the last coordinate list if it's not empty
        if coordinate_list:
            coordinate_lists.append(coordinate_list)
    return coordinate_lists

# Example usage:
file_path = 'preset_pos'  # Update with the actual file path
lists_of_coordinates = read_coordinate_lists_from_file(file_path)
print(lists_of_coordinates)
