def extended_euclidean_algorithm_modified(a, b):
    # Initial values
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    table = []

    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2

        # Record the values in the table
        table.append((q, r1, r2, r, s1, s2, s, t1, t2, t))

        # Update values
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    # Ensure the multiplicative inverse is positive
    if s1 < 0:
        s1 += a

    return table, s1

def print_modified_table(table):
    header = ["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"]
    print(f"{header[0]:>5} {header[1]:>5} {header[2]:>5} {header[3]:>5} {header[4]:>5} {header[5]:>5} {header[6]:>5} {header[7]:>5} {header[8]:>5} {header[9]:>5}")
    print("-" * 70)
    for row in table:
        print(f"{row[0]:>5} {row[1]:>5} {row[2]:>5} {row[3]:>5} {row[4]:>5} {row[5]:>5} {row[6]:>5} {row[7]:>5} {row[8]:>5} {row[9]:>5}")

# Example usage for modulus 180 and integer 11
modulus = 10
integer = 3

modified_table, multiplicative_inverse = extended_euclidean_algorithm_modified(modulus, integer)

print_modified_table(modified_table)
print(f"\nMultiplicative Inverse of {integer} in Z_{modulus} is: {multiplicative_inverse}")