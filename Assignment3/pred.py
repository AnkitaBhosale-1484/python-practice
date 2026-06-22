s="python"
print(id(s))
s=s+"3"
print(id(s))


"""output

2398820351600
2398822814544

reason -id() changes because strings are immutable.
s = "python" creates a string object.
s = s + "3" creates a new string object "python3".
s now refers to the new object.
Therefore, the memory address (id) changes.

"""