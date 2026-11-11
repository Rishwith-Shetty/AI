def unify(a, b):
    if a[0] != b[0] or len(a) != len(b):
        return "Unification Failed"

    subs = {}

    for x, y in zip(a[1:], b[1:]):
        if x == y:
            continue
        elif x.startswith("?"):
            subs[x] = y
        elif y.startswith("?"):
            subs[y] = x
        else:
            return "Unification Failed"

    result = tuple(
        subs.get(x, x) for x in a
    )

    return subs, result


# Example
A = ("Eats", "?x", "Apple")
B = ("Eats", "Riya", "?y")

answer = unify(A, B)

print("Expression A:", A)
print("Expression B:", B)
print("Substitutions:", answer[0])
print("Unified Expression:", answer[1])
print("Unification Successful!")
