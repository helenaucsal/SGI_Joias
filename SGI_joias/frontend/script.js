const conteudo = document.getElementById("conteudo");

document.getElementById("btnProdutos").addEventListener("click", () => {
    conteudo.innerHTML = `
        <h2 class="titulo">Lista de Produtos</h2>
        <ul class="lista">
            <li>Anel de Prata – R$ 120,00</li>
            <li>Colar de Ouro – R$ 350,00</li>
            <li>Pulseira de Pérola – R$ 200,00</li>
        </ul>
    `;
});

document.getElementById("btnEstoque").addEventListener("click", () => {
    conteudo.innerHTML = `
        <h2 class="titulo">Controle de Estoque</h2>
        <ul class="lista">
            <li>Produtos em estoque: 50 itens</li>
            <li>Itens com baixo estoque: 3</li>
        </ul>
    `;
});
