import { Navigate } from "react-router-dom";

export default function RoleRedirect() {
    const token = localStorage.getItem("token");
    const role = localStorage.getItem("userRole");

    // Se não estiver autenticado, vai para o login
    if (!token) {
        return <Navigate to="/login" replace />;
    }

    // Redireciona conforme a role salva
    if (role === "secretaria") {
        return <Navigate to="/secretaria" replace />;
    }

    if (role === "coordenador") {
        return <Navigate to="/coordenador" replace />;
    }

    // Aluno é o padrão
    return <Navigate to="/aluno" replace />;
}