students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
modulo = students % group_size

groups = students // group_size + -(-modulo // group_size)

print(f"Number of groups formed: {groups}")