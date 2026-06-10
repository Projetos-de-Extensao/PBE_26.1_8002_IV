import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

import MainLayout from "./layouts/MainLayout";

import DashboardAluno from "./pages/alunos/DashboardAluno";
import MeusTces from "./pages/alunos/MeusTces";
import MeuEstagio from "./pages/alunos/MeuEstagio";
import RelatoriosAluno from "./pages/alunos/RelatoriosAluno";

import DashboardSecretaria from "./pages/DashboardSecretaria";

import RoleRedirect from "./components/RoleRedirect";
import ProtectedRoute from "./components/ProtectedRoute";

const DashboardCoordenador = () => (
    <div className="p-4">
        Painel do Coordenador
    </div>
);

export default function App() {
    return (
        <Routes>

            <Route
                path="/login"
                element={<Login />}
            />

            <Route
                element={<MainLayout />}
            >
                <Route
                    path="/"
                    element={<RoleRedirect />}
                />

                {/* ALUNO */}

                <Route
                    path="/aluno"
                    element={
                        <ProtectedRoute>
                            <DashboardAluno />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/aluno/meus-tces"
                    element={
                        <ProtectedRoute>
                            <MeusTces />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/aluno/estagio"
                    element={
                        <ProtectedRoute>
                            <MeuEstagio />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/aluno/relatorios"
                    element={
                        <ProtectedRoute>
                            <RelatoriosAluno />
                        </ProtectedRoute>
                    }
                />

                {/* SECRETARIA */}

                <Route
                    path="/secretaria"
                    element={
                        <ProtectedRoute>
                            <DashboardSecretaria />
                        </ProtectedRoute>
                    }
                />

                {/* COORDENADOR */}

                <Route
                    path="/coordenador"
                    element={
                        <ProtectedRoute>
                            <DashboardCoordenador />
                        </ProtectedRoute>
                    }
                />
            </Route>

        </Routes>
    );
}