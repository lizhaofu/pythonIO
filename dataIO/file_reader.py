file_path = "data//pi_digits.txt"
try:
    with open(file_path) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    msg = "Sorry,the file " + file_path +" does not exit."
    print(msg)

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
