# relationship_status (python)
def relationship_status(from_member, to_member, social_graph):
    from_follows = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_follows and to_follows:
        return "friends"
    elif from_follows:
        return "follower"
    elif to_follows:
        return "followed by"
    else:
        return "no relationship"

# tic_tac_toe (python)
def tic_tac_toe(board):
    size = len(board)

    # Check rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != "":
            return row[0]

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if all(cell == column[0] for cell in column) and column[0] != "":
            return column[0]

    # Check top-left to bottom-right diagonal
    if all(board[i][i] == board[0][0] for i in range(size)) and board[0][0] != "":
        return board[0][0]

    # Check top-right to bottom-left diagonal
    if all(board[i][size - 1 - i] == board[0][size - 1] for i in range(size)) and board[0][size - 1] != "":
        return board[0][size - 1]

    return "NO WINNER"

# eta (python)
def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), leg in route_map.items():
            if start == current_stop:
                total_time += leg["travel_time_mins"]
                current_stop = end
                break

    return total_time