import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function MeusTces() {
    const [loading, setLoading] = useState(true);
    const [tces, setTces] = useState<any[]>([]);

    useEffect(() => {
        carregarTces();
    }, []);

    async function carregarTces() {
        try {
            const response = await api.get("/tces/");

            setTces(response.data.results || []);
        } catch (error) {
            console.error("Erro ao carregar TCEs:", error);
        } finally {
            setLoading(false);
        }
    }

    function corStatus(status?: string) {
        if (!status) return "text-gray-600";

        switch (status.toLowerCase()) {
            case "aprovado":
                return "text-green-600 bg-green-100";

            case "reprovado":
                return "text-red-600 bg-red-100";

            default:
                return "text-yellow-700 bg-yellow-100";
        }
    }

    if (loading) {
        return (
            <div className="bg-white p-6 rounded-lg shadow">
                Carregando TCEs...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    Meus TCEs
                </h1>

                <p className="text-gray-500 mt-1">
                    Visualize os termos de compromisso cadastrados.
                </p>
            </div>

            {tces.length === 0 ? (
                <div className="bg-white p-6 rounded-lg shadow text-center">
                    Nenhum TCE encontrado.
                </div>
            ) : (
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">

                    {tces.map((tce) => (
                        <div
                            key={tce.apoliceseguro}
                            className="bg-white rounded-lg shadow p-5 border"
                        >

                            <div className="flex justify-between items-center mb-4">

                                <h2 className="font-bold text-lg">
                                    TCE #{tce.apoliceseguro}
                                </h2>

                                <span
                                    className={`px-3 py-1 rounded-full text-sm font-semibold ${corStatus(
                                        tce.status
                                    )}`}
                                >
                                    {tce.status}
                                </span>

                            </div>

                            <div className="space-y-2">

                                <p>
                                    <strong>Apólice:</strong>{" "}
                                    {tce.apoliceseguro}
                                </p>

                                <p>
                                    <strong>Bolsa:</strong>{" "}
                                    R$ {tce.bolsa}
                                </p>

                                <p>
                                    <strong>Aluno:</strong>{" "}
                                    {tce.aluno_nome}
                                </p>

                                <p>
                                    <strong>Matrícula:</strong>{" "}
                                    {tce.aluno_id}
                                </p>

                            </div>

                        </div>
                    ))}

                </div>
            )}

        </div>
    );
}