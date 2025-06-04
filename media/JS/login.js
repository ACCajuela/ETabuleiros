function redirectToLogin() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login/';
}

document.addEventListener('DOMContentLoaded', async function() {
    const token = localStorage.getItem('access_token');
    const userData = localStorage.getItem('user');
    
    // Verificação inicial de autenticação
    if (!token || !userData) {
        redirectToLogin();
        return;
    }

    try {
        // Exibe dados básicos do localStorage enquanto carrega
        displayTemporaryData(JSON.parse(userData));
        
        // Carrega dados atualizados da API
        await loadProfileData(token);
    } catch (error) {
        handleProfileError(error);
    }
});

// Função para exibir dados temporários
function displayTemporaryData(user) {
    document.getElementById('nomeCompleto').textContent = `Nome completo: ${user.nome || 'Carregando...'}`;
    document.getElementById('emailUsuario').textContent = `Email: ${user.email || 'Carregando...'}`;
}

function redirectToLogin() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login/';
}
