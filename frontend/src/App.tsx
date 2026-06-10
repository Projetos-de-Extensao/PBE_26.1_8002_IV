import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import MainLayout from "./layouts/MainLayout";
import DashboardAluno from "./pages/Dashboard";
import RoleRedirect from "./components/RoleRedirect";

// Exemplo de dashboards vazios
const DashboardSecretaria = () => <div className="p-4">Painel da Secretaria</div>;
const DashboardCoordenador = () => <div className="p-4">Painel do Coordenador</div>;

export default function App() {
    return (
        <Routes>
            {/* Rota de Login */}
            <Route path="/login" element={<Login />} />
            
            {/* Rotas protegidas dentro do Layout Principal */}
            <Route element={<MainLayout />}>
                
                {/* Rota raiz: Verifica quem é o utilizador e redireciona */}
                <Route path="/" element={<RoleRedirect />} />
                
                {/* Dashboards Específicos */}
                <Route path="/aluno" element={<DashboardAluno />} />
                <Route path="/secretaria" element={<DashboardSecretaria />} />
                <Route path="/coordenador" element={<DashboardCoordenador />} />
                
            </Route>
        </Routes>
    );
}