import math
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. ENTROPY
# ==========================================

def entropy(data):
    target = data["Play"]
    counts = target.value_counts()

    total = len(target)
    ent = 0

    for count in counts:
        probability = count / total
        ent -= probability * math.log2(probability)

    return ent


# ==========================================
# 2. INFORMATION GAIN
# ==========================================

def information_gain(data, attribute):

    total_entropy = entropy(data)

    weighted_entropy = 0

    for value in data[attribute].unique():

        subset = data[data[attribute] == value]

        weighted_entropy += (
            len(subset) / len(data)
        ) * entropy(subset)

    return total_entropy - weighted_entropy


# ==========================================
# 3. ID3 ALGORITHM
# ==========================================

def id3(data, attributes):

    target = data["Play"]

    # If all examples belong to same class
    if len(target.unique()) == 1:
        return target.iloc[0]

    # If no attributes remain
    if len(attributes) == 0:
        return target.value_counts().idxmax()

    # Calculate information gain
    gains = {}

    for attribute in attributes:
        gains[attribute] = information_gain(data, attribute)

    # Select attribute with highest gain
    best_attribute = max(gains, key=gains.get)

    tree = {best_attribute: {}}

    # Create branches
    for value in data[best_attribute].unique():

        subset = data[data[best_attribute] == value]

        remaining_attributes = [
            attr for attr in attributes
            if attr != best_attribute
        ]

        tree[best_attribute][value] = id3(
            subset,
            remaining_attributes
        )

    return tree


# ==========================================
# 4. DATASET
# ==========================================

data = pd.DataFrame({

    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rain",
        "Rain", "Rain", "Overcast", "Sunny",
        "Sunny", "Rain", "Sunny", "Overcast",
        "Overcast", "Rain"
    ],

    "Temperature": [
        "Hot", "Hot", "Hot", "Mild",
        "Cool", "Cool", "Cool", "Mild",
        "Cool", "Mild", "Mild", "Mild",
        "Hot", "Mild"
    ],

    "Humidity": [
        "High", "High", "High", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "High"
    ],

    "Wind": [
        "Weak", "Strong", "Weak", "Weak",
        "Weak", "Strong", "Strong", "Weak",
        "Weak", "Weak", "Strong", "Strong",
        "Weak", "Strong"
    ],

    "Play": [
        "No", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "No",
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "No"
    ]
})


# ==========================================
# 5. DISPLAY INFORMATION GAIN
# ==========================================

attributes = [
    "Outlook",
    "Temperature",
    "Humidity",
    "Wind"
]

print("Entropy of Dataset:",
      round(entropy(data), 4))

print("\nInformation Gain:")

for attribute in attributes:
    gain = information_gain(data, attribute)
    print(attribute, "=", round(gain, 4))


# ==========================================
# 6. BUILD ID3 DECISION TREE
# ==========================================

tree = id3(data, attributes)

print("\nDecision Tree:")
print(tree)


# ==========================================
# 7. DRAW DECISION TREE
# ==========================================

fig, ax = plt.subplots(figsize=(14, 8))

ax.set_xlim(0, 14)
ax.set_ylim(0, 10)

ax.axis("off")

# Store positions
positions = {}


# ------------------------------------------
# Count number of leaves
# ------------------------------------------

def count_leaves(tree):

    if not isinstance(tree, dict):
        return 1

    total = 0

    for child in tree.values():
        total += count_leaves(child)

    return total


# ------------------------------------------
# Draw tree recursively
# ------------------------------------------

def draw_tree(tree, x, y, width, level=0):

    # If leaf node
    if not isinstance(tree, dict):

        if tree == "Yes":
            color = "lightgreen"
        else:
            color = "lightcoral"

        ax.text(
            x,
            y,
            tree,
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5",
                facecolor=color,
                edgecolor="black"
            )
        )

        return

    # Get attribute
    attribute = list(tree.keys())[0]

    children = tree[attribute]

    # Draw decision node
    ax.text(
        x,
        y,
        attribute,
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.6",
            facecolor="lightblue",
            edgecolor="black"
        )
    )

    child_count = len(children)

    # Calculate positions of children
    child_width = width / child_count

    start_x = x - width / 2 + child_width / 2

    child_y = y - 2

    for i, (value, child) in enumerate(children.items()):

        child_x = start_x + i * child_width

        # Draw line
        ax.plot(
            [x, child_x],
            [y - 0.35, child_y + 0.35],
            "k-"
        )

        # Put branch label
        middle_x = (x + child_x) / 2
        middle_y = (y + child_y) / 2

        ax.text(
            middle_x,
            middle_y,
            str(value),
            fontsize=11,
            ha="center",
            va="center"
        )

        # Draw child
        draw_tree(
            child,
            child_x,
            child_y,
            child_width,
            level + 1
        )


# ==========================================
# 8. DRAW THE TREE
# ==========================================

draw_tree(
    tree,
    x=7,
    y=9,
    width=12
)

plt.title(
    "ID3 Decision Tree - Play Tennis",
    fontsize=18,
    fontweight="bold"
)

plt.show()