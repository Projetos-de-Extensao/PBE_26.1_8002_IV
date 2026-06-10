import { api } from "./axios";

export async function listarAlunos() {
    const response = await api.get("/alunos/");
    return response.data;
}

export async function criarAluno(dados: any) {
    const response = await api.post("/alunos/", dados);
    return response.data;
}