import { Briefcase, Clock, FileText, ClipboardList, ArrowRight } from "lucide-react";

export default function Dashboard() {
    // Dados mockados baseados no seu script HTML
    const stats = [
        { label: 'Estágio', icon: Briefcase, value: 'Ativo', sub: 'TechCorp Ltda', color: 'text-[#27AE60]' },
        { label: 'Horas', icon: Clock, value: '210', sub: 'de 350 horas' },
        { label: 'TCE', icon: FileText, value: 'Aprovado', sub: 'Apólice #2024-001', color: 'text-[#27AE60]' },
        { label: 'Relatórios', icon: ClipboardList, value: '2', sub: '1 pendente de análise' },
    ];

    const tces = [
        { name: 'TCE #2024-001', meta: 'TechCorp Ltda · Sec. Maria Lima', status: 'aprovado' },
    ];

    const relatorios = [
        { name: 'Relatório 24.1', meta: 'Enviado em 15/07/2024 · 120h', status: 'aprovado' },
        { name: 'Relatório 24.2', meta: 'Enviado em 10/12/2024 · 90h', status: 'pendente' },
    ];

    const getStatusPill = (status: string) => (
        <span className={`status-pill status-${status} ${status === 'pendente' ? 'animate-pulse' : ''}`}>
            <span className={`stat-dot dot-${status}`}></span>
            {status.charAt(0).toUpperCase() + status.slice(1)}
        </span>
    );

    return (
        <div className="flex flex-col gap-5">
            {/* GRID DE ESTATÍSTICAS */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
                {stats.map((s, i) => (
                    <div key={i} className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                        <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                            <s.icon size={14} /> {s.label}
                        </div>
                        <div className={`text-[22px] font-medium ${s.color || 'text-[var(--color-text-primary)]'}`}>
                            {s.value}
                        </div>
                        <div className="text-[11px] text-[var(--color-text-secondary)] mt-1">{s.sub}</div>
                    </div>
                ))}
            </div>

            {/* DUAS COLUNAS: TCEs e Relatórios */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* COLUNA 1 - TCEs */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <FileText size={16} className="text-[var(--color-text-secondary)]" /> Meus TCEs
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col gap-2">
                        {tces.map((doc, i) => (
                            <div key={i} className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--color-border-tertiary)] bg-[var(--color-background-secondary)]">
                                <div className="doc-icon doc-icon-tce"><FileText size={16} /></div>
                                <div className="flex-1 min-w-0">
                                    <div className="text-xs font-medium text-[var(--color-text-primary)] truncate">{doc.name}</div>
                                    <div className="text-[11px] text-[var(--color-text-secondary)] mt-0.5">{doc.meta}</div>
                                </div>
                                {getStatusPill(doc.status)}
                            </div>
                        ))}
                    </div>
                </div>

                {/* COLUNA 2 - Relatórios */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <ClipboardList size={16} className="text-[var(--color-text-secondary)]" /> Relatórios semestrais
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col gap-2">
                        {relatorios.map((rel, i) => (
                            <div key={i} className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--color-border-tertiary)] bg-[var(--color-background-secondary)]">
                                <div className="doc-icon doc-icon-rel"><ClipboardList size={16} /></div>
                                <div className="flex-1 min-w-0">
                                    <div className="text-xs font-medium text-[var(--color-text-primary)] truncate">{rel.name}</div>
                                    <div className="text-[11px] text-[var(--color-text-secondary)] mt-0.5">{rel.meta}</div>
                                </div>
                                {getStatusPill(rel.status)}
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* MEU ESTÁGIO */}
            <div>
                <h3 className="text-[11px] font-medium text-[var(--color-text-secondary)] uppercase tracking-wider mb-2.5 mt-2">Meu estágio ativo</h3>
                <div className="border border-[var(--color-border-tertiary)] rounded-md p-3.5 bg-white shadow-sm">
                    <div className="text-[13px] font-medium text-[var(--color-text-primary)]">TechCorp Ltda</div>
                    <div className="text-[11px] text-[var(--color-text-secondary)] mt-1 flex gap-3">
                        <span className="flex items-center gap-1"><Briefcase size={12}/> Início: 01/03/2024</span>
                        <span className="flex items-center gap-1"><Clock size={12}/> 20h/semana</span>
                    </div>
                    <div className="mt-3">
                        <div className="flex justify-between text-[10px] text-[var(--color-text-secondary)] mb-1">
                            <span>Horas acumuladas</span>
                            <span>210 / 350h</span>
                        </div>
                        <div className="h-1 bg-[var(--color-border-tertiary)] rounded-full overflow-hidden">
                            <div className="h-full bg-[#27AE60] rounded-full" style={{ width: '60%' }}></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    );
}