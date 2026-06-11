import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { KeyRound, UserRound, Loader2 } from "lucide-react";
import { login } from "../../api/auth";

export default function Login() {
    const navigate = useNavigate();

    const [matricula, setMatricula] = useState("");
    const [senha, setSenha] = useState("");
    const [erro, setErro] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setErro("");

        if (!matricula || !senha) {
            setErro("Preencha matrícula e senha para continuar.");
            return;
        }

        try {
            setLoading(true);

            const responseData = await login(matricula, senha);

            // DEBUG
            console.log("===== LOGIN RESPONSE =====");
            console.log(responseData);

            const token =
                responseData.token ||
                responseData.access ||
                responseData.key;

            const role =
                responseData.role ||
                responseData.tipo_usuario;

            console.log("TOKEN:", token);
            console.log("ROLE:", role);

            if (token) {
                localStorage.setItem("token", token);

                if (role) {
                    localStorage.setItem("userRole", role);
                    console.log("Role salva:", role);
                } else {
                    console.warn(
                        "A API não devolveu a role. Entrando como aluno por padrão."
                    );
                    localStorage.setItem("userRole", "aluno");
                }

                console.log("Token salvo:", token);

                if (role === "secretaria") {
                    navigate("/secretaria");
                } else if (role === "coordenador") {
                    navigate("/coordenador");
                } else {
                    navigate("/aluno");
                }
            } else {
                setErro("Formato de token não reconhecido pela API.");
            }
        } catch (error: any) {
            console.error("Erro na requisição de login:", error);

            if (error.response) {
                console.error("Resposta da API:", error.response.data);
            }

            setErro(
                "Credenciais inválidas. Verifique seus dados e tente novamente."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-[#1B3A5C] flex flex-col justify-center items-center p-4">
            <div className="mb-8 text-center">
                <h1 className="text-3xl font-medium text-white tracking-wide">
                    Val Estágio
                </h1>
                <p className="text-sm text-white/60 mt-2">
                    Sistema de gestão acadêmica
                </p>
            </div>

            <div className="bg-white w-full max-w-md rounded-2xl shadow-xl overflow-hidden">
                <div className="p-8">
                    <h2 className="text-xl font-medium text-center mb-6">
                        Acesse sua conta
                    </h2>

                    <form
                        onSubmit={handleLogin}
                        className="flex flex-col gap-5"
                    >
                        <div>
                            <label className="block text-xs font-medium mb-1.5 uppercase tracking-wider">
                                Matrícula (Username)
                            </label>

                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <UserRound size={18} />
                                </div>

                                <input
                                    type="text"
                                    value={matricula}
                                    onChange={(e) => {
                                        setMatricula(e.target.value);
                                        setErro("");
                                    }}
                                    disabled={loading}
                                    className="w-full pl-10 pr-4 py-2.5 border rounded-lg"
                                    placeholder="Digite sua matrícula"
                                />
                            </div>
                        </div>

                        <div>
                            <label className="block text-xs font-medium mb-1.5 uppercase tracking-wider">
                                Senha
                            </label>

                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <KeyRound size={18} />
                                </div>

                                <input
                                    type="password"
                                    value={senha}
                                    onChange={(e) => {
                                        setSenha(e.target.value);
                                        setErro("");
                                    }}
                                    disabled={loading}
                                    className="w-full pl-10 pr-4 py-2.5 border rounded-lg"
                                    placeholder="••••••••"
                                />
                            </div>
                        </div>

                        {erro && (
                            <div className="text-xs text-red-600 text-center font-medium bg-red-100 py-2.5 rounded-md">
                                {erro}
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full mt-2 bg-[#1B3A5C] hover:bg-[#2F7FBF] text-white font-medium py-2.5 rounded-lg flex justify-center items-center gap-2"
                        >
                            {loading ? (
                                <>
                                    <Loader2
                                        size={18}
                                        className="animate-spin"
                                    />
                                    Autenticando...
                                </>
                            ) : (
                                "Entrar"
                            )}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}