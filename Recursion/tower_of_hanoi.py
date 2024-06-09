def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move 1st disk from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move {n}th disk from {source} to {destination}")
    tower_of_hanoi(n-1, helper, source, destination)

tower_of_hanoi(4, "src", "helper", "dest")