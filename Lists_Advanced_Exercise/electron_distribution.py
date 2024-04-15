number_of_electrons = int(input())
remaining_electrons = number_of_electrons
filled_shells = []
shell_position = 1
for shell_position in range(1, number_of_electrons + 1):
    if remaining_electrons <= 0:
        break
    max_electrons_in_shell = 2 * (shell_position ** 2)
    if remaining_electrons >= max_electrons_in_shell:
        filled_shells.append(max_electrons_in_shell)
        remaining_electrons -= max_electrons_in_shell
    else:
        filled_shells.append(remaining_electrons)
        remaining_electrons = 0

print(filled_shells)