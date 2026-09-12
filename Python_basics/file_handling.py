# File Handling in Python


# --------------------
# WRITING TO A FILE
# --------------------

with open("diary.txt", "w") as file:
    file.write("Hello dear diary!")
    file.write("\nGood to see you!")
    file.write("\nWishing you a great day ahead.")


# --------------------
# READING A FILE
# --------------------

with open("diary.txt", "r") as file:
    content = file.read()
    print(content)


# --------------------
# APPENDING TO A FILE
# --------------------

with open("diary.txt", "a") as file:
    file.write("\nHappy to be here!")


# --------------------
# READING FILE LINE BY LINE
# --------------------

with open("diary.txt", "r") as file:
    lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")