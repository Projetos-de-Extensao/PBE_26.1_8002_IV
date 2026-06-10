import { useEffect, useState } from "react";

import { listarAlunos } from "../../api/alunos";
import { useNavigate } from "react-router-dom";

export default function Alunos() {
    const navigate = useNavigate();

    const [alunos, setAlunos] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);


    useEffect(() => {
        async function carregar() {
            try {
                const dados = await listarAlunos();

                setAlunos(dados.results);
            } finally {
                setLoading(false);
            }
        }

        carregar();
    }, []);

    if (loading) {
        return <p>Carregando...</p>;
    }

    return (
        <div>
            <h1>Alunos</h1>

            <button onClick={() => navigate("/alunos/novo")}>
                Novo aluno
            </button>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Matrícula</th>
                        <th>Telefone</th>
                        <th>Ações</th>
                    </tr>
                </thead>

                <tbody>
                    {alunos.map((aluno) => (
                        <tr key={aluno.id}>
                            <td>{aluno.id}</td>
                            <td>{aluno.matricula}</td>
                            <td>{aluno.telefone}</td>

                            <td>
                                <button>Editar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}