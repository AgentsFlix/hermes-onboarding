#!/usr/bin/env python3
"""Validate public onboarding documentation without accessing a Hermes runtime."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = ["README.md", "PROMPT.md", "AGENTS.md", "CONTRIBUTING.md",
            "docs/identidade.md", "docs/integracoes.md", "docs/validacao.md"]
errors = []
for name in required:
    if not (root / name).is_file() or not (root / name).read_text().strip():
        errors.append(f"Arquivo obrigatório ausente ou vazio: {name}")
for path in root.rglob("*.md"):
    content = path.read_text()
    if content.count("```") % 2:
        errors.append(f"Bloco de código não fechado: {path.relative_to(root)}")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        local = target.split("#", 1)[0]
        if local and not (path.parent / local).exists():
            errors.append(f"Link local ausente: {path.relative_to(root)}: {target}")
for path in (root / "scripts").glob("*.py"):
    compile(path.read_text(), str(path), "exec")
for path in root.rglob("*"):
    if ".git" in path.parts or not path.is_file():
        continue
    if path.name.startswith(".env") or path.suffix in (".local", ".bak"):
        errors.append(f"Arquivo privado na árvore de entrega: {path.relative_to(root)}")
if errors:
    raise SystemExit("\n".join(errors))
print("Documentação, links locais e sintaxe Python: OK")
