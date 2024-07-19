l2 = [1, 2, 4, 6]

# Find the minimum and maximum values in l2
min_val = min(l2)
max_val = max(l2)

# Create a full range list from min to max
full_range = list(range(min_val, max_val + 1))

# Find missing values by comparing l2 with the full range
missing_values = [item for item in full_range if item not in l2]

# Combine l2 and missing values, then sort the list
l3 = sorted(l2 + missing_values)

print(l3)
