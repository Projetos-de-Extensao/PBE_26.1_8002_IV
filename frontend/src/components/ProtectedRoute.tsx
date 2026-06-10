import { Navigate } from "react-router-dom";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export default function ProtectedRoute({
  children,
}: ProtectedRouteProps) {
  const token = localStorage.getItem("token");

  // Se não estiver logado, volta para o login
  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}