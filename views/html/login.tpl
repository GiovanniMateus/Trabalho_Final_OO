<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="login.css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>

        % if mensagem:
            <p style="color: green;">{{ mensagem }}</p>
        % end

        <form action="/login" method="post">
            <label for="username">Nome:</label>
            <input id="username" name="username" type="text" required /><br>

            <label for="password">Senha:</label>
            <input id="password" name="password" type="password" required /><br>

            <input value="Login" type="submit" />
        </form>

        <h2>Cadastre-se</h2>
        <form action = "/cadastro" method="post">
            <label for ="new_username">Nome:</label>
            <input id="new_username" name="nome" type="text" required /><br>

            <label for="new_password">Senha:</label>
            <input> id= "new_password" name="senha" type="password" required/><br>
            
            <button type="submit">Cadastrar</button>
        </form>  
    </div>
</body>
</html>