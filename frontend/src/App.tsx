import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import MainLayout from "./layouts/MainLayout";
import DashboardAluno from "./pages/Dashboard"; 
import DashboardSecretaria from "./pages/DashboardSecretaria";
import RoleRedirect from "./components/RoleRedirect";


// Exemplo de dashboard vazio (para o coordenador que faremos depois)
const DashboardCoordenador = () => <div className="p-4">Painel do Coordenador</div>;

export default function App() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            
            <Route element={<MainLayout />}>
                <Route path="/" element={<RoleRedirect />} />
                
                <Route path="/aluno" element={<DashboardAluno />} />
                <Route path="/secretaria" element={<DashboardSecretaria />} /> {/* <-- Coloque o componente real aqui */}
                <Route path="/coordenador" element={<DashboardCoordenador />} />
            </Route>
        </Routes>
    );
}