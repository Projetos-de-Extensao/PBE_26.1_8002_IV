import { Outlet, Link, useLocation, useNavigate } from "react-router-dom";
import { LayoutDashboard, FileText, Briefcase, ClipboardList, Users, Building, GraduationCap, LogOut } from "lucide-react";

// Definição dos dados dos menus de acordo com o HTML original
const roleMenuConfig = {
    aluno: {
    title: "Engenharia de Software",
    items: [
        {
            path: "/aluno",
            label: "Painel",
            icon: LayoutDashboard
        },
        {
            path: "/aluno/meus-tces",
            label: "Meus TCEs",
            icon: FileText,
            badge: 1
        },
        {
            path: "/aluno/estagio",
            label: "Meu Estágio",
            icon: Briefcase
        },
        {
            path: "/aluno/relatorios",
            label: "Relatórios",
            icon: ClipboardList,
            badge: 2
        }
        ]
    },
    secretaria: {
        title: "Secretaria · Unidade Barra",
        items: [
            { path: "/secretaria", label: "Painel", icon: LayoutDashboard },
            { path: "/secretaria/alunos", label: "Alunos", icon: Users },
            { path: "/secretaria/tces", label: "TCEs", icon: FileText, badge: 3 },
            { path: "/secretaria/empresas", label: "Empresas", icon: Building },
        ]
    },
    coordenador: {
        title: "Coordenador · Unidade Barra",
        items: [
            { path: "/coordenador", label: "Painel", icon: LayoutDashboard },
            { path: "/relatorios", label: "Relatórios", icon: ClipboardList, badge: 4 },
            { path: "/alunos", label: "Alunos", icon: Users },
            { path: "/coordenadores", label: "Coordenadores", icon: GraduationCap },
        ]
    }
};

const userMockData = {
    aluno: { name: 'João Silva', matricula: '202400012345', role: 'Aluno', className: 'role-aluno' },
    secretaria: { name: 'Maria Lima', matricula: '202100056789', role: 'Secretaria', className: 'role-secretaria' },
    coordenador: { name: 'Prof. Ribeiro', matricula: '201800034567', role: 'Coordenador', className: 'role-coordenador' }
};

export default function MainLayout() {
    const location = useLocation();
    const navigate = useNavigate();
    
    // Identifica o papel do usuário logado (padrão: aluno)
    const currentRole = (localStorage.getItem("userRole") || "aluno") as "aluno" | "secretaria" | "coordenador";
    
    const menuConfig = roleMenuConfig[currentRole] || roleMenuConfig.aluno;
    const userData = userMockData[currentRole] || userMockData.aluno;

    const handleLogout = () => {
        localStorage.clear(); // Limpa o token e a role do navegador
        navigate("/login");
    };

    return (
        <div className="flex min-h-screen bg-[var(--color-background-tertiary)] p-4">
            <div className="flex w-full flex-col md:flex-row bg-[var(--color-background-tertiary)] rounded-xl overflow-hidden border border-[var(--color-border-tertiary)] shadow-sm">
                
                {/* SIDEBAR */}
                <aside className="w-[var(--sidebar-w)] bg-[#1B3A5C] flex flex-col shrink-0 justify-between">
                    <div>
                        <div className="p-5 border-b border-white/10">
                            <h1 className="text-sm font-medium text-white tracking-wide">Val Estágio</h1>
                            <p className="text-[11px] text-white/50 mt-1">Sistema de gestão acadêmica</p>
                        </div>

                        <div className="p-4 flex items-center gap-3 border-b border-white/10">
                            <div className="w-8 h-8 rounded-full bg-[#2F7FBF] flex items-center justify-center text-xs font-medium text-white shrink-0">
                                {userData.name.split(" ").map(n => n[0]).join("").slice(0, 2)}
                            </div>
                            <div className="overflow-hidden">
                                <div className="text-xs font-medium text-white truncate">{userData.name}</div>
                                <div className="text-[10px] text-white/50 mt-[1px]">{userData.matricula}</div>
                                <span className={`role-badge ${userData.className}`}>{userData.role}</span>
                            </div>
                        </div>

                        <nav className="p-2 flex flex-col gap-1">
                            <div className="text-[9px] font-medium text-white/35 tracking-widest uppercase px-4 pt-2 pb-1">Menu</div>
                            {menuConfig.items.map((item, index) => {
                                const Icon = item.icon;
                                const isActive = location.pathname === item.path || (item.path !== "/" && location.pathname.startsWith(item.path));
                                return (
                                    <Link 
                                        key={index}
                                        to={item.path} 
                                        className={`flex items-center justify-between px-4 py-2 text-[13px] transition-colors border-l-3 ${isActive ? 'bg-[#2F7FBF]/25 text-white border-[#2F7FBF]' : 'text-white/65 border-transparent hover:bg-white/5 hover:text-white/90'}`}
                                    >
                                        <div className="flex items-center gap-2.5">
                                            <Icon size={16} />
                                            {item.label}
                                        </div>
                                        {item.badge && (
                                            <span className="bg-[#F5A623] text-[#7B4A00] text-[9px] font-medium px-1.5 py-0.5 rounded-full">{item.badge}</span>
                                        )}
                                    </Link>
                                );
                            })}
                        </nav>
                    </div>

                    {/* BOTÃO DE LOGOUT */}
                    <div className="p-2 border-t border-white/10">
                        <button 
                            onClick={handleLogout}
                            className="w-full flex items-center gap-2.5 px-4 py-2 text-[13px] text-white/65 hover:bg-white/5 hover:text-red-300 transition-colors rounded"
                        >
                            <LogOut size={16} />
                            Sair do Sistema
                        </button>
                    </div>
                </aside>

                {/* AREA DE CONTEÚDO */}
                <main className="flex-1 flex flex-col overflow-hidden bg-[var(--color-background-primary)]">
                    <header className="border-b border-[var(--color-border-tertiary)] p-4 px-6 flex items-center justify-between">
                        <div>
                            <h2 className="text-base font-medium text-[var(--color-text-primary)]">Painel de controle</h2>
                            <p className="text-xs text-[var(--color-text-secondary)] mt-0.5">{menuConfig.title}</p>
                        </div>
                        <div className="flex gap-2">
                            {currentRole === 'secretaria' && (
                                <button className="flex items-center gap-1.5 px-3.5 py-1.5 bg-[#1B3A5C] text-white rounded-md text-xs font-medium hover:bg-[#2F7FBF] transition-colors">
                                    Novo TCE ↗
                                </button>
                            )}
                            {currentRole === 'aluno' && (
                                <button className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-md text-xs font-medium border border-[var(--color-border-secondary)] hover:bg-[var(--color-background-secondary)] transition-colors">
                                    Ver relatórios ↗
                                </button>
                            )}
                            {currentRole === 'coordenador' && (
                                <button className="flex items-center gap-1.5 px-3.5 py-1.5 bg-[#1B3A5C] text-white rounded-md text-xs font-medium hover:bg-[#2F7FBF] transition-colors">
                                    Aprovar relatório ↗
                                </button>
                            )}
                        </div>
                    </header>

                    <div className="flex-1 overflow-y-auto p-6 bg-[var(--color-background-secondary)]">
                        <Outlet />
                    </div>
                </main>
            </div>
        </div>
    );
}