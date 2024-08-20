
const chessboard = document.getElementById('chessboard');
const botao = document.getElementById('alterar');
const bvoltar = document.getElementById('voltar');
const arcoires = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3'];

function criarTabuleiro(){
    for( let row = 0; row < 8; row++ ){
        for(let col = 0; col < 8; col++){
            const square = document.createElement('div');
            square.classList.add('square');
            const squareNumber = row * 8 + col + 1; // Número único do quadrado
            square.dataset.number = squareNumber; // Armazena o número no atributo data
            if((row + col) % 2 === 0 ){
                square.classList.add('white');
            } else {
                square.classList.add('black');
            }
            square.addEventListener('click', () => {
                limparNumeros(); // Limpa todos os números
                square.innerText = square.dataset.number; // Exibe o número apenas no quadrado clicado
            });
            chessboard.appendChild(square);
        }
    }
}

function limparNumeros(){
    const squares = document.querySelectorAll('.square');
    squares.forEach(square => {
        square.innerText = ''; // Limpa o texto de todos os quadrados
    });
}

function alterarCores(){
    const blacksquare = document.querySelectorAll('.black');
    blacksquare.forEach((square, index) => {
        square.style.backgroundColor = arcoires[index % arcoires.length];
    });
}

function voltarCoresOriginais(){
    const blacksquare = document.querySelectorAll('.black');
    blacksquare.forEach((square) => {
        square.style.backgroundColor = 'black';
    });
}

criarTabuleiro();
botao.addEventListener('click', alterarCores);
bvoltar.addEventListener('click', voltarCoresOriginais);

