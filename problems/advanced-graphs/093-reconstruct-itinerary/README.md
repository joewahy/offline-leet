# 93. Reconstruct Itinerary (Hard)

`tickets[i] = [from, to]` is an airline ticket for a flight between two airports (given as three-letter codes). Rebuild the trip of a traveller who starts at `"JFK"` and uses every ticket exactly once.

Return the itinerary as the list of airports in visiting order. If several valid itineraries exist, return the one that is smallest in lexical order (compare the airports one by one, as strings). A valid itinerary is guaranteed to exist.

## Examples

```
Input:  tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input:  tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

## Constraints

- `1 <= len(tickets) <= 2000`
- Airport codes are three uppercase letters.
- `from != to` for every ticket, and tickets may repeat.

## Hints

- This is an Eulerian path. Hierholzer's algorithm builds it with a DFS that always takes the smallest destination first and appends airports on the way back.
