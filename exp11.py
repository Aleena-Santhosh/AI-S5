facts = {
    ("Bird", "is", "animal"),
    ("Tweety", "is", "bird")}
rules = [
    (("X", "is", "bird"), ("X", "can", "fly"))
]
print("Given Knowledge:")
for f in facts:
    print(f)
for condition, conclusion in rules:
    for fact in list(facts):
        if fact[1:] == condition[1:]:
            new_fact = (fact[0], conclusion[1], conclusion[2])
            facts.add(new_fact)
print("\nDerived Knowledge:")
for f in facts:
    print(f)