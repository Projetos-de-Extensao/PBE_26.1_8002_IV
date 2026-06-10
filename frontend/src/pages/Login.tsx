import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { KeyRound, UserRound, Loader2 } from "lucide-react";
import { login } from "../api/auth";

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
            
            // Faz a requisição para o Django
            const responseData = await login(matricula, senha);

            const token = responseData.token || responseData.access;
            
            // AGORA QUEM MANDA É A API: O backend precisa devolver o cargo na resposta do login
            // Exemplo esperado do backend: { token: "123...", role: "secretaria" }
            const role = responseData.role || responseData.tipo_usuario;

            if (token) {
                localStorage.setItem("token", token);
                
                // Salva a role verdadeira que veio do banco de dados
                if (role) {
                    localStorage.setItem("userRole", role);
                } else {
                    // Fallback de segurança se a API ainda não estiver a enviar a role
                    console.warn("A API não devolveu a role. Entrando como aluno por padrão.");
                    localStorage.setItem("userRole", "aluno");
                }
                
                // Direciona para o painel correto com base na resposta do backend
                if (role === "secretaria") navigate("/secretaria");
                else if (role === "coordenador") navigate("/coordenador");
                else navigate("/aluno"); // Padrão

            } else {
                setErro("Formato de token não reconhecido pela API.");
            }

        } catch (error: any) {
            console.error("Erro na requisição de login:", error);
            setErro("Credenciais inválidas. Verifique os seus dados e tente novamente.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-[#1B3A5C] flex flex-col justify-center items-center p-4">
            <div className="mb-8 text-center">
                <h1 className="text-3xl font-medium text-white tracking-wide">Val Estágio</h1>
                <p className="text-sm text-white/60 mt-2">Sistema de gestão acadêmica</p>
            </div>

            <div className="bg-white w-full max-w-md rounded-2xl shadow-xl overflow-hidden">
                <div className="p-8">
                    <h2 className="text-xl font-medium text-[var(--color-text-primary)] mb-6 text-center">
                        Acesse sua conta
                    </h2>

                    <form onSubmit={handleLogin} className="flex flex-col gap-5">
                        
                        {/* CAMPO DE MATRÍCULA */}
                        <div>
                            <label className="block text-xs font-medium text-[var(--color-text-secondary)] mb-1.5 uppercase tracking-wider">
                                Matrícula (Username)
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-[var(--color-text-secondary)]">
                                    <UserRound size={18} />
                                </div>
                                <input
                                    type="text"
                                    value={matricula}
                                    onChange={(e) => { setMatricula(e.target.value); setErro(""); }}
                                    disabled={loading}
                                    className="w-full pl-10 pr-4 py-2.5 bg-[var(--color-background-tertiary)] border border-[var(--color-border-tertiary)] rounded-lg text-[14px] text-[var(--color-text-primary)] focus:outline-none focus:ring-2 focus:ring-[#2F7FBF] transition-all disabled:opacity-50"
                                    placeholder="Ex: 202400012345"
                                />
                            </div>
                        </div>

                        {/* CAMPO DE SENHA */}
                        <div>
                            <label className="block text-xs font-medium text-[var(--color-text-secondary)] mb-1.5 uppercase tracking-wider">
                                Senha
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-[var(--color-text-secondary)]">
                                    <KeyRound size={18} />
                                </div>
                                <input
                                    type="password"
                                    value={senha}
                                    onChange={(e) => { setSenha(e.target.value); setErro(""); }}
                                    disabled={loading}
                                    className="w-full pl-10 pr-4 py-2.5 bg-[var(--color-background-tertiary)] border border-[var(--color-border-tertiary)] rounded-lg text-[14px] text-[var(--color-text-primary)] focus:outline-none focus:ring-2 focus:ring-[#2F7FBF] transition-all disabled:opacity-50"
                                    placeholder="••••••••"
                                />
                            </div>
                        </div>

                        {erro && (
                            <div className="text-xs text-[#E74C3C] text-center font-medium bg-[#FCEBEB] py-2.5 rounded-md border border-[#E74C3C]/20">
                                {erro}
                            </div>
                        )}

                        <button 
                            type="submit" 
                            disabled={loading}
                            className="w-full mt-2 bg-[#1B3A5C] hover:bg-[#2F7FBF] text-white font-medium py-2.5 rounded-lg transition-colors flex justify-center items-center gap-2 text-sm disabled:bg-[#1B3A5C]/70 disabled:cursor-not-allowed"
                        >
                            {loading ? <><Loader2 size={18} className="animate-spin" /> Autenticando...</> : "Entrar no sistema"}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}