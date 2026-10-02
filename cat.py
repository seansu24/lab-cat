import sys

def cat(file, chunk_size=8192):
    """
    Read from the file object in chunks and write to stdout.
    This ensures O(1) memory usage relative to the file size.
    """
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
