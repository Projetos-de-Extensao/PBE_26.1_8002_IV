import { useState, useEffect } from "react";
import { Users, FileText, Briefcase, Building, ArrowRight, Inbox, Loader2 } from "lucide-react";
import { api } from "../api/axios";

// Definição das interfaces com base no seu backend Django (models.py)
interface ResumoSecretaria {
    alunosAtivos: number;
    tcesPendentes: number;
    estagiosAtivos: number;
    empresas: number;
}

interface TcePendente {
    id: number;
    aluno_nome: string;
    empresa_nome: string;
    status: string;
}

export default function DashboardSecretaria() {
    const [loading, setLoading] = useState(true);
    
    const [resumo, setResumo] = useState<ResumoSecretaria | null>(null);

    const [tces, setTces] = useState<TcePendente[]>([]);

    // Busca os dados REAIS da sua API Django (val_estagio/views.py)
    useEffect(() => {
        const carregarDadosReais = async () => {
            try {
                // Dispara todas as requisições ao mesmo tempo para ser mais rápido
                const [alunosRes, tcesPendentesRes, estagiosRes, empresasRes, tcesListaRes] = await Promise.all([
                    api.get("/alunos/"),
                    api.get("/tces/?status=pendente"),
                    api.get("/estagios/"),
                    api.get("/empresas/"),
                    api.get("/tces/?status=pendente&limit=5") // Busca os 5 últimos TCEs
                ]);

                // Atualiza o resumo com a contagem real vinda do banco de dados
                setResumo({
                    alunosAtivos: alunosRes.data.count || alunosRes.data.length || 0,
                    tcesPendentes: tcesPendentesRes.data.count || tcesPendentesRes.data.length || 0,
                    estagiosAtivos: estagiosRes.data.count || estagiosRes.data.length || 0,
                    empresas: empresasRes.data.count || empresasRes.data.length || 0,
                });

                // Atualiza a lista de documentos (Adaptar aos campos reais do seu TceSerializer)
                const listaReal = tcesListaRes.data.results || tcesListaRes.data;
                if (listaReal && listaReal.length > 0) {
                    setTces(listaReal.map((tce: any) => ({
                        id: tce.id,
                        aluno_nome: tce.aluno?.usuario?.nome || tce.aluno_nome || 'Aluno Sem Nome',
                        empresa_nome: tce.empresa?.nome || 'Empresa Indefinida',
                        status: tce.status
                    })));
                }

            } catch (error) {
                console.warn("Usando dados do Mockup. A API retornou erro ou não tem dados:", error);
            } finally {
                setLoading(false);
            }
        };

        carregarDadosReais();
    }, []);

    // Componente visual de Status (Pílula)
    const getStatusPill = (status: string) => {
        const isPendente = status.toLowerCase() === 'pendente';
        return (
            <span className={`status-pill status-${status} ${isPendente ? 'animate-pulse' : ''}`}>
                <span className={`stat-dot dot-${status}`}></span>
                {status.charAt(0).toUpperCase() + status.slice(1)}
            </span>
        );
    };

    if (loading) {
        return (
            <div className="flex h-full items-center justify-center text-[var(--color-text-secondary)] gap-2">
                <Loader2 size={24} className="animate-spin" /> Carregando painel da secretaria...
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-5">
            
            {/* GRID DE ESTATÍSTICAS */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                    <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                        <Users size={14} /> Alunos ativos
                    </div>
                    <div className="text-[22px] font-medium text-[var(--color-text-primary)]">{resumo.alunosAtivos}</div>
                </div>

                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                    <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                        <FileText size={14} /> TCEs pendentes
                    </div>
                    <div className="text-[22px] font-medium text-[#F5A623]">{resumo.tcesPendentes}</div>
                    <div className="text-[11px] text-[var(--color-text-secondary)] mt-1">aguardando aprovação</div>
                </div>

                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                    <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                        <Briefcase size={14} /> Estágios ativos
                    </div>
                    <div className="text-[22px] font-medium text-[var(--color-text-primary)]">{resumo.estagiosAtivos}</div>
                </div>

                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-lg p-3.5 shadow-sm">
                    <div className="text-[11px] text-[var(--color-text-secondary)] mb-1.5 flex items-center gap-1.5">
                        <Building size={14} /> Empresas cadastradas
                    </div>
                    <div className="text-[22px] font-medium text-[var(--color-text-primary)]">{resumo.empresas}</div>
                </div>
            </div>

            {/* DUAS COLUNAS: TCEs e Relatórios */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                {/* COLUNA 1 - TCEs PENDENTES */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm flex flex-col">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <FileText size={16} className="text-[var(--color-text-secondary)]" /> TCEs pendentes de aprovação
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col gap-2 flex-1">
                        {tces.length > 0 ? tces.map((doc) => (
                            <div key={doc.id} className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--color-border-tertiary)] bg-[var(--color-background-secondary)]">
                                <div className="doc-icon doc-icon-tce"><FileText size={16} /></div>
                                <div className="flex-1 min-w-0">
                                    <div className="text-xs font-medium text-[var(--color-text-primary)] truncate">TCE #{doc.id.toString().padStart(3, '0')}</div>
                                    <div className="text-[11px] text-[var(--color-text-secondary)] mt-0.5">{doc.aluno_nome} · {doc.empresa_nome}</div>
                                </div>
                                {getStatusPill(doc.status)}
                            </div>
                        )) : (
                            <div className="flex flex-col items-center justify-center flex-1 py-8 text-[var(--color-text-secondary)]">
                                <Inbox size={28} className="opacity-40 mb-2" />
                                <span className="text-xs">Nenhum documento pendente</span>
                            </div>
                        )}
                    </div>
                </div>

                {/* COLUNA 2 - RELATÓRIOS SEMESTRAIS (Vazio para Secretaria) */}
                <div className="bg-white border border-[var(--color-border-tertiary)] rounded-xl p-4 shadow-sm flex flex-col">
                    <div className="flex items-center justify-between mb-3.5">
                        <div className="text-[13px] font-medium flex items-center gap-2 text-[var(--color-text-primary)]">
                            <Inbox size={16} className="text-[var(--color-text-secondary)]" /> Relatórios semestrais
                        </div>
                        <button className="text-[11px] text-[#2F7FBF] flex items-center gap-1 hover:underline">
                            Ver todos <ArrowRight size={11} />
                        </button>
                    </div>
                    
                    <div className="flex flex-col items-center justify-center flex-1 py-8 text-[var(--color-text-secondary)] bg-[var(--color-background-secondary)] border border-[var(--color-border-tertiary)] rounded-lg">
                        <Inbox size={28} className="opacity-40 mb-2" />
                        <span className="text-xs">Nenhum relatório para análise</span>
                    </div>
                </div>

            </div>
        </div>
    );
}
