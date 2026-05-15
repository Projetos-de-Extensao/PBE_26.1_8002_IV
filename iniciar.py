import subprocess
import os
import sys
import time
import webbrowser
import threading

# ─── Caminhos do projeto ───────────────────────────────────────────────────────
pasta_raiz    = os.path.dirname(os.path.abspath(__file__))
pasta_backend = os.path.join(pasta_raiz, "Back_end")
requirements  = os.path.join(pasta_backend, "requirements.txt")

# ─── 1. Instala dependências Python ────────────────────────────────────────────
print("=" * 50)
print("  Validação de Estágios — Iniciando...")
print("=" * 50)

print("\n[1/4] Instalando dependências Python...")
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", requirements],
    check=True
)

# ─── 2. Roda as migrations ─────────────────────────────────────────────────────
print("\n[2/4] Verificando alterações nos models...")
subprocess.run(
    [sys.executable, "manage.py", "makemigrations"],
    cwd=pasta_backend,
    check=True
)

print("\n[3/4] Aplicando migrations no banco de dados...")
subprocess.run(
    [sys.executable, "manage.py", "migrate"],
    cwd=pasta_backend,
    check=True
)

# ─── 3. Sobe o servidor Django ─────────────────────────────────────────────────
print("\n[4/4] Iniciando o servidor Django...")
servidor = subprocess.Popen(\
    [sys.executable, "manage.py", "runserver"],
    cwd=pasta_backend
)

# Aguarda o Django subir antes de abrir o navegador
time.sleep(2)

# Abre o painel admin no navegador
webbrowser.open("http://127.0.0.1:8000/api/")
print("\nServidor rodando em: http://127.0.0.1:8000")
print("API em:   http://127.0.0.1:8000/api/")
print("\nAperte Ctrl+C para encerrar.")

# ─── Aguarda o servidor e lida com encerramento ────────────────────────────────
def aguardar(proc, nome):
    proc.wait()
    print(f"\n{nome} encerrou.")

t = threading.Thread(target=aguardar, args=(servidor, "Backend"), daemon=True)
t.start()

try:
    t.join()
except KeyboardInterrupt:
    print("\nEncerrando o servidor...")
    servidor.terminate()