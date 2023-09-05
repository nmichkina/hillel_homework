"""
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist. Names of people in the format
 "John Dow" first and second name. Find those who are on all blacklists.
"""

casino_blacklist = ["John Dow", "Micle Jackson", "Anna Font", "James Fox"]
pocker_blacklist = ["John Dow", "Amily Fix", "Nataly Black", "Maximilian First"]
alcohol_blacklist = ["John Dow", "Antonio Banderas", "Julia Roberts", "Max Brener"]

common = set(casino_blacklist) & set(pocker_blacklist) & set(alcohol_blacklist)
print(common)
