import { Briefcase, Clock, FileText, ClipboardList, ArrowRight, Users, Building, Check, X, Cpu } from "lucide-react";

const dashboardDataData = {
    aluno: {
        stats: [
            { label: 'Estágio', icon: Briefcase, value: 'Ativo', sub: 'TechCorp Ltda', color: 'text-[#27AE60]' },
            { label: 'Horas acumuladas', icon: Clock, value: '210', sub: 'de 350 horas' },
            { label: 'TCE', icon: FileText, value: 'Aprovado', sub: 'Apólice #2024-001', color: 'text-[#27AE60]' },
            { label: 'Relatórios', icon: ClipboardList, value: '2', sub: '1 pendente de análise' },
        ],
        docs: [{ name: 'TCE #2024-001', meta: 'TechCorp Ltda · Secretaria Maria Lima', status: 'aprovado', type: 'tce' }],
        relatorios: [
            { name: 'Relatório 24.1', meta: 'Enviado em 15/07/2024 · 120h', status: 'aprovado' },
            { name: 'Relatório 24.2', meta: 'Enviado em 10/12/2024 · 90h', status: 'pendente' },
        ],
        estagio: { empresa: 'TechCorp Ltda', inicio: '01/03/2024', carga: '20h/semana', horas: 210, max: 350 }
    },
    secretaria: {
        stats: [
            { label: 'Alunos ativos', icon: Users, value: '148' },
            { label: 'TCEs pendentes', icon: FileText, value: '3', sub: 'aguardando aprovação', color: 'text-[#F5A623]' },
            { label: 'Estágios ativos', icon: Briefcase, value: '62' },
            { label: 'Empresas cadastradas', icon: Building, value: '27' },
        ],
        docs: [
            { name: 'TCE #2024-045', meta: 'João Silva · TechCorp Ltda', status: 'pendente', type: 'tce' },
            { name: 'TCE #2024-044', meta: 'Ana Costa · StartupXP', status: 'pendente', type: 'tce' },
            { name: 'TCE #2024-043', meta: 'Carlos Melo · Banco Digital', status: 'pendente', type: 'tce' },
        ],
        relatorios: [],
        estagio: null
    },
    coordenador: {
        stats: [
            { label: 'Relatórios pendentes', icon: ClipboardList, value: '4', sub: 'aguardando análise', color: 'text-[#F5A623]' },
            { label: 'Aprovados este semestre', icon: Check, value: '18', color: 'text-[#27AE60]' },
            { label: 'Reprovados', icon: X, value: '2', color: 'text-[#E74C3C]' },
            { label: 'Área', icon: Cpu, value: 'Tecnologia' },
        ],
        docs: [],
        relatorios: [
            { name: 'Relatório 24.2 — João Silva', meta: 'TechCorp Ltda · 90h estagiadas', status: 'pendente' },
            { name: 'Relatório 24.2 — Ana Costa', meta: 'StartupXP · 80h estagiadas', status: 'pendente' },
            { name: 'Relatório 24.1 — Marcos T.', meta: 'TechCorp Ltda · 120h estagiadas', status: 'pendente' },
            { name: 'Relatório 24.2 — Carla N.', meta: 'BigData Inc · 110h estagiadas', status: 'pendente' },
        ],
        estagio: null
    }
};

