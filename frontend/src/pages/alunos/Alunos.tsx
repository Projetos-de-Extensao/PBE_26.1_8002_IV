import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function Alunos() {
    const [loading, setLoading] = useState(true);
    const [alunos, setAlunos] = useState<any[]>([]);

    useEffect(() => {
        carregarAlunos();
    }, []);

    async function carregarAlunos() {
        try {
            const response = await api.get("/alunos/");

            setAlunos(response.data.results || []);
        } catch (error) {
            console.error("Erro ao carregar alunos:", error);
        } finally {
            setLoading(false);
        }
    }

    if (loading) {
        return (
            <div className="bg-white p-6 rounded-lg shadow">
                Carregando alunos...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    Alunos
                </h1>

                <p className="text-gray-500 mt-1">
                    Lista de alunos cadastrados no sistema.
                </p>
            </div>

            <div className="bg-white rounded-lg shadow border overflow-hidden">

                <table className="w-full">

                    <thead className="bg-gray-100">
                        <tr>
                            <th className="text-left p-4">Usuário</th>
                            <th className="text-left p-4">Matrícula</th>
                            <th className="text-left p-4">Telefone</th>
                            <th className="text-left p-4">CPF</th>
                        </tr>
                    </thead>

                    <tbody>

                        {alunos.map((aluno) => (
                            <tr
                                key={aluno.usuario}
                                className="border-t hover:bg-gray-50"
                            >
                                <td className="p-4">
                                    {aluno.usuario_nome}
                                </td>

                                <td className="p-4">
                                    {aluno.matricula}
                                </td>

                                <td className="p-4">
                                    {aluno.telefone}
                                </td>

                                <td className="p-4">
                                    {aluno.cpf}
                                </td>
                            </tr>
                        ))}

                    </tbody>

                </table>

            </div>

        </div>
    );
}