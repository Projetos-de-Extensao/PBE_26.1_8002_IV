import { Link, Outlet, useNavigate } from "react-router-dom";
import { logout } from "../api/auth";

export default function MainLayout() {
    const navigate = useNavigate();

    function handleLogout() {
        logout();               // remove o token
        navigate("/login");     // vai para a tela de login
    }

    return (
        <div style={{ display: "flex", minHeight: "100vh" }}>
            <aside
                style={{
                    width: "240px",
                    padding: "1rem",
                    borderRight: "1px solid #ddd",
                }}
            >
                <h2>Sistema de Estágios</h2>

                <nav>
                    <ul style={{ listStyle: "none", padding: 0 }}>
                        <li><Link to="/">Dashboard</Link></li>
                        <li><Link to="/alunos">Alunos</Link></li>
                        <li><Link to="/empresas">Empresas</Link></li>
                    </ul>
                </nav>

                <button
                    onClick={handleLogout}
                    style={{ marginTop: "2rem" }}
                >
                    Sair
                </button>
            </aside>

            <main style={{ flex: 1, padding: "2rem" }}>
                <Outlet />
            </main>
        </div>
    );
}