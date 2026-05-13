# Read number of names
n = int(input().strip())

processed = []  # This will store processed names

# Read each full name
for _ in range(n):
    name = input().strip()
    parts = name.split()
    
    # Last name is the last word
    last_name = parts[-1]
    
    # First letters of all names except the last
    initials = ""
    for p in parts[:-1]:
        initials += p[0] + ". "
    
    # Remove extra space at the end and form final string
    final_name = initials.strip() + " " + last_name
    
    processed.append(final_name)

# Sort alphabetically
processed.sort()

# Print result
for name in processed:
    print(name)
