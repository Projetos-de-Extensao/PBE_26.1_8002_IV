import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function TcesSecretaria() {
    const [loading, setLoading] = useState(true);
    const [tces, setTces] = useState<any[]>([]);

    useEffect(() => {
        carregarTces();
    }, []);

    async function carregarTces() {
        try {
            const response = await api.get("/tces/");

            console.log("===== TCES SECRETARIA =====");
            console.log(response.data);

            setTces(response.data.results || []);
        } catch (error) {
            console.error("Erro ao carregar TCEs:", error);
        } finally {
            setLoading(false);
        }
    }

    async function aprovarTce(apolice: string) {
        try {
            await api.post(`/tces/${apolice}/aprovar/`);

            alert("TCE aprovado com sucesso!");

            carregarTces();
        } catch (error) {
            console.error(error);
            alert("Erro ao aprovar TCE");
        }
    }

    async function reprovarTce(apolice: string) {
        try {
            await api.post(`/tces/${apolice}/reprovar/`);

            alert("TCE reprovado com sucesso!");

            carregarTces();
        } catch (error) {
            console.error(error);
            alert("Erro ao reprovar TCE");
        }
    }

    function corStatus(status?: string) {
        if (!status) {
            return "bg-yellow-100 text-yellow-700";
        }

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
            <div className="bg-white p-6 rounded-lg shadow">
                Carregando TCEs...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    TCEs
                </h1>

                <p className="text-gray-500 mt-1">
                    Gerencie os termos de compromisso cadastrados.
                </p>
            </div>

            <div className="bg-white rounded-lg shadow border overflow-hidden">

                <table className="w-full">

                    <thead className="bg-gray-100">
                        <tr>
                            <th className="text-left p-4">Aluno</th>
                            <th className="text-left p-4">Apólice</th>
                            <th className="text-left p-4">Bolsa</th>
                            <th className="text-left p-4">Secretaria</th>
                            <th className="text-left p-4">Status</th>
                            <th className="text-left p-4">Ações</th>
                        </tr>
                    </thead>

                    <tbody>

                        {tces.map((tce) => (
                            <tr
                                key={tce.apoliceseguro}
                                className="border-t hover:bg-gray-50"
                            >
                                <td className="p-4">
                                    {tce.aluno_nome}
                                </td>

                                <td className="p-4">
                                    {tce.apoliceseguro}
                                </td>

                                <td className="p-4">
                                    R$ {Number(tce.bolsa).toFixed(2)}
                                </td>

                                <td className="p-4">
                                    {tce.secretaria}
                                </td>

                                <td className="p-4">
                                    <span
                                        className={`px-3 py-1 rounded-full text-sm font-semibold ${corStatus(
                                            tce.status
                                        )}`}
                                    >
                                        {tce.status}
                                    </span>
                                </td>

                                <td className="p-4">
                                    <div className="flex gap-2">

                                        <button
                                            onClick={() =>
                                                aprovarTce(
                                                    tce.apoliceseguro
                                                )
                                            }
                                            className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
                                        >
                                            Aprovar
                                        </button>

                                        <button
                                            onClick={() =>
                                                reprovarTce(
                                                    tce.apoliceseguro
                                                )
                                            }
                                            className="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700"
                                        >
                                            Reprovar
                                        </button>

                                    </div>
                                </td>

                            </tr>
                        ))}

                    </tbody>

                </table>

            </div>

        </div>
    );
}