export default function Dashboard() {
    const currentRole = (localStorage.getItem("userRole") || "aluno") as "aluno" | "secretaria" | "coordenador";
    const data = dashboardDataData[currentRole] || dashboardDataData.aluno;

    const getStatusPill = (status: string) => (
        <span className={`status-pill status-${status} ${status === 'pendente' ? 'animate-pulse' : ''}`}>
            <span className={`stat-dot dot-${status}`}></span>
            {status.charAt(0).toUpperCase() + status.slice(1)}
        </span>
    );

    const docCardTitle = currentRole === 'aluno' ? 'Meus TCEs' : currentRole === 'secretaria' ? 'TCEs pendentes de aprovação' : 'Documentos';
    const relCardTitle = currentRole === 'coordenador' ? 'Relatórios para análise' : 'Relatórios semestrais';

    return (
        <div className="flex flex-col gap-5">
            {/* GRID DE CARDS DE ESTATÍSTICA */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
                {data.stats.map((s, i) => {
                    const Icon = s.icon;
                    return (
                        <div key={i} className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                            <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                                <Icon size={14} /> {s.label}
                            </div>
                            <div className={`text-[22px] font-medium ${s.color || 'text-[var(--color-text-primary)]'}`}>
                                {s.value}
                            </div>
                            {'sub' in s && <div className="text-[11px] text-[var(--color-text-secondary)] mt-1">{s.sub}</div>}
                        </div>
                    );
                })}
            </div>

            {/* DUAS COLUNAS */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* COLUNA ESQUERDA - DOCUMENTOS / TCEs */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <FileText size={16} className="text-[var(--color-text-secondary)]" /> {docCardTitle}
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col gap-2">
                        {data.docs.length > 0 ? (
                            data.docs.map((doc, i) => (
                                <div key={i} className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--color-border-tertiary)] bg-[var(--color-background-secondary)]">
                                    <div className="doc-icon doc-icon-tce"><FileText size={16} /></div>
                                    <div className="flex-1 min-w-0">
                                        <div className="text-xs font-medium text-[var(--color-text-primary)] truncate">{doc.name}</div>
                                        <div className="text-[11px] text-[var(--color-text-secondary)] mt-0.5">{doc.meta}</div>
                                    </div>
                                    {getStatusPill(doc.status)}
                                </div>
                            ))
                        ) : (
                            <div className="text-center py-6 text-xs text-[var(--color-text-secondary)]">Nenhum documento pendente</div>
                        )}
                    </div>
                </div>

                {/* COLUNA DIREITA - RELATÓRIOS */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <ClipboardList size={16} className="text-[var(--color-text-secondary)]" /> {relCardTitle}
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col gap-2">
                        {data.relatorios.length > 0 ? (
                            data.relatorios.map((rel, i) => (
                                <div key={i} className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--color-border-tertiary)] bg-[var(--color-background-secondary)]">
                                    <div className="doc-icon doc-icon-rel"><ClipboardList size={16} /></div>
                                    <div className="flex-1 min-w-0">
                                        <div className="text-xs font-medium text-[var(--color-text-primary)] truncate">{rel.name}</div>
                                        <div className="text-[11px] text-[var(--color-text-secondary)] mt-0.5">{rel.meta}</div>
                                    </div>
                                    {getStatusPill(rel.status)}
                                </div>
                            ))
                        ) : (
                            <div className="text-center py-6 text-xs text-[var(--color-text-secondary)]">Nenhum relatório cadastrado</div>
                        )}
                    </div>
                </div>
            </div>

            {/* SEÇÃO INFERIOR EXCLUSIVA DO ALUNO */}
            {data.estagio && (
                <div>
                    <h3 className="text-[11px] font-medium text-[var(--color-text-secondary)] uppercase tracking-wider mb-2.5 mt-2">Meu estágio ativo</h3>
                    <div className="border border-[var(--color-border-tertiary)] rounded-md p-3.5 bg-white shadow-sm">
                        <div className="text-[13px] font-medium text-[var(--color-text-primary)]">{data.estagio.empresa}</div>
                        <div className="text-[11px] text-[var(--color-text-secondary)] mt-1 flex gap-3">
                            <span className="flex items-center gap-1"><Briefcase size={12}/> Início: {data.estagio.inicio}</span>
                            <span className="flex items-center gap-1"><Clock size={12}/> {data.estagio.carga}</span>
                        </div>
                        <div className="mt-3">
                            <div className="flex justify-between text-[10px] text-[var(--color-text-secondary)] mb-1">
                                <span>Horas acumuladas</span>
                                <span>{data.estagio.horas} / {data.estagio.max}h</span>
                            </div>
                            <div className="h-1 bg-[var(--color-border-tertiary)] rounded-full overflow-hidden">
                                <div className="h-full bg-[#27AE60] rounded-full" style={{ width: `${Math.round((data.estagio.horas / data.estagio.max) * 100)}%` }}></div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}