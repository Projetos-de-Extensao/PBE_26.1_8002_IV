import { Outlet, Link, useLocation } from "react-router-dom";
import { LayoutDashboard, FileText, Briefcase, ClipboardList } from "lucide-react";

export default function MainLayout() {
    const location = useLocation();

    // Simulando os dados do usuário (no futuro virá do seu contexto de Auth)
    const user = {
        name: "João Silva",
        matricula: "202400012345",
        role: "Aluno",
        roleClass: "role-aluno"
    };

    return (
        <div className="flex min-h-screen bg-[var(--color-background-tertiary)] p-4">
            <div className="flex w-full flex-col md:flex-row bg-[var(--color-background-tertiary)] rounded-xl overflow-hidden border border-[var(--color-border-tertiary)] shadow-sm">
                
                {/* SIDEBAR */}
                <aside className="w-[var(--sidebar-w)] bg-[#1B3A5C] flex flex-col shrink-0">
                    <div className="p-5 border-b border-white/10">
                        <h1 className="text-sm font-medium text-white tracking-wide">Val Estágio</h1>
                        <p className="text-[11px] text-white/50 mt-1">Sistema de gestão acadêmica</p>
                    </div>

                    <div className="p-4 flex items-center gap-3 border-b border-white/10">
                        <div className="w-8 h-8 rounded-full bg-[#2F7FBF] flex items-center justify-center text-xs font-medium text-white shrink-0">
                            {user.name.split(" ").map(n => n[0]).join("").slice(0, 2)}
                        </div>
                        <div className="overflow-hidden">
                            <div className="text-xs font-medium text-white truncate">{user.name}</div>
                            <div className="text-[10px] text-white/50 mt-[1px]">{user.matricula}</div>
                            <span className={`role-badge ${user.roleClass}`}>{user.role}</span>
                        </div>
                    </div>

                    <nav className="p-2 flex-1 flex flex-col gap-1">
                        <div className="text-[9px] font-medium text-white/35 tracking-widest uppercase px-4 pt-2 pb-1">Menu</div>
                        
                        <Link to="/" className={`flex items-center gap-2.5 px-4 py-2 text-[13px] transition-colors border-l-3 ${location.pathname === '/' ? 'bg-[#2F7FBF]/25 text-white border-[#2F7FBF]' : 'text-white/65 border-transparent hover:bg-white/5 hover:text-white/90'}`}>
                            <LayoutDashboard size={16} /> Painel
                        </Link>
                        
                        <Link to="/tces" className="flex items-center justify-between px-4 py-2 text-[13px] transition-colors border-l-3 text-white/65 border-transparent hover:bg-white/5 hover:text-white/90">
                            <div className="flex items-center gap-2.5"><FileText size={16} /> Meus TCEs</div>
                            <span className="bg-[#F5A623] text-[#7B4A00] text-[9px] font-medium px-1.5 py-0.5 rounded-full">1</span>
                        </Link>

                        <Link to="/estagio" className="flex items-center gap-2.5 px-4 py-2 text-[13px] transition-colors border-l-3 text-white/65 border-transparent hover:bg-white/5 hover:text-white/90">
                            <Briefcase size={16} /> Meu Estágio
                        </Link>

                        <Link to="/relatorios" className="flex items-center justify-between px-4 py-2 text-[13px] transition-colors border-l-3 text-white/65 border-transparent hover:bg-white/5 hover:text-white/90">
                            <div className="flex items-center gap-2.5"><ClipboardList size={16} /> Relatórios</div>
                            <span className="bg-[#F5A623] text-[#7B4A00] text-[9px] font-medium px-1.5 py-0.5 rounded-full">2</span>
                        </Link>
                    </nav>
                </aside>

                {/* MAIN CONTENT AREA */}
                <main className="flex-1 flex flex-col overflow-hidden bg-[var(--color-background-primary)]">
                    {/* TOPBAR */}
                    <header className="border-b border-[var(--color-border-tertiary)] p-4 px-6 flex items-center justify-between">
                        <div>
                            <h2 className="text-base font-medium text-[var(--color-text-primary)]">Painel de controle</h2>
                            <p className="text-xs text-[var(--color-text-secondary)] mt-0.5">Engenharia de Software</p>
                        </div>
                        <div className="flex gap-2">
                            <button className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-md text-xs font-medium border border-[var(--color-border-secondary)] hover:bg-[var(--color-background-secondary)] transition-colors">
                                Ver relatórios ↗
                            </button>
                        </div>
                    </header>

                    {/* DYNAMIC CONTENT (AppRoutes Outlet) */}
                    <div className="flex-1 overflow-y-auto p-6 bg-[var(--color-background-secondary)]">
                        <Outlet />
                    </div>
                </main>
            </div>
        </div>
    );
}