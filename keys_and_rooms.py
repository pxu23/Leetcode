def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    visited_rooms = set()
    visited_rooms.add(0)

    stack = [0]

    while len(stack) > 0:
        cur_room = stack.pop()
        keys_room = rooms[cur_room]
        for key in keys_room:
            if key in visited_rooms:
                continue

            visited_rooms.add(key)
            stack.append(key)

    return True if len(visited_rooms) == len(rooms) else False

if __name__=="__main__":
    # Example 1
    rooms = [[1], [2], [3], []]
    print(canVisitAllRooms(rooms))

    # Example 2
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(canVisitAllRooms(rooms))