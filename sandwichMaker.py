import pyinputplus as pyip

cost = 1.5
response = []
response.append(
    pyip.inputMenu(["wheat", "white", "sourdough"], "Please select a bread type:\n")
)
response.append(
    pyip.inputMenu(
        ["chicken", "turkey", "ham", "tofu"], "Please select your protein:\n"
    )
)

if pyip.inputYesNo("Would you like cheese? ") == "yes":
    response.append(
        pyip.inputMenu(
            ["Cheddar", "Swiss", "Mozzarella"], "Please select a cheese type:\n"
        )
    )
    cost += 0.50

for addition in ["mayo", "mustard", "lettuce", "tomato", "cress"]:
    if pyip.inputYesNo(f"Would you like {addition}? ") == "yes":
        response.append(addition)
        cost = cost + 0.10

nSandwiches = pyip.inputInt("How many sandwiches would you like? ")
print(
    f"You've ordered {nSandwiches} "
    + ", ".join(response[:-1])
    + " and "
    + response[-1]
    + " sandwich"
    + (nSandwiches > 1) * "es"
    + f". That will be £{cost*nSandwiches:.2f} please."
)
