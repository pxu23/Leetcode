from collections import deque

def predictPartyVictory(senate: str) -> str:
    banned = [False] * len(senate)

    if len(senate) == 1:
        if senate[0] == "R":
            return "Radiant"
        else:
            return "Dire"
    republic_queue = deque()
    demo_queue = deque()
    for i in range(len(senate)):
        if senate[i] == "R":
            republic_queue.append(("R", i))
        else:
            demo_queue.append(("D", i))

    while True:
        for i in range(len(senate)):
            if not demo_queue:
                return "Radiant"
            if not republic_queue:
                return "Dire"

            if banned[i] == True:
                continue

            if senate[i] == "D":
                _, banned_idx = republic_queue.popleft()
                demo_queue.popleft()
                demo_queue.append(("D", i + len(senate)))
            else:
                _, banned_idx = demo_queue.popleft()
                republic_queue.popleft()
                republic_queue.append(("R", i + len(senate)))

            banned[banned_idx % len(senate)] = True

    return ""

if __name__=="__main__":
    # Example 1
    senate = "RD"
    print(predictPartyVictory(senate))

    # Example 2
    senate = "RDD"
    print(predictPartyVictory(senate))