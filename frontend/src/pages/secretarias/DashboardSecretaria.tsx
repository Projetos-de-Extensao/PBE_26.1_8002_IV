import { useState, useEffect } from "react";
import {
    Users,
    FileText,
    Briefcase,
    Building,
    ArrowRight,
    Inbox,
    Loader2
} from "lucide-react";
import { api } from "../../api/axios";

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

    const [resumo, setResumo] = useState<ResumoSecretaria>({
        alunosAtivos: 0,
        tcesPendentes: 0,
        estagiosAtivos: 0,
        empresas: 0,
    });

    const [tces, setTces] = useState<TcePendente[]>([]);

    useEffect(() => {
        carregarDados();
    }, []);

    async function carregarDados() {
        try {
            const [
                alunosRes,
                tcesPendentesRes,
                estagiosRes,
                empresasRes,
                tcesListaRes
            ] = await Promise.all([
                api.get("/alunos/"),
                api.get("/tces/"),
                api.get("/estagios/"),
                api.get("/empresas/"),
                api.get("/tces/")
            ]);

            console.log("===== ALUNOS =====");
            console.log(alunosRes.data);

            console.log("===== TCES =====");
            console.log(tcesPendentesRes.data);

            console.log("===== ESTAGIOS =====");
            console.log(estagiosRes.data);

            console.log("===== EMPRESAS =====");
            console.log(empresasRes.data);

            setResumo({
                alunosAtivos:
                    alunosRes.data.count ||
                    alunosRes.data.results?.length ||
                    alunosRes.data.length ||
                    0,

                tcesPendentes:
                    tcesPendentesRes.data.count ||
                    tcesPendentesRes.data.results?.length ||
                    tcesPendentesRes.data.length ||
                    0,

                estagiosAtivos:
                    estagiosRes.data.count ||
                    estagiosRes.data.results?.length ||
                    estagiosRes.data.length ||
                    0,

                empresas:
                    empresasRes.data.count ||
                    empresasRes.data.results?.length ||
                    empresasRes.data.length ||
                    0,
            });

            const listaTces =
                tcesListaRes.data.results ||
                tcesListaRes.data ||
                [];

            setTces(
                listaTces.slice(0, 5).map((tce: any) => ({
                    id: tce.id || tce.tce,
                    aluno_nome:
                        tce.aluno_nome ||
                        tce.aluno?.nome ||
                        tce.aluno ||
                        "Aluno",

                    empresa_nome:
                        tce.empresa_nome ||
                        tce.empresa?.nome ||
                        tce.empresa ||
                        "Empresa",

                    status: tce.status || "pendente",
                }))
            );
        } catch (error) {
            console.error("Erro ao carregar dashboard:", error);
        } finally {
            setLoading(false);
        }
    }

    const getStatusPill = (status: string) => (
        <span className="px-2 py-1 rounded-full text-xs bg-yellow-100 text-yellow-700">
            {status}
        </span>
    );

    if (loading) {
        return (
            <div className="flex items-center justify-center h-full gap-2">
                <Loader2 size={24} className="animate-spin" />
                Carregando painel...
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-5">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">

                <div className="bg-white rounded-lg border p-4">
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                        <Users size={16} />
                        Alunos ativos
                    </div>

                    <div className="text-3xl font-bold mt-2">
                        {resumo.alunosAtivos}
                    </div>
                </div>

                <div className="bg-white rounded-lg border p-4">
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                        <FileText size={16} />
                        TCEs
                    </div>

                    <div className="text-3xl font-bold mt-2">
                        {resumo.tcesPendentes}
                    </div>
                </div>

                <div className="bg-white rounded-lg border p-4">
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                        <Briefcase size={16} />
                        Estágios
                    </div>

                    <div className="text-3xl font-bold mt-2">
                        {resumo.estagiosAtivos}
                    </div>
                </div>

                <div className="bg-white rounded-lg border p-4">
                    <div className="flex items-center gap-2 text-sm text-gray-500">
                        <Building size={16} />
                        Empresas
                    </div>

                    <div className="text-3xl font-bold mt-2">
                        {resumo.empresas}
                    </div>
                </div>

            </div>

            <div className="bg-white rounded-xl border p-4">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="font-semibold">
                        Últimos TCEs
                    </h2>

                    <button className="text-blue-600 flex items-center gap-1">
                        Ver todos
                        <ArrowRight size={14} />
                    </button>
                </div>

                {tces.length === 0 ? (
                    <div className="flex flex-col items-center py-8 text-gray-500">
                        <Inbox size={28} />
                        <p>Nenhum TCE encontrado.</p>
                    </div>
                ) : (
                    <div className="space-y-3">
                        {tces.map((tce) => (
                            <div
                                key={tce.id}
                                className="border rounded-lg p-3 flex justify-between items-center"
                            >
                                <div>
                                    <div className="font-medium">
                                        TCE #{tce.id}
                                    </div>

                                    <div className="text-sm text-gray-500">
                                        {tce.aluno_nome}
                                    </div>

                                    <div className="text-sm text-gray-500">
                                        {tce.empresa_nome}
                                    </div>
                                </div>

                                {getStatusPill(tce.status)}
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}