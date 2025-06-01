let authToken = localStorage.getItem('authToken') || null;
let pendingCategoryData = null;

// Fluxo principal de adição de categoria
async function adicionarCategoria() {
    const inputNome = document.querySelector('#popupCategoria input[type="text"]');
    const nomeCategoria = inputNome.value.trim();
    
    if (!nomeCategoria) {
        alert('Por favor, insira um nome para a categoria');
        return;
    }

    // Se não autenticado, armazena os dados e pede autenticação
    if (!authToken) {
        pendingCategoryData = nomeCategoria;
        mostrarPopupSeguranca();
        setupAuthObserver();
        return;
    }

    // Se já autenticado, cria a categoria diretamente
    await criarCategoria(nomeCategoria);
}

// Configura observer para o popup de autenticação
function setupAuthObserver() {
    const popup = document.getElementById('popupSeguranca');
    const observer = new MutationObserver(async (mutations) => {
        if (popup.style.display === 'none' && authToken && pendingCategoryData) {
            observer.disconnect();
            await criarCategoria(pendingCategoryData);
            pendingCategoryData = null;
        }
    });
    observer.observe(popup, { attributes: true, attributeFilter: ['style'] });
}

// Função dedicada para criar a categoria
async function criarCategoria(nomeCategoria) {
    const botaoConfirmar = document.querySelector('#popupCategoria button');
    const textoOriginal = botaoConfirmar.textContent;
    
    try {
        botaoConfirmar.textContent = 'Enviando...';
        botaoConfirmar.disabled = true;

        const response = await fetch('http://127.0.0.1:8000/api/categorias/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`,
            },
            body: JSON.stringify({
                nome_categoria: nomeCategoria
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            
            if (response.status === 401) {
                // Token inválido - prepara para reautenticação
                authToken = null;
                localStorage.removeItem('authToken');
                pendingCategoryData = nomeCategoria;
                mostrarPopupSeguranca();
                setupAuthObserver();
                throw new Error('Sessão expirada. Por favor, faça login novamente.');
            }
            
            throw new Error(errorData.nome_categoria?.[0] || errorData.message || 'Erro ao criar categoria');
        }

        // Sucesso - limpa e fecha
        alert('Categoria adicionada com sucesso!');
        document.querySelector('#popupCategoria input').value = '';
        esconderPopupCategoria();
        
    } catch (error) {
        console.error('Erro:', error);
        alert(error.message);
    } finally {
        botaoConfirmar.textContent = textoOriginal;
        botaoConfirmar.disabled = false;
    }
}

// Função de login (mantida conforme seu código)
async function fazerLoginAdmin() {
    // ... (implementação existente)
    // Ao autenticar com sucesso:
    authToken = data.token; // Armazena o novo token
    localStorage.setItem('authToken', authToken);
    return true;
}

// Event listeners (mantidos conforme seu código)
document.addEventListener('DOMContentLoaded', function() {
    // ... (configuração existente de listeners)
});

//Criação de produto



//login
