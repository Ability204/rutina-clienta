import shutil
from pathlib import Path

from app import RUTINA, con_imagenes, app

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

with app.test_request_context():
    from flask import render_template

    html = render_template(
        "index.html",
        rutina=con_imagenes(RUTINA),
        cliente="Sofía Gómez",
        frase="Cada repetición de hoy es un paso hacia la versión más fuerte de ti misma.",
    )

html = html.replace('href="/static/', 'href="static/').replace('src="/static/', 'src="static/')

(DOCS / "index.html").write_text(html, encoding="utf-8")

shutil.copyfile(ROOT / "static" / "css" / "style.css", DOCS / "static" / "css" / "style.css")
shutil.copyfile(ROOT / "static" / "js" / "script.js", DOCS / "static" / "js" / "script.js")

print("Sitio estatico generado en docs/")
