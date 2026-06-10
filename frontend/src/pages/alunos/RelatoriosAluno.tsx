import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function RelatoriosAluno() {
    const [loading, setLoading] = useState(true);
    const [relatorios, setRelatorios] = useState<any[]>([]);

    useEffect(() => {
        carregarRelatorios();
    }, []);

    async function carregarRelatorios() {
        try {
            const response = await api.get("/relatorios/");

            setRelatorios(response.data.results || []);
        } catch (error) {
            console.error("Erro ao carregar relatórios:", error);
        } finally {
            setLoading(false);
        }
    }

    function corStatus(status: string) {
        if (!status) return "bg-gray-100 text-gray-700";

        switch (status.toLowerCase()) {
            case "aprovado":
                return "bg-green-100 text-green-700";

            case "reprovado":
                return "bg-red-100 text-red-700";

            default:
                return "bg-yellow-100 text-yellow-700";
        }
    }

    if (loading) {
        return (
            <div className="bg-white rounded-lg p-6">
                Carregando relatórios...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    Relatórios
                </h1>

                <p className="text-gray-500">
                    Histórico de relatórios enviados.
                </p>
            </div>

            <div className="bg-white rounded-lg border shadow-sm overflow-hidden">

                <table className="w-full">
                    <thead className="bg-gray-50 border-b">
                        <tr>
                            <th className="text-left px-4 py-3">
                                ID
                            </th>

                            <th className="text-left px-4 py-3">
                                Semestre
                            </th>

                            <th className="text-left px-4 py-3">
                                Data
                            </th>

                            <th className="text-left px-4 py-3">
                                Horas
                            </th>

                            <th className="text-left px-4 py-3">
                                Status
                            </th>
                        </tr>
                    </thead>

                    <tbody>
                        {relatorios.map((relatorio) => (
                            <tr
                                key={relatorio.idrelatorio}
                                className="border-b"
                            >
                                <td className="px-4 py-3">
                                    #{relatorio.idrelatorio}
                                </td>

                                <td className="px-4 py-3">
                                    {relatorio.semestre}
                                </td>

                                <td className="px-4 py-3">
                                    {relatorio.data_envio}
                                </td>

                                <td className="px-4 py-3">
                                    {relatorio.horas_estagiadas}
                                </td>

                                <td className="px-4 py-3">
                                    <span
                                        className={`px-2 py-1 rounded-full text-xs font-medium ${corStatus(relatorio.status)}`}
                                    >
                                        {relatorio.status}
                                    </span>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>

            </div>

        </div>
    );
}