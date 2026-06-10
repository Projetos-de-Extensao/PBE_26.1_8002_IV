import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../api/auth";

export default function Login() {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [erro, setErro] = useState("");

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        setErro("");

        try {
            const data = await login(username, password);

            localStorage.setItem("token", data.token);

            navigate("/");
        } catch {
            setErro("Usuário ou senha inválidos.");
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>Entrar</h1>

            {erro && <p>{erro}</p>}

            <input
                placeholder="Usuário"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />

            <br /><br />

            <input
                type="password"
                placeholder="Senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <br /><br />

            <button type="submit">
                Entrar
            </button>
        </form>
    );
}