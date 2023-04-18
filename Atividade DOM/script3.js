// selecione o botão usando o método getElementById
var botao = document.getElementById("botao");
var limpar = document.getElementById("clean");
// adicione um evento de clique ao botão
botao.addEventListener("click", function() {
// selecione o parágrafo usando o método getElementById
var paragrafo = document.getElementById("paragrafo");

// altere o texto do parágrafo
paragrafo.textContent = "O texto deste parágrafo foi alterado!";
});

limpar.addEventListener("click", function() {
    var paragrafo = document.getElementById("paragrafo");
    paragrafo.textContent = "";

});