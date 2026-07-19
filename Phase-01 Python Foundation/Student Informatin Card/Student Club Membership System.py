coding_club = {"Krishna", "Rahul", "Aman", "Riya"}

robotics_club = {"Aman", "Riya", "Neha", "Arjun"}

print("=====================STUDENT CLUB MEMBERSHIP SYSTEM=================\n")

print("\nAll Students:\n")
print(coding_club | robotics_club)

print("\nStudents in both clubs:\n")
print(coding_club & robotics_club)

print("\n Only in coding club:\n")
print(coding_club - robotics_club)

print("\n Only in robotics club:\n")
print(robotics_club - coding_club)

print("\nOnly in one club:\n")
print(coding_club ^ robotics_club)