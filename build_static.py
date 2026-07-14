import shutil
from pathlib import Path

from app import DIAS, render_dia, app

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

with app.test_request_context():
    for dia in DIAS:
        html = render_dia(dia)
        html = html.replace('href="/static/', 'href="static/').replace('src="/static/', 'src="static/')
        (DOCS / f"{dia['slug']}.html").write_text(html, encoding="utf-8")

shutil.copyfile(ROOT / "static" / "css" / "style.css", DOCS / "static" / "css" / "style.css")
shutil.copyfile(ROOT / "static" / "js" / "script.js", DOCS / "static" / "js" / "script.js")

print("Sitio estatico generado en docs/ (index.html y dia2.html)")
