import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function DashboardAluno() {
    const [loading, setLoading] = useState(true);

    const [tce, setTce] = useState<any>(null);
    const [estagio, setEstagio] = useState<any>(null);
    const [relatorios, setRelatorios] = useState<any[]>([]);

    useEffect(() => {
        carregarDados();
    }, []);

    async function carregarDados() {
        try {
            const [tceRes, estagioRes, relatorioRes] =
                await Promise.all([
                    api.get("/tces/"),
                    api.get("/estagios/"),
                    api.get("/relatorios/")
                ]);

            setTce(tceRes.data.results?.[0] || null);
            setEstagio(estagioRes.data.results?.[0] || null);
            setRelatorios(relatorioRes.data.results || []);

        } catch (err) {
            console.error("ERRO:", err);
        } finally {
            setLoading(false);
        }
    }

    const horasAcumuladas = relatorios.reduce(
        (total, rel) => total + rel.horas_estagiadas,
        0
    );

    const percentualHoras = Math.min(
        (horasAcumuladas / 350) * 100,
        100
    );

    function formatarData(data?: string) {
        if (!data) return "-";

        return new Date(data).toLocaleDateString("pt-BR");
    }

    function corStatus(status?: string) {
        if (!status) return "text-gray-600";

        switch (status.toLowerCase()) {
            case "aprovado":
                return "text-green-600 font-semibold";

            case "reprovado":
                return "text-red-600 font-semibold";

            default:
                return "text-yellow-600 font-semibold";
        }
    }

    if (loading) {
        return (
            <div className="bg-white p-6 rounded-lg shadow">
                Carregando informações...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    Dashboard do Aluno
                </h1>

                <p className="text-gray-500 mt-1">
                    Acompanhe seu estágio e seus relatórios.
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">

                <div className="bg-white p-5 rounded-lg shadow">
                    <h2 className="font-semibold text-lg mb-3">
                        TCE
                    </h2>

                    <p>
                        <strong>Apólice:</strong>{" "}
                        {tce?.apoliceseguro}
                    </p>

                    <p>
                        <strong>Bolsa:</strong>{" "}
                        R$ {tce?.bolsa}
                    </p>

                    <p>
                        <strong>Status:</strong>{" "}
                        <span className={corStatus(tce?.status)}>
                            {tce?.status}
                        </span>
                    </p>
                </div>

                <div className="bg-white p-5 rounded-lg shadow">
                    <h2 className="font-semibold text-lg mb-3">
                        Estágio
                    </h2>

                    <p>
                        <strong>Empresa:</strong>{" "}
                        {estagio?.empresa_nome}
                    </p>

                    <p>
                        <strong>Início:</strong>{" "}
                        {formatarData(estagio?.dtinicio)}
                    </p>

                    <p>
                        <strong>Carga Horária:</strong>{" "}
                        {estagio?.cargahorariasemanal}h
                    </p>
                </div>

                <div className="bg-white p-5 rounded-lg shadow">
                    <h2 className="font-semibold text-lg mb-3">
                        Relatórios
                    </h2>

                    <p className="text-3xl font-bold text-blue-600">
                        {relatorios.length}
                    </p>

                    <p className="text-gray-500">
                        enviados
                    </p>
                </div>

                <div className="bg-white p-5 rounded-lg shadow">
                    <h2 className="font-semibold text-lg mb-3">
                        Horas Acumuladas
                    </h2>

                    <p className="text-3xl font-bold text-green-600">
                        {horasAcumuladas}
                    </p>

                    <p className="text-gray-500">
                        de 350 horas
                    </p>
                </div>

            </div>

            <div className="bg-white p-5 rounded-lg shadow">

                <div className="flex justify-between mb-2">
                    <span className="font-medium">
                        Progresso do Estágio
                    </span>

                    <span>
                        {horasAcumuladas}/350 horas
                    </span>
                </div>

                <div className="w-full bg-gray-200 rounded-full h-4">
                    <div
                        className="bg-green-500 h-4 rounded-full transition-all"
                        style={{
                            width: `${percentualHoras}%`
                        }}
                    />
                </div>

            </div>

            <div className="bg-white p-5 rounded-lg shadow">

                <h2 className="font-semibold text-lg mb-4">
                    Relatórios Enviados
                </h2>

                <div className="overflow-x-auto">

                    <table className="w-full">

                        <thead>
                            <tr className="border-b bg-gray-50">
                                <th className="text-left p-3">
                                    ID
                                </th>

                                <th className="text-left p-3">
                                    Semestre
                                </th>

                                <th className="text-left p-3">
                                    Data
                                </th>

                                <th className="text-left p-3">
                                    Horas
                                </th>

                                <th className="text-left p-3">
                                    Status
                                </th>
                            </tr>
                        </thead>

                        <tbody>

                            {relatorios.map((rel) => (
                                <tr
                                    key={rel.idrelatorio}
                                    className="border-b hover:bg-gray-50"
                                >
                                    <td className="p-3">
                                        {rel.idrelatorio}
                                    </td>

                                    <td className="p-3">
                                        {rel.semestre}
                                    </td>

                                    <td className="p-3">
                                        {formatarData(rel.data_envio)}
                                    </td>

                                    <td className="p-3">
                                        {rel.horas_estagiadas}
                                    </td>

                                    <td className="p-3">
                                        <span className={corStatus(rel.status)}>
                                            {rel.status}
                                        </span>
                                    </td>
                                </tr>
                            ))}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>
    );
}