# validate.py
from generate import generate_scenarios

REQUIREMENT = "A registered user should be able to log in with valid credentials and view their dashboard."

ALLOWED = ["login", "enter", "redirect", "show", "dashboard", "password"]

def is_valid(scenario: str):
    lower = scenario.lower()
    return all(keyword in lower for keyword in ["given", "when", "then"])

def select_happy(scenarios):
    # pick the one that sounds positive
    return [s for s in scenarios if "success" in s.lower() or "valid" in s.lower()]

if __name__ == "__main__":
    scs = generate_scenarios(REQUIREMENT)
    valid = [s for s in scs if is_valid(s)]
    happy = select_happy(valid)

    print("\n✔ Selected HAPPY PATH scenario:\n")
    print(happy[0])
    print("\n")

    # Write feature file dynamically
    with open("features/login.feature", "w") as f:
        f.write("Feature: User login\n\n" + happy[0])

    print("✨ Feature file updated successfully at features/login.feature")
