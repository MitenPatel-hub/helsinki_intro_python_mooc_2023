# Write your solution here
def hash_square(length):
    rows = length
    while rows > 0:
        print("#" * length)
        rows -= 1 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)