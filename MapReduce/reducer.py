#!/usr/bin/env python3
import sys
from collections import defaultdict

video_views = defaultdict(int)
video_likes = defaultdict(int)
video_comments = defaultdict(int)
video_shares = defaultdict(int)
user_counts = defaultdict(int)
hour_counts = defaultdict(int)
video_metrics = defaultdict(lambda: {"view": 0, "like": 0, "comment": 0, "share": 0})


def main():
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        key_type, key, value = parts
        if key_type == "video_view":
            video_views[key] += int(value)
            video_metrics[key]["view"] += int(value)
        elif key_type == "video_like":
            video_likes[key] += int(value)
            video_metrics[key]["like"] += int(value)
        elif key_type == "video_comment":
            video_comments[key] += int(value)
            video_metrics[key]["comment"] += int(value)
        elif key_type == "video_share":
            video_shares[key] += int(value)
            video_metrics[key]["share"] += int(value)
        elif key_type == "user":
            user_counts[key] += int(value)
        elif key_type == "hour":
            hour_counts[key] += int(value)
        elif key_type == "video_ratio":
            action = value
            if action == "shared":
                action = "share"
            if action in video_metrics[key]:
                video_metrics[key][action] += 1

    video_mas_visto = max(video_views.items(), key=lambda item: (item[1], item[0]), default=(None, 0))
    video_con_mas_likes = max(video_likes.items(), key=lambda item: (item[1], item[0]), default=(None, 0))
    video_mas_comentado = max(video_comments.items(), key=lambda item: (item[1], item[0]), default=(None, 0))
    usuario_mas_recurrente = max(user_counts.items(), key=lambda item: (item[1], item[0]), default=(None, 0))
    hora_mas_interaccion = max(hour_counts.items(), key=lambda item: (item[1], item[0]), default=(None, 0))

    def ratio(item):
        video, counts = item
        total = counts["like"] + counts["comment"] + counts["share"]
        views = counts["view"]
        if views == 0:
            return 0
        return total / views

    video_ratio = max(video_metrics.items(), key=lambda item: (ratio(item), item[0]), default=(None, {"view": 0, "like": 0, "comment": 0, "share": 0}))

    print("RESULTADOS_MAP_REDUCE")
    print(f"video_mas_visto\t{video_mas_visto[0]}\t{video_mas_visto[1]}")
    print(f"video_con_mas_likes\t{video_con_mas_likes[0]}\t{video_con_mas_likes[1]}")
    print(f"video_mas_comentado\t{video_mas_comentado[0]}\t{video_mas_comentado[1]}")
    print(f"usuario_mas_recurrente\t{usuario_mas_recurrente[0]}\t{usuario_mas_recurrente[1]}")
    print(f"hora_mas_interaccion\t{hora_mas_interaccion[0]}\t{hora_mas_interaccion[1]}")
    print(f"video_mayor_ratio_interaccion\t{video_ratio[0]}\t{ratio(video_ratio)}")


if __name__ == "__main__":
    main()
