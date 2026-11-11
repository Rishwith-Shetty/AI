KB = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]

# Rules: (Premises, Conclusion)
rules = [
    (
        [("Missile", "?x")],
        ("Weapon", "?x")
    ),
    (
        [("Enemy", "?x", "America")],
        ("Hostile", "?x")
    ),
    (
        [("Missile", "?x"), ("Owns", "A", "?x")],
        ("Sells", "Robert", "?x", "A")
    ),
    (
        [
            ("American", "?p"),
            ("Weapon", "?q"),
            ("Sells", "?p", "?q", "?r"),
            ("Hostile", "?r")
        ],
        ("Criminal", "?p")
    )
]


# Match a pattern with a fact
def match(pattern, fact, substitution):

    if pattern[0] != fact[0] or len(pattern) != len(fact):
        return None

    sub = substitution.copy()

    for p, f in zip(pattern[1:], fact[1:]):

        if p.startswith("?"):
            if p in sub and sub[p] != f:
                return None
            sub[p] = f

        elif p != f:
            return None

    return sub


# Find all possible substitutions for rule premises
def find_matches(premises, facts, substitution=None):

    if substitution is None:
        substitution = {}

    if not premises:
        return [substitution]

    results = []

    first = premises[0]

    for fact in facts:
        sub = match(first, fact, substitution)

        if sub is not None:
            results.extend(
                find_matches(premises[1:], facts, sub)
            )

    return results


# Apply substitutions to a conclusion
def apply_substitution(expression, substitution):
    return tuple(
        substitution.get(item, item) for item in expression
    )


# Forward Chaining Function
def forward_chaining(KB, rules):

    iteration = 1

    while True:
        new_facts = []

        for premises, conclusion in rules:

            substitutions = find_matches(premises, KB)

            for sub in substitutions:
                fact = apply_substitution(conclusion, sub)

                if fact not in KB and fact not in new_facts:
                    new_facts.append(fact)

        if not new_facts:
            break

        print(f"\nIteration {iteration}:")
        for fact in new_facts:
            print("New Fact:", fact)

        KB.extend(new_facts)
        iteration += 1

    return KB


# Main Program
print("INITIAL KNOWLEDGE BASE")
for fact in KB:
    print(fact)

print("\nFORWARD CHAINING STARTED")

KB = forward_chaining(KB, rules)

print("\nFINAL KNOWLEDGE BASE")
for fact in KB:
    print(fact)

# Check the goal
print("\nGOAL: Criminal(Robert)")

if ("Criminal", "Robert") in KB:
    print("SUCCESS: Robert is a Criminal!")
else:
    print("FAILURE: Goal cannot be proved.")
