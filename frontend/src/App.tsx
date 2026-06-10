import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import MainLayout from "./layouts/MainLayout";
import DashboardAluno from "./pages/Dashboard"; // Aquele Dashboard que fizemos antes
import RoleRedirect from "./components/RoleRedirect";

// Exemplo de dashboards vazios (você vai criar eles depois)
const DashboardSecretaria = () => <div className="p-4">Painel da Secretaria</div>;
const DashboardCoordenador = () => <div className="p-4">Painel do Coordenador</div>;

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            
            {/* O MainLayout já tem a sua lógica de rotas protegidas por volta dele */}
            <Route element={<MainLayout />}>
                
                {/* Rota raiz: Verifica quem é o usuário e redireciona */}
                <Route path="/" element={<RoleRedirect />} />
                
                {/* Dashboards Específicos */}
                <Route path="/aluno" element={<DashboardAluno />} />
                <Route path="/secretaria" element={<DashboardSecretaria />} />
                <Route path="/coordenador" element={<DashboardCoordenador />} />
                
            </Route>
        </Routes>
    );
}