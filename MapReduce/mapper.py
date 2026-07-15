#!/usr/bin/env python3
import sys


def parse_line(line: str):
    line = line.strip()
    if not line:
        return None
    parts = [part.strip() for part in line.split(",")]
    if len(parts) != 5:
        return None
    usuario, accion, fecha, hora, short = parts
    return usuario, accion.lower(), fecha, hora, short


def main():
    for raw in sys.stdin:
        registro = parse_line(raw)
        if not registro:
            continue
        usuario, accion, fecha, hora, short = registro

        if accion == "view":
            print(f"video_view\t{short}\t1")
        elif accion == "like":
            print(f"video_like\t{short}\t1")
        elif accion == "comment":
            print(f"video_comment\t{short}\t1")
        elif accion == "shared":
            print(f"video_share\t{short}\t1")

        print(f"user\t{usuario}\t1")
        print(f"hour\t{hora}\t1")
        print(f"video_ratio\t{short}\t{accion}")


if __name__ == "__main__":
    main()
