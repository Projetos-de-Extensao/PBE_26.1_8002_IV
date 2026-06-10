from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
import hashlib
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validar_cpf, validar_cnpj, validar_matricula, validar_cep, validar_periodo, validar_positivo, validar_semestre
from .choices import StatusDocumento, UNIDADE_CHOICES, AREA_CHOICES, CURSOS_CHOICES


# --- USUÁRIOS E PERFIS (Herança e Relacionamentos) ---

class Usuario(AbstractUser): # --- Classe usuário ---
    # Extensão do User do Django: adicionamos matrícula e unidade
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, verbose_name="Unidade")
    matricula = models.CharField(max_length=12, primary_key=True, verbose_name="Matrícula", validators=[validar_matricula])
    
    def __str__(self):
        return f"{self.username} - Matrícula: {self.matricula} ({self.unidade})"

class Aluno(models.Model): # OneToOne vincula o perfil de Aluno ao Usuario
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula', verbose_name="Matrícula")
    telefone = PhoneNumberField(region='BR', verbose_name="Telefone")
    cpf =  EncryptedCharField(max_length=14, validators=[validar_cpf], verbose_name="CPF")
    cpf_hash = models.CharField(max_length=64,null=True,blank=True,editable=False)
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")
    procurando_estagio = models.BooleanField(default=False, verbose_name="Procurando Estágio")
    horas_estagio = models.IntegerField(default=0, verbose_name="Horas de Estágio")
    periodo = models.PositiveIntegerField(verbose_name="Período", validators=[validar_periodo])
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, db_column='id_curso', verbose_name="Curso")

 # Gera o hash do CPF para garantir unicidade sem expor o valor real
    def save(self, *args, **kwargs):

        cpf_limpo = (
            self.cpf
            .replace('.', '')
            .replace('-', '')
        )

        self.cpf_hash = hashlib.sha256(
            cpf_limpo.encode('utf-8')
        ).hexdigest()

        super().save(*args, **kwargs)
    
# Lógica de negócio: atualiza horas, limitando ao teto de 350

    def ganhar_horas_estagio(self, horas_estagiadas):
        if(horas_estagiadas > 0 and self.horas_estagio < 350):
            self.horas_estagio = min(self.horas_estagio + horas_estagiadas, 350)
        self.save()

    def __str__(self):
        return f"{self.usuario.username} - Matrícula: {self.usuario.matricula} | Curso: {self.curso.nome}"
    
     # --- Classe Secretaria ---
    
class Secretaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula')

    def aprovar_tce(self, tce):
        tce.se_aprovar()

    def reprovar_tce(self, tce):
        tce.se_reprovar()

    def __str__(self):
        return f"{self.usuario.username} - Matrícula: {self.usuario.matricula} | Secretaria"
    
     # --- Classe Coordenador ---

class Coordenador(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    area = models.CharField(max_length=100, choices=AREA_CHOICES, verbose_name="Área")

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def aprovar_relatorio(self, relatorioSemestral):
        relatorioSemestral.se_aprovar()

    def reprovar_relatorio(self, relatorioSemestral):
        relatorioSemestral.se_reprovar()

    def __str__(self):
        return f"{self.usuario.username} - Matrícula: {self.usuario.matricula} | Área: {self.area}"
    
    # --- ENTIDADES E NEGÓCIOS ---

# --- Classe Curso ---
class Curso(models.Model):
    
    nome = models.CharField(max_length=100, choices=CURSOS_CHOICES, unique=True, verbose_name="Nome do Curso")

    def __str__(self):
        return f"Curso: {self.nome}"


# --- Classe Empresa ---
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome da Empresa")
    telefone = PhoneNumberField(region='BR', verbose_name="Telefone")
    cep = models.CharField(max_length=9, verbose_name="CEP", validators=[validar_cep])
    uf = models.CharField(max_length=2, verbose_name="UF")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    log = models.CharField(max_length=255, verbose_name="Logradouro")
    comp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Complemento")
    num = models.CharField(max_length=20, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cnpj =  EncryptedCharField(max_length=18, validators=[validar_cnpj], verbose_name="CNPJ")
    cnpj_hash = models.CharField(max_length=64,null=True,blank=True,editable=False)

    def save(self, *args, **kwargs):

        cnpj_limpo = (
        self.cnpj
        .replace('.', '')
        .replace('/', '')
        .replace('-', '')
        )

        self.cnpj_hash = hashlib.sha256(
        cnpj_limpo.encode('utf-8')
        ).hexdigest()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - CNPJ: {self.cnpj} | {self.cidade}/{self.uf}"
    
# --- DOCUMENTAÇÃO E FLUXO DE ESTÁGIO ---


    # --- Classe TCE ---
class Tce(models.Model):
    status = models.CharField(max_length=20, choices=StatusDocumento.choices, default=StatusDocumento.PENDENTE, verbose_name="Status do TCE")
    apoliceseguro = models.CharField(max_length=50, primary_key=True, verbose_name="Apólice de Seguro",)
    bolsa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Bolsa", validators=[validar_positivo])
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT, db_column='matricula_secretaria', verbose_name="Secretaria")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='matricula_aluno', verbose_name="Aluno")

    def se_aprovar(self):
        self.status = StatusDocumento.APROVADO
        self.save()

    def se_reprovar(self):
        self.status = StatusDocumento.REPROVADO
        self.save()
    

    def __str__(self):
        return f"TCE: {self.apoliceseguro} | Aluno: {self.aluno.usuario.username} | Status: {self.status}"
    

    # --- Classe Estágio ---
