from collections import deque, defaultdict

def minMutation(startGene: str, endGene: str, bank) -> int:
    def is_mutation(gene1, gene2):
        if len(gene1) != len(gene2):
            return False

        num_char_changed = 0
        for i in range(len(gene1)):
            if gene1[i] != gene2[i]:
                num_char_changed += 1
            if num_char_changed > 1:
                break

        return True if num_char_changed == 1 else False

    adjacency = defaultdict(list)

    for gene in bank:
        if is_mutation(startGene, gene):
            adjacency[startGene].append(gene)
            adjacency[gene].append(startGene)

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            if is_mutation(bank[i], bank[j]):
                adjacency[bank[i]].append(bank[j])
                adjacency[bank[j]].append(bank[i])

    queue = deque()
    queue.append(startGene)
    visited = set()
    visited.add(startGene)

    min_length = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            cur_gene = queue.popleft()
            if cur_gene == endGene:
                return min_length
            for gene in adjacency[cur_gene]:
                if gene in visited:
                    continue
                queue.append(gene)
                visited.add(gene)
        min_length += 1

    return -1

if __name__=="__main__":
    # Example 1
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(minMutation(startGene, endGene, bank))

    # Example 2
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(minMutation(startGene, endGene, bank))