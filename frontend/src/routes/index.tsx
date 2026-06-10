import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/alunos/DashboardAluno";
import MainLayout from "../layouts/MainLayout";

import Alunos from "../pages/alunos/Alunos";
import NovoAluno from "../pages/alunos/NovoAluno";
import type { JSX } from "react/jsx-runtime";

import DashboardSecretaria from "../pages/DashboardSecretaria";

function ProtectedRoute({ children }: { children: JSX.Element }) {
    const token = localStorage.getItem("token");

    if (!token) {
        return <Navigate to="/login" replace />;
    }

    return children;
}

export function AppRoutes() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />

            <Route
                element={
                    <ProtectedRoute>
                        <MainLayout />
                    </ProtectedRoute>
                }
            >
                <Route path="/" element={<Dashboard />} />
                <Route path="/alunos" element={<Alunos />} />
                <Route path="/alunos/novo" element={<NovoAluno />} />
                <Route path="/secretaria" element={<DashboardSecretaria />} />
            </Route>
        </Routes>
    );
}