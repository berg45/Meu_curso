document.getElementById("loginForm").onsubmit = function(event) {
    event.preventDefault(); // Impede o envio do formulário
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    alert(`Nome: ${username}\nSenha: ${password}`); // Exibe os dados (para teste)
    const modal = bootstrap.Modal.getInstance(document.getElementById('modal'));
    modal.hide(); // Fecha o modal após o envio
};
