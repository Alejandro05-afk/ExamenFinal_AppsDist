#!/usr/bin/env bash
set -euo pipefail

INPUT_FILE=${1:-"MapReduce/entrada.txt"}
OUTPUT_DIR=${2:-"MapReduce/splits"}

mkdir -p "$OUTPUT_DIR"
rm -f "$OUTPUT_DIR"/split_*.txt

if [ ! -f "$INPUT_FILE" ]; then
  echo "No se encontró el archivo de entrada: $INPUT_FILE" >&2
  exit 1
fi

split -n 4 "$INPUT_FILE" "$OUTPUT_DIR/split_"