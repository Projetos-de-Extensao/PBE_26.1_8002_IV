import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function Empresas() {
    const [loading, setLoading] = useState(true);
    const [empresas, setEmpresas] = useState<any[]>([]);
    const [busca, setBusca] = useState("");

    useEffect(() => {
        carregarEmpresas();
    }, []);

    async function carregarEmpresas() {
        try {
            const response = await api.get("/empresas/");

            setEmpresas(response.data.results || []);
        } catch (error) {
            console.error("Erro ao carregar empresas:", error);
        } finally {
            setLoading(false);
        }
    }

    async function excluirEmpresa(id: number) {
        const confirmar = window.confirm(
            "Deseja realmente excluir esta empresa?"
        );

        if (!confirmar) return;

        try {
            await api.delete(`/empresas/${id}/`);

            setEmpresas(
                empresas.filter((empresa) => empresa.id !== id)
            );

            alert("Empresa removida com sucesso.");
        } catch (error) {
            console.error(error);
            alert("Erro ao excluir empresa.");
        }
    }

    const empresasFiltradas = empresas.filter((empresa) =>
        empresa.nome?.toLowerCase().includes(
            busca.toLowerCase()
        )
    );

    if (loading) {
        return (
            <div className="bg-white p-6 rounded-lg shadow">
                Carregando empresas...
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div className="flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold">
                        Empresas
                    </h1>

                    <p className="text-gray-500 mt-1">
                        Empresas conveniadas cadastradas no sistema.
                    </p>

                    <p className="text-sm text-gray-400 mt-2">
                        {empresas.length} empresa(s) cadastrada(s)
                    </p>
                </div>

                <button
                    className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                >
                    Nova Empresa
                </button>
            </div>

            <div className="bg-white p-4 rounded-lg shadow border">
                <input
                    type="text"
                    placeholder="Buscar empresa pelo nome..."
                    value={busca}
                    onChange={(e) => setBusca(e.target.value)}
                    className="w-full border rounded px-3 py-2"
                />
            </div>

            {empresasFiltradas.length === 0 ? (
                <div className="bg-white p-8 rounded-lg shadow border text-center">
                    Nenhuma empresa encontrada.
                </div>
            ) : (
                <div className="bg-white rounded-lg shadow border overflow-hidden">

                    <table className="w-full">

                        <thead className="bg-gray-100">
                            <tr>
                                <th className="text-left p-4">Nome</th>
                                <th className="text-left p-4">Telefone</th>
                                <th className="text-left p-4">CNPJ</th>
                                <th className="text-left p-4">Cidade</th>
                                <th className="text-left p-4">CEP</th>
                                <th className="text-left p-4">Ações</th>
                            </tr>
                        </thead>

                        <tbody>

                            {empresasFiltradas.map((empresa) => (
                                <tr
                                    key={empresa.id}
                                    className="border-t hover:bg-gray-50"
                                >
                                    <td className="p-4">
                                        {empresa.nome}
                                    </td>

                                    <td className="p-4">
                                        {empresa.telefone}
                                    </td>

                                    <td className="p-4">
                                        {empresa.cnpj}
                                    </td>

                                    <td className="p-4">
                                        {empresa.cidade}/{empresa.uf}
                                    </td>

                                    <td className="p-4">
                                        {empresa.cep}
                                    </td>

                                    <td className="p-4">
                                        <div className="flex gap-2">

                                            <button
                                                className="bg-yellow-500 text-white px-3 py-1 rounded hover:bg-yellow-600"
                                            >
                                                Editar
                                            </button>

                                            <button
                                                onClick={() =>
                                                    excluirEmpresa(
                                                        empresa.id
                                                    )
                                                }
                                                className="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700"
                                            >
                                                Excluir
                                            </button>

                                        </div>
                                    </td>
                                </tr>
                            ))}

                        </tbody>

                    </table>

                </div>
            )}
        </div>
    );
}