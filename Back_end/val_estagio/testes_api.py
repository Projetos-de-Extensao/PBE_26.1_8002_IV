from datetime import date

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import (
    Usuario,
    Curso,
    Aluno,
    Secretaria,
)
"""
Testes de integração da API.

Cobertura:
- Controle de acesso
- Autenticação
- Autorização por perfil
- Busca de alunos (RF10)

Objetivo:
Garantir que usuários só consigam acessar
os recursos permitidos para seu perfil.
"""

class SegurancaAlunoApiTests(APITestCase):

    def setUp(self):

        self.curso = Curso.objects.create(
            nome="engenharia de software"
        )

        # -------------------------
        # Aluno A
        # -------------------------

        self.usuario_a = Usuario.objects.create_user(
            username="rafael",
            password="123456",
            matricula="202502985045",
            unidade="barra"
        )

        self.aluno_a = Aluno.objects.create(
            usuario=self.usuario_a,
            telefone="+55219999999999",
            cpf="188.772.767-11",
            dt_nascimento=date(2000, 1, 1),
            periodo=3,
            curso=self.curso
        )

        # -------------------------
        # Aluno B
        # -------------------------

        self.usuario_b = Usuario.objects.create_user(
            username="carlos",
            password="123456",
            matricula="202502985046",
            unidade="barra"
        )

        self.aluno_b = Aluno.objects.create(
            usuario=self.usuario_b,
            telefone="+55218888888888",
            cpf="111.111.111-11",
            dt_nascimento=date(2000, 1, 1),
            periodo=3,
            curso=self.curso
        )

        # -------------------------
        # Secretaria
        # -------------------------

        self.usuario_secretaria = Usuario.objects.create_user(
            username="secretaria",
            password="123456",
            matricula="202502985047",
            unidade="barra"
        )

        self.secretaria = Secretaria.objects.create(
            usuario=self.usuario_secretaria
        )

        self.token_aluno = Token.objects.create(
            user=self.usuario_a
        )

        self.token_secretaria = Token.objects.create(
            user=self.usuario_secretaria
        )

    # ==================================================
    # Aluno não enxerga outro aluno
    # ==================================================

    def test_aluno_nao_enxerga_outro_aluno(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token_aluno.key}"
        )

        response = self.client.get(
            f"/api/alunos/{self.aluno_b.pk}/"
        )

        self.assertIn(
            response.status_code,
            [403, 404]
        )

    # ==================================================
    # Secretaria enxerga qualquer aluno
    # ==================================================

    def test_secretaria_enxerga_qualquer_aluno(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token_secretaria.key}"
        )

        response = self.client.get(
            f"/api/alunos/{self.aluno_a.pk}/"
        )

        self.assertEqual(
            response.status_code,
            200
        )

    # ==================================================
    # RF10 Busca por matrícula
    # ==================================================

    def test_busca_aluno_por_matricula(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token_secretaria.key}"
        )

        response = self.client.get(
            "/api/alunos/?search=202502985045"
        )

        self.assertEqual(
            response.status_code,
            200
        )

    # ==================================================
    # Usuário anônimo não acessa alunos
    # ==================================================

    def test_anonimo_nao_acessa_alunos(self):

        response = self.client.get(
            "/api/alunos/"
        )

        self.assertIn(
            response.status_code,
            [401, 403]
        )

    # ==================================================
    # Aluno não pode listar todos os alunos
    # ==================================================

    def test_aluno_nao_lista_alunos(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token_aluno.key}"
        )

        response = self.client.get(
            "/api/alunos/"
        )

        self.assertEqual(
            response.status_code,
            403
        )