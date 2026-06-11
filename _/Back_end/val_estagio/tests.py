from datetime import date

from django.test import TestCase

from .models import (
    Usuario,
    Curso,
    Aluno,
    Secretaria,
    Coordenador,
    Empresa,
    Tce,
    Estagio,
    RelatorioSemestral,
)
from .choices import StatusDocumento


class FluxoEstagioTests(TestCase):

    def setUp(self):

        self.curso = Curso.objects.create(
            nome="engenharia de software"
        )

        self.usuario_aluno = Usuario.objects.create(
            username="rafael",
            matricula="202502985045",
            unidade="barra"
        )

        self.aluno = Aluno.objects.create(
            usuario=self.usuario_aluno,
            telefone="+55219997520777",
            cpf="188.772.767-11",
            dt_nascimento=date(2000, 1, 1),
            procurando_estagio=True,
            horas_estagio=0,
            periodo=3,
            curso=self.curso
        )

        self.usuario_secretaria = Usuario.objects.create(
            username="secretaria",
            matricula="202502985046",
            unidade="barra"
        )

        self.secretaria = Secretaria.objects.create(
            usuario=self.usuario_secretaria
        )

        self.usuario_coordenador = Usuario.objects.create(
            username="coordenador",
            matricula="202502985047",
            unidade="barra"
        )

        self.coordenador = Coordenador.objects.create(
            usuario=self.usuario_coordenador,
            area="tecnologia"
        )

        self.empresa = Empresa.objects.create(
            nome="IBMEC",
            telefone="+55219997520777",
            cep="22775033",
            uf="RJ",
            cidade="Rio de Janeiro",
            log="Av Presidente Jose de Alencar",
            comp="",
            num="608",
            bairro="Jacarepagua",
            cnpj="16.153.078/2388-32"
        )

    def criar_tce(self):

        return Tce.objects.create(
            apoliceseguro="APOLICE001",
            bolsa=1000,
            secretaria=self.secretaria,
            aluno=self.aluno
        )

    def criar_estagio(self):

        tce = self.criar_tce()

        return Estagio.objects.create(
            dtinicio=date.today(),
            cargahorariasemanal=20,
            tce=tce,
            empresa=self.empresa
        )

    # ------------------------------------------------------------------
    # Criação de TCE
    # ------------------------------------------------------------------

    def test_criacao_tce(self):

        tce = self.criar_tce()

        self.assertEqual(
            tce.status,
            StatusDocumento.PENDENTE
        )

    # ------------------------------------------------------------------
    # Aprovação de TCE
    # ------------------------------------------------------------------

    def test_aprovacao_tce(self):

        tce = self.criar_tce()

        tce.se_aprovar()
        tce.refresh_from_db()

        self.assertEqual(
            tce.status,
            StatusDocumento.APROVADO
        )

    # ------------------------------------------------------------------
    # Aprovação de Relatório
    # ------------------------------------------------------------------

    def test_aprovacao_relatorio(self):

        estagio = self.criar_estagio()

        relatorio = RelatorioSemestral.objects.create(
            semestre="2025",
            data_envio=date.today(),
            horas_estagiadas=100,
            coordenador=self.coordenador,
            estagio=estagio
        )

        relatorio.se_aprovar()

        relatorio.refresh_from_db()
        self.aluno.refresh_from_db()

        self.assertEqual(
            relatorio.status,
            StatusDocumento.APROVADO
        )

        self.assertEqual(
            self.aluno.horas_estagio,
            100
        )

    # ------------------------------------------------------------------
    # Reprovação de Relatório
    # ------------------------------------------------------------------

    def test_reprovacao_relatorio(self):

        estagio = self.criar_estagio()

        relatorio = RelatorioSemestral.objects.create(
            semestre="2026",
            data_envio=date.today(),
            horas_estagiadas=100,
            coordenador=self.coordenador,
            estagio=estagio
        )

        relatorio.se_reprovar()

        relatorio.refresh_from_db()

        self.assertEqual(
            relatorio.status,
            StatusDocumento.REPROVADO
        )

    # ------------------------------------------------------------------
    # Atualização de horas
    # ------------------------------------------------------------------

    def test_ganhar_horas_estagio(self):

        self.aluno.ganhar_horas_estagio(50)

        self.aluno.refresh_from_db()

        self.assertEqual(
            self.aluno.horas_estagio,
            50
        )

    # ------------------------------------------------------------------
    # Limite de 350 horas
    # ------------------------------------------------------------------

    def test_limite_maximo_350_horas(self):

        self.aluno.ganhar_horas_estagio(400)

        self.aluno.refresh_from_db()

        self.assertEqual(
            self.aluno.horas_estagio,
            350
        )
