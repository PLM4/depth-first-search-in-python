def limitedDepthSearch():
    initial_state = int(input("Enter the initial number: "))
    target = int(input("Enter the target number: "))
    depth_limit = int(input("Enter the depth limit: "))

    visited = set()
    nodes_visited = 0

    def depth_limited_search(current_state, path, current_depth):
        nonlocal nodes_visited
        nodes_visited += 1

        path.append(current_state)
        visited.add(current_state)

        if current_state == target:
            return path.copy()
        
        if current_depth >= depth_limit:
            path.pop()
            return None
        
        for next_state in [current_state * 2, current_state + 1]:
            if next_state not in visited:
                result = depth_limited_search(next_state, path, current_depth + 1)
                if result is not None:
                    return result
        
        path.pop()
        return None
    
    result = depth_limited_search(initial_state, [], 0)

    if result:
        print(f"Path taken: {result}")
        print(f"Number of nodes visited: {nodes_visited}")
        print(f"Total cost: {len(result) - 1}")
    else:
        print("Target not found within depth limit")
        print(f"Number of nodes visited: {nodes_visited}")

limitedDepthSearch()