facts = input("Enter initial fact: ").split(",")
facts = [f.strip() for f in facts]
rules = [
    ("raining", "ground is wet"),
    ("ground is wet", "road is slippery"),
    ("road is slippery", "drive carefully")
]
for condition, conclusion in rules:
    if condition in facts and conclusion not in facts:
        facts.append(conclusion)
print("\nFinal Facts:")
for fact in facts:
    print("-", fact)