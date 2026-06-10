import { useEffect, useState } from "react";
import { api } from "../../api/axios";

export default function MeuEstagio() {
    const [loading, setLoading] = useState(true);
    const [estagio, setEstagio] = useState<any>(null);

    useEffect(() => {
        carregarEstagio();
    }, []);

    async function carregarEstagio() {
        try {
            const response = await api.get("/estagios/");

            const dados = response.data.results || [];

            if (dados.length > 0) {
                setEstagio(dados[0]);
            }
        } catch (error) {
            console.error("Erro ao carregar estágio:", error);
        } finally {
            setLoading(false);
        }
    }

    if (loading) {
        return (
            <div className="bg-white rounded-lg p-6">
                <p>Carregando estágio...</p>
            </div>
        );
    }

    if (!estagio) {
        return (
            <div className="bg-white rounded-lg p-6">
                <h1 className="text-3xl font-bold mb-2">
                    Meu Estágio
                </h1>

                <p className="text-gray-500">
                    Nenhum estágio encontrado.
                </p>
            </div>
        );
    }

    return (
        <div className="space-y-6">

            <div>
                <h1 className="text-3xl font-bold">
                    Meu Estágio
                </h1>

                <p className="text-gray-500 mt-1">
                    Informações do estágio cadastrado.
                </p>
            </div>

            <div className="bg-white rounded-lg border p-6 shadow-sm">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    <div>
                        <h3 className="text-sm text-gray-500">
                            Empresa
                        </h3>

                        <p className="text-xl font-semibold">
                            {estagio.empresa_nome}
                        </p>
                    </div>

                    <div>
                        <h3 className="text-sm text-gray-500">
                            ID do Estágio
                        </h3>

                        <p className="text-xl font-semibold">
                            #{estagio.idestagio}
                        </p>
                    </div>

                    <div>
                        <h3 className="text-sm text-gray-500">
                            Data de Início
                        </h3>

                        <p className="font-medium">
                            {estagio.dtinicio}
                        </p>
                    </div>

                    <div>
                        <h3 className="text-sm text-gray-500">
                            Data de Término
                        </h3>

                        <p className="font-medium">
                            {estagio.dtfim || "Não informada"}
                        </p>
                    </div>

                    <div>
                        <h3 className="text-sm text-gray-500">
                            Carga Horária Semanal
                        </h3>

                        <p className="font-medium">
                            {estagio.cargahorariasemanal} horas
                        </p>
                    </div>

                    <div>
                        <h3 className="text-sm text-gray-500">
                            TCE Vinculado
                        </h3>

                        <p className="font-medium">
                            #{estagio.tce}
                        </p>
                    </div>

                </div>
            </div>

        </div>
    );
}