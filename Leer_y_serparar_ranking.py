"""
Program: Ranking Data Organizer

Description:
This script reads a text file containing institutional ranking data,
where each line follows the format:
    GroupCode | RankingPosition | InstitutionName | Score

The script processes the data and:
- Groups entries by their group code
- Creates a separate output file for each group
- Writes corresponding records into each group file
- Generates an index file summarizing each group, including:
    * Group code
    * Last institution processed
    * Ranking position
    * Output file path
    * Number of records per group
"""

import os
from pathlib import Path

def process_ranking(input_file, output_dir, index_file):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    current_group = None
    group_file = None
    count = 0

    with open(input_file, "r", encoding="utf-8") as f, \
         open(index_file, "w", encoding="utf-8") as index:

        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) < 4 or parts[0] == "Grupo":
                continue

            codigo, posicion, nombre, puntuacion = parts
            nombre = nombre.upper()

            # Cambio de grupo
            if codigo != current_group:
                if group_file:
                    group_file.close()
                    index.write(f"{current_group}|{last_nombre}|{last_pos}|{last_path}|{count}|\n")

                folder = output_dir / f"Ranking_Grupo_{codigo}"
                folder.mkdir(exist_ok=True)

                file_path = folder / f"Grupo_{codigo}.txt"
                group_file = open(file_path, "w", encoding="utf-8")

                current_group = codigo
                count = 0
                last_path = str(file_path)

            group_file.write(line + "\n")

            last_nombre = nombre
            last_pos = posicion
            count += 1

        # último grupo
        if group_file:
            group_file.close()
            index.write(f"{current_group}|{last_nombre}|{last_pos}|{last_path}|{count}|\n")


# Uso
process_ranking(
    input_file="Ingenieria2014.txt",
    output_dir="RankingInstituciones",
    index_file="indiceRankingIngenieria.txt"
)