import os
import time

print("Noble Grant's preformance_testing script")

def test_file_io(file_size_MB):
    # name of the file I want to create and test
    test_file = "test_file"
    
    # Calculate bytes
    file_size_bytes = file_size_MB * 1024 * 1024
    
    # Create file with specified size
    start_time = time.time()
    with open(test_file, 'wb') as f:
        f.write(os.urandom(file_size_bytes))
    creation_time = time.time() - start_time
    
    # Measure read time
    start_time = time.time()
    with open(test_file, 'rb') as f:
        data = f.read()
    read_time = time.time() - start_time

    # Measure write time
    start_time = time.time()
    with open(test_file, 'wb') as f:
        f.write(data)
    write_time = time.time() - start_time
    
    # Cleanup: Remove the test file
    try:
        os.remove(test_file)
    except Exception as e:
        print(f"Error during cleanup: {e}")

    return creation_time, read_time, write_time

def main():
    file_sizes = [1, 10, 100, 500, 1000]  # in MB

    # Print header
    print("\nFile I/O Performance Test Results")
    print("---------------------------------")
    print("{:<15} {:<25} {:<25} {:<25}".format("File Size (MB)", "Creation Time (min)", "Read Time (min)", "Write Time (min)"))
    print("="*100)

    # Perform tests
    for size in file_sizes:
        print(f"{size:<15}", end="")
        creation_time, read_time, write_time = test_file_io(size)
        print("{:<25.6f} {:<25.6f} {:<25.6f}".format(creation_time/60, read_time/60, write_time/60))

    print("\nTests completed successfully.\n\n")

if __name__ == "__main__":
    main()
