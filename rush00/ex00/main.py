#!/usr/bin/env python3
from checkmate import is_in_check

def main():
    
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'K', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'P', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    
    result = is_in_check(board)
    print(result)

if __name__ == "__main__":
    main()