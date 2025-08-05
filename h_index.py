def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()

    citation_paper_count = {}

    for c in citations:
        citation_paper_count[c] = citation_paper_count.get(c, 0) + 1

    total_papers = len(citations)

    num_papers_with_less_citation = 0
    h_index = 0
    for i in range(len(citations)):
        if i > 0 and citations[i] == citations[i - 1]:
            continue

        num_papers_with_citation = citation_paper_count[citations[i]]
        num_papers_with_at_least_citation = total_papers - num_papers_with_less_citation

        temp = min(citations[i], num_papers_with_at_least_citation)
        h_index = max(h_index, temp)

        num_papers_with_less_citation += num_papers_with_citation

    return h_index

if __name__=="__main__":
    # Example 1
    citations = [3, 0, 6, 1, 5]
    print(hIndex(citations))

    # Example 2
    citations = [1, 3, 1]
    print(hIndex(citations))