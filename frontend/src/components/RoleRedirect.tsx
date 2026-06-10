import { Navigate } from "react-router-dom";

export default function RoleRedirect() {
    // Pega a role que salvamos no localStorage durante o login
    const role = localStorage.getItem("userRole");

    // Redireciona para a rota correta
    if (role === "secretaria") {
        return <Navigate to="/secretaria" replace />;
    } else if (role === "coordenador") {
        return <Navigate to="/coordenador" replace />;
    }
    
    // Se for aluno ou se não tiver role definida, vai pro aluno
    return <Navigate to="/aluno" replace />;
}