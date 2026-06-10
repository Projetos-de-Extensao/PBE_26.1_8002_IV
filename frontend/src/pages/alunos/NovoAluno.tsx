import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { criarAluno } from "../../api/alunos";

export default function NovoAluno() {
    const navigate = useNavigate();

    const [matricula, setMatricula] = useState("");
    const [telefone, setTelefone] = useState("");

    const [erro, setErro] = useState("");

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        setErro("");

        try {
            await criarAluno({
                matricula,
                telefone,
            });

            navigate("/alunos");
        } catch {
            setErro("Erro ao cadastrar aluno.");
        }
    }

    return (
        <div>
            <h1>Novo Aluno</h1>

            {erro && <p>{erro}</p>}

            <form onSubmit={handleSubmit}>
                <div>
                    <label>Matrícula</label>

                    <input
                        value={matricula}
                        onChange={(e) => setMatricula(e.target.value)}
                    />
                </div>

                <br />

                <div>
                    <label>Telefone</label>

                    <input
                        value={telefone}
                        onChange={(e) => setTelefone(e.target.value)}
                    />
                </div>

                <br />

                <button type="submit">
                    Salvar
                </button>
            </form>
        </div>
    );
}