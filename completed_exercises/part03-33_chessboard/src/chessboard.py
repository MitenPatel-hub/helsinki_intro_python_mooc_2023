# Write your solution here
def chessboard(size):
    for row in range(1, size + 1):
        if row % 2 == 1:
            for column in range(1, size + 1):
                if column % 2 == 1:
                    print("1", end="")
                else:
                    print("0", end="")
        else:
            for column in range(1, size + 1):
                if column % 2 == 1:
                    print("0", end="")
                else:
                    print("1", end="")
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(6)
