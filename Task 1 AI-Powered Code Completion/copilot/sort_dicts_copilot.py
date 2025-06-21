def sort_list_of_dicts(lst, key, reverse=False):
    """
    Sorts a list of dictionaries by the specified key.

    Args:
        lst (list): List of dictionaries to sort.
        key (str): The key to sort by.
        reverse (bool): Sort in descending order if True.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(lst, key=lambda d: d.get(key, None), reverse=reverse)

if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_data = sort_list_of_dicts(sample_data, "age")
    print("Sorted by age:")
    for item in sorted_data:
        print(item)
