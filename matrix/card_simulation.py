"""
Simulation of card movement on a 2D grid

Description

Given an application that organizes information by arranging cards with notes on them into lists on a two-dimensional grid. These notes can be moved across multiple lists.

Examples include billboard-based task management applications such as Trello or Jira.

Image is bellow.
The first argument, cards, is given a value Indicating the initial position of all cards in the board, each as a two-dimensional array, with the following rules [CardID, RowIndex, ColumnIndex]

Here, the row and column indexes are assumed to be zero-based-Indexed.

The second argument, moves, is a two- dimensional array of values indicating the movement of the cards, each with the following futes

[Cardib, Row index before move, Column index before move,

Destination row index, Destination column index]

Here, the row and column indexes are zero- Based indexed and valid values (you don't have to assume that every index is not valid):

The third argument, query, is an int type value indicating the ID of the card to be moved.

Note that there are cases where moving one card will cause other cards to be moved.

Based on the given cards and moves, Implement a function that returns the final position of the card specified in the third argument, query, as [row index, column index).

Note that the following rules are assumed to exist for moving cards.

Note that the following rules are assumed to exist for moving cards.

• When a card is moved and if there is a card at the destination, the existing card is moved down one row.

• Also, when a card is moved, other cards in the original column move up one.

• Cards can be moved to the same row and column as before.

• There shall be no gaps in the initial placement.

• We can assume that the coordinates before a move is correct.

Example 1

cards=[[1,1,0], [3,0,0], [6,0,1], [4,0,2], [5,2,0], [7,1,1], [2,1,2]]
moves=[[6,0,1,2,0]]
query=6


Output: [2,0]

Example 2
cards = [[1, 1, 0], [3, 0, 0], [6, 0, 1], [4, 0, 2], [5, 2, 0], [7, 1, 1], [2, 1, 2]]
moves = [[6, 0, 1, 2, 0], [7, 0, 1, 0, 2]]
query = 2

OUTPUT: [2,2]
"""

from typing import Dict


def main(cards: list[list[int]], moves: list[list[int]], query: int) -> list[int, int]:
    card_positions: Dict[int, list[int, int]] = {}
    for card in cards:
        card_positions[card[0]] = [card[1], card[2]]

    def move(card_id: int, from_loc: list[int], to_loc: list[int]) -> None:
        card_positions[card_id] = []

        for cid, loc in card_positions.items():
            if not loc:
                continue

            curr_card_row, curr_card_col = loc
            from_row, from_col = from_loc
            if curr_card_col == from_col and from_row < curr_card_row:  # indicating col is same
                if to_loc[1] != curr_card_col:
                    move(cid, [curr_card_row, curr_card_col], [curr_card_row - 1, curr_card_col])
                else:
                    move(cid, [curr_card_row, curr_card_col], [curr_card_row + 1, curr_card_col])

        for cid, loc in card_positions.items():
            if not loc:
                continue

            curr_card_row, curr_card_col = loc
            to_row, to_col = to_loc

            if curr_card_row == to_row and curr_card_col == to_col:  # indicating row and col is same, thus push the item in that row in the next row
                move(cid, [curr_card_row, curr_card_col], [curr_card_row + 1, curr_card_col])

        card_positions[card_id] = to_loc

    for card_move in moves:
        card_id, from_row, from_col, to_row, to_col = card_move
        move(card_id, [from_row, from_col], [to_row, to_col])

    return card_positions[query]


if __name__ == "__main__":
    cards = [[1, 1, 0], [3, 0, 0], [6, 0, 1], [4, 0, 2], [5, 2, 0], [7, 1, 1], [2, 1, 2]]
    moves = [[6, 0, 1, 2, 0]]
    query = 6
    assert main(cards, moves, query) == [2, 0]

    cards = [[1, 1, 0], [3, 0, 0], [6, 0, 1], [4, 0, 2], [5, 2, 0], [7, 1, 1], [2, 1, 2]]
    moves = [[6, 0, 1, 2, 0], [7, 0, 1, 0, 2]]
    query = 2
    assert main(cards, moves, query) == [2, 2]
