
import re

def convert_to_cnf():
    print("===== FOL TO CNF CONVERSION =====")

    expr = input("\nEnter FOL expression: ")

    print("\n1. Original Expression:")
    print(expr)

    # Step 1: Eliminate implication
    expr = re.sub(r'(\w+)\s*->\s*(\w+)',
                  r'(~\1 | \2)', expr)

    print("\n2. After Eliminating Implication:")
    print(expr)

    # Step 2: Move negation inward
    expr = expr.replace("~~", "")

    print("\n3. After Moving Negation Inward:")
    print(expr)

    # Step 3: Standardize variables
    variables = re.findall(r'(?:FORALL|EXISTS)\s+(\w+)', expr)

    for i, var in enumerate(variables):
        new_var = var + str(i + 1)
        expr = re.sub(r'\b' + var + r'\b', new_var, expr)

    print("\n4. After Standardizing Variables:")
    print(expr)

    # Step 4: Skolemization
    count = 0

    while re.search(r'EXISTS\s+(\w+)', expr):
        count += 1
        var = re.search(r'EXISTS\s+(\w+)', expr).group(1)
        skolem = "SK" + str(count)

        expr = re.sub(r'\b' + var + r'\b', skolem, expr)
        expr = expr.replace("EXISTS", "", 1)

    print("\n5. After Skolemization:")
    print(expr)

    # Step 5: Remove universal quantifiers
    expr = re.sub(r'FORALL\s+\w+', '', expr)

    print("\n6. After Removing Universal Quantifiers:")
    print(expr)

    # Step 6: Final CNF clauses
    print("\n7. Final CNF Clauses:")

    clauses = expr.split("&")

    for i, clause in enumerate(clauses, 1):
        print("Clause", i, ":", clause.strip())

    print("\n===== CNF CONVERSION COMPLETED =====")


convert_to_cnf()
