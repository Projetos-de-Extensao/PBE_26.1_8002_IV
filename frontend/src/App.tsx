import { Routes, Route } from "react-router-dom";

import Login from "./pages/login/Login";

import MainLayout from "./layouts/MainLayout";

import DashboardAluno from "./pages/alunos/DashboardAluno";
import MeusTces from "./pages/alunos/MeusTces";
import MeuEstagio from "./pages/alunos/MeuEstagio";
import RelatoriosAluno from "./pages/alunos/RelatoriosAluno";
import Alunos from "./pages/alunos/Alunos";

import DashboardSecretaria from "./pages/secretarias/DashboardSecretaria";
import Empresas from "./pages/secretarias/Empresas";
import TcesSecretaria from "./pages/secretarias/TcesSecretaria";

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
                <Route
                path="/secretaria/tces"
                element={
                    <ProtectedRoute>
                         <TcesSecretaria />
                    </ProtectedRoute>
                }
            />
                <Route
                path="/secretaria/alunos"
                element={
                <ProtectedRoute>
                    <Alunos />
                </ProtectedRoute>
         }
                />
                <Route
                path="/secretaria/empresas"
                element={
                <ProtectedRoute>
                    <Empresas />
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