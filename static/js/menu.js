document.addEventListener("DOMContentLoaded", function () {
    let contador = 1;

    // Botão para criar estoque
    document.getElementById("criarEstoque").addEventListener("click", function () {
        let container = document.getElementById("estoques");
        let estoque = document.createElement("div");
        estoque.classList.add("estoque");
        estoque.innerHTML = `Estoque ${contador} <button class="excluir">X</button>`;

        // Evento de clique para redirecionar ou excluir estoque
        estoque.addEventListener("click", function (event) {
            if (event.target.classList.contains("excluir")) {
                container.removeChild(estoque);
            } else {
                window.location.href = `/estoque/${contador}`;
            }
        });

        container.appendChild(estoque);
        contador++;
    });

    // Botão de logout
    document.getElementById("logout").addEventListener("click", function () {
        window.location.href = "/login";
    });
});
