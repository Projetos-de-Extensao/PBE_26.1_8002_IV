import subprocess
import os
import sys
import webbrowser
import time

# ─── Caminhos ────────────────────────────────────────────────────────────────
pasta_raiz = os.path.dirname(os.path.abspath(__file__))

pasta_backend = os.path.join(
    pasta_raiz,
    "Back_end"
)

requirements = os.path.join(
    pasta_backend,
    "requirements.txt"
)

# ─── Início ──────────────────────────────────────────────────────────────────
print("=" * 50)
print("  Validação de Estágios — Iniciando...")
print("=" * 50)

# ─── Instala dependências ────────────────────────────────────────────────────
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

# ─── Migrations ──────────────────────────────────────────────────────────────
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

print("\n[3/4] Aplicando migrations...")

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "migrate"
    ],
    cwd=pasta_backend,
    check=True
)

# ─── Inicia servidor ─────────────────────────────────────────────────────────
print("\n[4/4] Iniciando servidor Django...")

servidor = subprocess.Popen(
    [
        sys.executable,
        "manage.py",
        "runserver"
    ],
    cwd=pasta_backend
)

# Espera servidor subir
time.sleep(2)

# ─── Abre navegador ──────────────────────────────────────────────────────────
webbrowser.open(
    "http://127.0.0.1:8000/admin/"
)

print("\nServidor rodando:")
print("http://127.0.0.1:8000")

print("\nAPI:")
print("http://127.0.0.1:8000/api/")

print("\nAdmin:")
print("http://127.0.0.1:8000/admin/")