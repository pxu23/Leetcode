def prisonAfterNDays(cells, n):
    visited_cell = {}
    visited_cell[tuple(cells)] = 0
    cycle_detected = False
    cycle_length = 0
    for j in range(1, n + 1):
        copied_cell = cells.copy()
        cells[0] = 0
        cells[-1] = 0
        for i in range(1, 7):
            if copied_cell[i - 1] == 0:
                if copied_cell[i + 1] == 0:
                    cells[i] = 1
                else:
                    cells[i] = 0
            else:
                if copied_cell[i + 1] == 1:
                    cells[i] = 1
                else:
                    cells[i] = 0
        # print(tuple(cells))
        if tuple(cells) in visited_cell:
            cycle_length = j - visited_cell[tuple(cells)]
            cycle_detected = True
            break

        visited_cell[tuple(cells)] = j

    if cycle_detected:
        remain = (n - visited_cell[tuple(cells)]) % cycle_length
        for _ in range(remain):
            copied_cell = cells.copy()
            cells[0] = 0
            cells[-1] = 0
            for i in range(1, 7):
                if copied_cell[i - 1] == 0:
                    if copied_cell[i + 1] == 0:
                        cells[i] = 1
                    else:
                        cells[i] = 0
                else:
                    if copied_cell[i + 1] == 1:
                        cells[i] = 1
                    else:
                        cells[i] = 0
    return cells

if __name__=="__main__":
    # Example 1
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    n = 7
    print(prisonAfterNDays(cells, n))

    # Example 3
    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    n = 1000000000
    print(prisonAfterNDays(cells, n))