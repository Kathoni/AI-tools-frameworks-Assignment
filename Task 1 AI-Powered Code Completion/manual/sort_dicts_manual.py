# Manual implementation to sort a list of dicts by a key
# sort_dicts_manual.py

print("Script started")

def sort_dicts_by_key(data, key):
    """
    Sorts a list of dictionaries based on a specific key.
    """
    return sorted(data, key=lambda x: x[key])

# Only runs this if executed directly, not if imported
if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    
    sorted_data = sort_dicts_by_key(sample_data, "age")
    print("Sorted by age:")
    for item in sorted_data:
        print(item)


