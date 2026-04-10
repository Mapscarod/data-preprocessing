# Ranking Data Organizer

This project processes a text file containing institutional ranking data and organizes it by group.

## What it does

- Reads a ranking dataset from a `.txt` file
- Splits the data by group code
- Creates a separate file for each group
- Generates an index file with summary information

## Input format

Each line in the input file must follow:

GroupCode | RankingPosition | InstitutionName | Score

## Output

- One file per group inside organized folders
- An index file summarizing all groups

## Usage
