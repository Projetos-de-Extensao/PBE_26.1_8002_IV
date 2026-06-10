import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { KeyRound, UserRound, Users } from "lucide-react";

export default function Login() {
    const navigate = useNavigate();
    const [matricula, setMatricula] = useState("");
    const [senha, setSenha] = useState("");
    const [role, setRole] = useState("aluno"); // Novo estado para o tipo de usuário
    const [erro, setErro] = useState(false);

    const handleLogin = (e: React.FormEvent) => {
        e.preventDefault();

        if (matricula.length > 0 && senha.length > 0) {
            // Salva o token e a role escolhida
            localStorage.setItem("token", "token-simulado-val-estagio");
            localStorage.setItem("userRole", role); 
            
            // Direciona para o painel específico baseado na role
            if (role === "aluno") navigate("/aluno");
            else if (role === "secretaria") navigate("/secretaria");
            else if (role === "coordenador") navigate("/coordenador");
            
        } else {
            setErro(true);
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
                        {/* CAMPO: TIPO DE USUÁRIO (Apenas para prototipagem) */}
                        <div>
                            <label className="block text-xs font-medium text-[var(--color-text-secondary)] mb-1.5 uppercase tracking-wider">
                                Entrar como
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-[var(--color-text-secondary)]">
                                    <Users size={18} />
                                </div>
                                <select
                                    value={role}
                                    onChange={(e) => setRole(e.target.value)}
                                    className="w-full pl-10 pr-4 py-2.5 bg-[var(--color-background-tertiary)] border border-[var(--color-border-tertiary)] rounded-lg text-[14px] text-[var(--color-text-primary)] focus:outline-none focus:ring-2 focus:ring-[#2F7FBF] transition-all appearance-none"
                                >
                                    <option value="aluno">Aluno</option>
                                    <option value="secretaria">Secretaria</option>
                                    <option value="coordenador">Coordenador</option>
                                </select>
                            </div>
                        </div>

                        {/* CAMPO: MATRÍCULA */}
                        <div>
                            <label className="block text-xs font-medium text-[var(--color-text-secondary)] mb-1.5 uppercase tracking-wider">
                                Matrícula ou E-mail
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-[var(--color-text-secondary)]">
                                    <UserRound size={18} />
                                </div>
                                <input
                                    type="text"
                                    value={matricula}
                                    onChange={(e) => { setMatricula(e.target.value); setErro(false); }}
                                    className="w-full pl-10 pr-4 py-2.5 bg-[var(--color-background-tertiary)] border border-[var(--color-border-tertiary)] rounded-lg text-[14px] text-[var(--color-text-primary)] focus:outline-none focus:ring-2 focus:ring-[#2F7FBF] transition-all"
                                    placeholder="Ex: 202400012345"
                                />
                            </div>
                        </div>

                        {/* CAMPO: SENHA */}
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
                                    onChange={(e) => { setSenha(e.target.value); setErro(false); }}
                                    className="w-full pl-10 pr-4 py-2.5 bg-[var(--color-background-tertiary)] border border-[var(--color-border-tertiary)] rounded-lg text-[14px] text-[var(--color-text-primary)] focus:outline-none focus:ring-2 focus:ring-[#2F7FBF] transition-all"
                                    placeholder="••••••••"
                                />
                            </div>
                        </div>

                        {erro && (
                            <div className="text-xs text-[#E74C3C] text-center font-medium bg-[#FCEBEB] py-2 rounded-md">
                                Preencha matrícula e senha para continuar.
                            </div>
                        )}

                        <button type="submit" className="w-full mt-2 bg-[#1B3A5C] hover:bg-[#2F7FBF] text-white font-medium py-2.5 rounded-lg transition-colors flex justify-center items-center gap-2 text-sm">
                            Entrar no sistema
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}