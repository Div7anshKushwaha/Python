img_extensions = {'jpg', 'jpeg', 'png', 'gif'}
total_size = 0

with open("filename", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        size_str, fname = line.split(",")
        size = int(size_str)

        # convert filename to lowercase
        fname = fname.lower()

        # extract the extension
        ext = fname.split(".")[-1]

        # if it matches an allowed image extension, add size
        if ext in img_extensions:
            total_size += size

print(total_size)
