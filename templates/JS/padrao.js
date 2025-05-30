document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkFamilia");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaFamilia.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkJogosCartas");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaJogosCartas.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkJogosTabuleiro");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaJogosTabuleiros.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkQuebraCabecas");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaQuebraCabeca.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkRPG");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaRPG.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("link18");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaProibidao.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const logo = document.getElementById("logoSite");

  if (logo) {
    logo.style.cursor = "pointer";
    logo.addEventListener("click", () => {
      window.location.href = "home.html"; 
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const iconeUsuario = document.getElementById("logoUsuario");

  if (iconeUsuario) {
    iconeUsuario.style.cursor = "pointer";
    iconeUsuario.addEventListener("click", () => {
      const usuarioLogado = localStorage.getItem("usuarioLogado") === "true";

      if (usuarioLogado) {
        window.location.href = "perfil.html";
      } else {
        window.location.href = "login.html";
      }
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const btnCadastro = document.getElementById("btnCadastro");

  if (btnCadastro) {
    btnCadastro.addEventListener("click", () => {
      window.location.href = "cadastro.html";
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("edProdutoCategoria");
  familia.addEventListener("click", () => {
    window.location.href = "editProdutoCategoria.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("edFuncionarioAdm");
  familia.addEventListener("click", () => {
    window.location.href = "editFuncionarioAdm.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("edCliente");
  familia.addEventListener("click", () => {
    window.location.href = "editCliente.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("Dindin");
  familia.addEventListener("click", () => {
    window.location.href = "exportaFinanca.html";
  });
});

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

function redirectToLogin() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login/';
}
