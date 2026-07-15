from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="mysql_principal",
        user="root",
        password="root",
        database="examenad",
        autocommit=True,
    )


@app.get("/datos")
def datos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT usuario, accion, fecha, hora, short FROM redes LIMIT 5")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({"servidor": "server2", "datos": [
            {"usuario": r[0], "accion": r[1], "fecha": r[2], "hora": r[3], "short": r[4]}
            for r in rows
        ]})
    except Error as exc:
        return jsonify({"error": str(exc)}), 500


@app.get("/metricas")
def metricas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT short, COUNT(*) AS views
            FROM redes
            WHERE accion = 'view'
            GROUP BY short
            ORDER BY views DESC, short DESC
            LIMIT 1
        """)
        video_mas_visto = cursor.fetchone()

        cursor.execute("""
            SELECT short, COUNT(*) AS likes
            FROM redes
            WHERE accion = 'like'
            GROUP BY short
            ORDER BY likes DESC, short DESC
            LIMIT 1
        """)
        video_mas_likes = cursor.fetchone()

        cursor.execute("""
            SELECT short, COUNT(*) AS comments
            FROM redes
            WHERE accion = 'comment'
            GROUP BY short
            ORDER BY comments DESC, short DESC
            LIMIT 1
        """)
        video_mas_comentado = cursor.fetchone()

        cursor.execute("""
            SELECT usuario, COUNT(*) AS total
            FROM redes
            GROUP BY usuario
            ORDER BY total DESC, usuario DESC
            LIMIT 1
        """)
        usuario_mas_recurrente = cursor.fetchone()

        cursor.execute("""
            SELECT hora, COUNT(*) AS total
            FROM redes
            GROUP BY hora
            ORDER BY total DESC, hora DESC
            LIMIT 1
        """)
        hora_mas_interaccion = cursor.fetchone()

        cursor.execute("""
            SELECT short,
                   SUM(CASE WHEN accion='like' THEN 1 ELSE 0 END) AS likes,
                   SUM(CASE WHEN accion='comment' THEN 1 ELSE 0 END) AS comments,
                   SUM(CASE WHEN accion='shared' THEN 1 ELSE 0 END) AS shares,
                   SUM(CASE WHEN accion='view' THEN 1 ELSE 0 END) AS views
            FROM redes
            GROUP BY short
            ORDER BY (likes + comments + shares) / NULLIF(views, 0) DESC, short DESC
            LIMIT 1
        """)
        video_ratio = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify({
            "servidor": "server2",
            "video_mas_visto": {"video": video_mas_visto[0] if video_mas_visto else None, "valor": video_mas_visto[1] if video_mas_visto else 0},
            "video_con_mas_likes": {"video": video_mas_likes[0] if video_mas_likes else None, "valor": video_mas_likes[1] if video_mas_likes else 0},
            "video_mas_comentado": {"video": video_mas_comentado[0] if video_mas_comentado else None, "valor": video_mas_comentado[1] if video_mas_comentado else 0},
            "usuario_mas_recurrente": {"usuario": usuario_mas_recurrente[0] if usuario_mas_recurrente else None, "valor": usuario_mas_recurrente[1] if usuario_mas_recurrente else 0},
            "hora_mas_interaccion": {"hora": hora_mas_interaccion[0] if hora_mas_interaccion else None, "valor": hora_mas_interaccion[1] if hora_mas_interaccion else 0},
            "video_mayor_ratio_interaccion": {"video": video_ratio[0] if video_ratio else None, "likes": video_ratio[1] if video_ratio else 0, "comments": video_ratio[2] if video_ratio else 0, "shares": video_ratio[3] if video_ratio else 0, "views": video_ratio[4] if video_ratio else 0}
        })
    except Error as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
