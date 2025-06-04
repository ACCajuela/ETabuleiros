// Atualiza a interface com os dados
function updateProfileUI(data) {
    document.getElementById('nomeCompleto').textContent = `Nome completo: ${data.nome || 'Não informado'}`;
    document.getElementById('idadeUsuario').textContent = `Idade: ${data.idade ? data.idade + ' anos' : 'Não informada'}`;
    document.getElementById('cpfUsuario').textContent = `CPF: ${formatCPF(data.cpf)}`;
    document.getElementById('enderecoUsuario').textContent = `Endereço: ${data.endereco || 'Não informado'}`;
    document.getElementById('telefoneUsuario').textContent = `Telefone: ${formatPhone(data.telefone)}`;
    document.getElementById('emailUsuario').textContent = `Email: ${data.email || 'Não informado'}`;
}

// Funções auxiliares
function formatCPF(cpf) {
    if (!cpf) return 'Não informado';
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

function formatPhone(phone) {
    if (!phone) return 'Não informado';
    const nums = phone.replace(/\D/g, '');
    return nums.replace(/(\d{2})(\d{4,5})(\d{4})/, '($1) $2-$3');
}

async function parseErrorResponse(response) {
    try {
        return await response.json();
    } catch {
        return {
            status: response.status,
            message: response.statusText
        };
    }
}

function handleProfileError(error) {
    console.error('Erro no perfil:', error);
    
    // Mostra mensagem amigável
    const errorContainer = document.createElement('div');
    errorContainer.className = 'error-message';
    errorContainer.innerHTML = `
        <p>Não foi possível carregar os dados do perfil.</p>
        <p>${error.message}</p>
        <button onclick="window.location.reload()">Tentar novamente</button>
        <button onclick="redirectToLogin()">Fazer login novamente</button>
    `;
    
    document.querySelector('.infoUser').appendChild(errorContainer);
}

// Função principal para carregar dados
async function loadProfileData(token) {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/perfil/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            const errorData = await parseErrorResponse(response);
            throw new Error(errorData.message || 'Erro ao carregar perfil');
        }

        const data = await response.json();
        updateProfileUI(data);
        
    } catch (error) {
        console.error('Erro detalhado:', error);
        throw error; // Re-lança para tratamento no catch principal
    }
}