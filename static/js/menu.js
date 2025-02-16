document.addEventListener("DOMContentLoaded", async function () {
    let container = document.getElementById("estoques");

    // Carregar estoques do servidor
    async function carregarEstoques() {
        let response = await fetch("/api/estoques");
        let estoques = await response.json();
        container.innerHTML = ""; // Limpa o container antes de renderizar

        estoques.forEach(estoque => {
            criarElementoEstoque(estoque.id, estoque.nome);
        });
    }

    // Criar um novo estoque
    document.getElementById("criarEstoque").addEventListener("click", async function () {
        let response = await fetch("/api/estoques", { method: "POST" });
        if (response.ok) {
            let novoEstoque = await response.json();
            criarElementoEstoque(novoEstoque.id, novoEstoque.nome);
        }
    });

    // Criar um elemento de estoque na tela
    function criarElementoEstoque(id, nome) {
        let estoque = document.createElement("div");
        estoque.classList.add("estoque");
        estoque.innerHTML = `${nome} <button class="excluir" data-id="${id}">X</button>`;

        estoque.addEventListener("click", function (event) {
            if (event.target.classList.contains("excluir")) {
                excluirEstoque(event.target.getAttribute("data-id"), estoque);
            } else {
                window.location.href = `/estoque/${id}`;
            }
        });

        container.appendChild(estoque);
    }

    // Excluir estoque
    async function excluirEstoque(id, elemento) {
        let response = await fetch(`/api/estoques/${id}`, { method: "DELETE" });
        if (response.ok) {
            elemento.remove();
        }
    }

    // Logout do usuário
    document.getElementById("logout").addEventListener("click", function () {
        fetch("/logout", { method: "POST" }).then(() => {
            window.location.href = "/login";
        });
    });

    // Inicializar carregando estoques
    await carregarEstoques();
});

