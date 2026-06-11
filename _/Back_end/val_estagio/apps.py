from django.apps import AppConfig

# Classe de configuração do aplicativo.
# O Django utiliza esta classe para identificar e carregar o seu app 'val_estagio' durante a inicialização do sistema.
class ValEstagioConfig(AppConfig):
    # 'name' define o caminho completo do pacote Python que contém o aplicativo. É obrigatório que este nome corresponda ao nome da pasta do seu app.
    name = 'val_estagio'