class Estagio(models.Model):
    idestagio = models.AutoField(primary_key=True)
    dtinicio = models.DateField(verbose_name="Data de Início")
    dtfim = models.DateField(null=True, blank=True, verbose_name="Data de Término")
    cargahorariasemanal = models.IntegerField(verbose_name="Carga Horária Semanal")
    tce = models.ForeignKey(Tce, on_delete=models.PROTECT, db_column='apolice_seguro', verbose_name="TCE")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa")

    # models.py — Estagio
    def clean(self):
        if self.dtfim and self.dtfim < self.dtinicio:
            raise ValidationError(
                {'dtfim': 'A data de término não pode ser anterior à data de início.'}
            )

    def adicionar_relatorio(self, coordenador, semestre, horas_estagiadas, data_envio):

        from .models import RelatorioSemestral 

        novo_relatorio = RelatorioSemestral.objects.create(
            estagio=self,
            coordenador=coordenador,
            semestre=semestre,
            horas_estagiadas=horas_estagiadas,
            data_envio=data_envio
        )
        return novo_relatorio


    def __str__(self):
        dtfim_str = self.dtfim.strftime('%d/%m/%Y') if self.dtfim else 'em andamento'
        return f"Estágio: {self.tce.aluno.usuario.username} | Empresa: {self.empresa.nome} | {self.dtinicio.strftime('%d/%m/%Y')} → {dtfim_str}"

# --- Classe Relatório Semestral ---
class RelatorioSemestral(models.Model):
    status = models.CharField(max_length=20, choices=StatusDocumento.choices, default=StatusDocumento.PENDENTE, verbose_name="Status do Relatório")
    idrelatorio = models.AutoField(primary_key=True)
    data_envio = models.DateField(verbose_name="Data de Envio")
    semestre = models.CharField(max_length=4, validators=[validar_semestre], verbose_name="Semestre")
    horas_estagiadas = models.PositiveIntegerField(verbose_name="Horas Estagiadas", validators=[validar_positivo])
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, db_column='matricula_coordenador', verbose_name="Coordenador")
    estagio = models.ForeignKey(Estagio, on_delete=models.CASCADE, db_column='id_estagio', verbose_name="Estágio")

    def se_aprovar(self):
        if(self.status != StatusDocumento.APROVADO):
            self.status = StatusDocumento.APROVADO

            aluno_deste_relatorio = self.estagio.tce.aluno
            aluno_deste_relatorio.ganhar_horas_estagio(self.horas_estagiadas)
            
            self.save()

    def se_reprovar(self):
        self.status = StatusDocumento.REPROVADO
        self.save()


    class Meta:
        verbose_name = "Relatório Semestral"
        verbose_name_plural = "Relatórios Semestrais"
        unique_together = ['estagio', 'semestre']

    def __str__(self):
        return f"Relatório {self.semestre} | Aluno: {self.estagio.tce.aluno.usuario.username} | Status: {self.status}"