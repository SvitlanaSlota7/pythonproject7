days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

direct_dict = {i: day for i, day in enumerate(days, 1)}

reverse_dict = {day: i for i, day in direct_dict.items()}

print("Direct dictionary:", direct_dict)
print("Reverse dictionary:", reverse_dict)