import subprocess
import os
import sys
import webbrowser

# ─── Caminhos do projeto ───────────────────────────────────────────────────────
pasta_raiz = os.path.dirname(os.path.abspath(__file__))

pasta_backend = os.path.join(
    pasta_raiz,
    "Back_end"
)

requirements = os.path.join(
    pasta_backend,
    "requirements.txt"
)

# ─── Início ────────────────────────────────────────────────────────────────────
print("=" * 50)
print("  Validação de Estágios — Iniciando...")
print("=" * 50)

# ─── 1. Instalar dependências ──────────────────────────────────────────────────
print("\n[1/4] Instalando dependências Python...")

subprocess.run(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        requirements
    ],
    check=True
)

# ─── 2. Criar migrations ───────────────────────────────────────────────────────
print("\n[2/4] Verificando alterações nos models...")

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "makemigrations"
    ],
    cwd=pasta_backend,
    check=True
)

# ─── 3. Aplicar migrations ─────────────────────────────────────────────────────
print("\n[3/4] Aplicando migrations no banco de dados...")

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "migrate"
    ],
    cwd=pasta_backend,
    check=True
)

# ─── 4. Iniciar servidor Django ────────────────────────────────────────────────
print("\n[4/4] Iniciando o servidor Django...")

webbrowser.open(
    "http://127.0.0.1:8000/admin/"
)

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "runserver"
    ],
    cwd=pasta_backend
)