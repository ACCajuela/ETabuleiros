//Puxando API de add categoria

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Verifica se o cookie começa com o nome desejado
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

  
    document.getElementById('btnConfirmarCategoria').addEventListener('click', function () {
    const nomeCategoria = document.getElementById('nomeCategoriaInput').value;

    fetch('http://127.0.0.1:8000/api/criar-categoria/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            'nome_categoria': nomeCategoria
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
        return response.text(); // Recebe como texto primeiro
    })
    .then(text => {
        try {
            const data = JSON.parse(text); // Tenta converter para JSON
            if (data.status === 'success') {
                alert('Categoria criada com sucesso!');
                esconderPopupCategoria();
            } else {
                alert('Erro: ' + (data.message || 'Resposta desconhecida da API'));
            }
        } catch (e) {
            console.error('Resposta não é um JSON válido:', text);
            alert('Erro: resposta inesperada do servidor.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao criar a categoria');
    });
});
