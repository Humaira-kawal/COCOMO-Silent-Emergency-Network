# COCOMO Cost Estimation
# Problem Statement: Silent Emergency Network

print("======================================")
print("       COCOMO COST ESTIMATION")
print("   Silent Emergency Network")
print("======================================")

# Input: Estimated Lines of Code
loc = float(input("Enter estimated Lines of Code (LOC): "))

# Convert LOC to KLOC
kloc = loc / 1000

print("\nSelect Project Mode:")
print("1. Organic")
print("2. Semi-Detached")
print("3. Embedded")

mode = int(input("Enter your choice: "))

# Basic COCOMO coefficients
if mode == 1:
    a = 2.4
    b = 1.05
    c = 2.5
    d = 0.38
    mode_name = "Organic"

elif mode == 2:
    a = 3.0
    b = 1.12
    c = 2.5
    d = 0.35
    mode_name = "Semi-Detached"

elif mode == 3:
    a = 3.6
    b = 1.20
    c = 2.5
    d = 0.32
    mode_name = "Embedded"

else:
    print("Invalid choice!")
    exit()

# Effort calculation
effort = a * (kloc ** b)

# Development time calculation
development_time = c * (effort ** d)

# Average staff calculation
staff = effort / development_time

print("\n========== RESULTS ==========")
print("Project Name:", "Silent Emergency Network")
print("Project Mode:", mode_name)
print("Estimated LOC:", loc)
print("KLOC:", round(kloc, 2))
print("Effort:", round(effort, 2), "Person-Months")
print("Development Time:", round(development_time, 2), "Months")
print("Average Staff Required:", round(staff, 2))
print("==============================")