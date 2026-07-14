import shutil
from pathlib import Path

from flask import render_template

from app import DIAS, CLIENTE, render_dia, nav_para, app

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"


def limpiar_rutas(html):
    return html.replace('href="/static/', 'href="static/').replace('src="/static/', 'src="static/')


with app.test_request_context():
    for dia in DIAS:
        html = limpiar_rutas(render_dia(dia))
        (DOCS / f"{dia['slug']}.html").write_text(html, encoding="utf-8")

    html_progreso = limpiar_rutas(
        render_template("progreso.html", cliente=CLIENTE, nav=nav_para("progreso"))
    )
    (DOCS / "progreso.html").write_text(html_progreso, encoding="utf-8")

shutil.copyfile(ROOT / "static" / "css" / "style.css", DOCS / "static" / "css" / "style.css")
shutil.copyfile(ROOT / "static" / "js" / "script.js", DOCS / "static" / "js" / "script.js")
shutil.copyfile(ROOT / "static" / "js" / "progreso.js", DOCS / "static" / "js" / "progreso.js")

print("Sitio estatico generado en docs/ (index.html, dia2.html y progreso.html)")
