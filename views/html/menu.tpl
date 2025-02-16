<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu</title>
    <link rel="stylesheet" href="/static/css/menu.css">
    <script defer src="/static/js/menu.js"></script>
</head>
<body>
    <button id="criarEstoque">Criar Estoque</button>

    <div id="estoques">
        % for estoque in estoques:
            <div class="estoque" data-id="{{estoque['id']}}">
                <span onclick="redirecionarParaEstoque({{estoque['id']}})">{{estoque['nome']}}</span>
                <button class="excluir" onclick="excluirEstoque({{estoque['id']}})">X</button>
            </div>
        % end
    </div>

    <button id="logout" onclick="logout()">Logout</button>
</body>
</html>
