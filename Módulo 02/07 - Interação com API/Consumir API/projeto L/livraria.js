document.addEventListener("DOMContentLoaded", function() {
    // Carregar os livros quando a página for carregada
    loadBooks();

    // Adicionar evento de clique ao botão de busca
    const searchButton = document.getElementById("search-button");
    searchButton.addEventListener("click", function() {
      const searchInput = document.getElementById("search-input").value.toLowerCase();
      searchBooks(searchInput);
    });

    // Adicionar evento de pressionar Enter ao campo de busca
    const searchInput = document.getElementById("search-input");
    searchInput.addEventListener("keypress", function(e) {
      if (e.key === 'Enter') {
        const searchInput = document.getElementById("search-input").value.toLowerCase();
        searchBooks(searchInput);
      }
    });

    // Carregar livros a partir do arquivo JSON
    function loadBooks() {
      fetch("books.json")
        .then(response => response.json())
        .then(data => displayBooks(data))
        .catch(error => console.error("Error fetching books:", error));
    }

    // Exibir todos os livros ou filtrar por termo de pesquisa
    function searchBooks(searchTerm) {
      fetch("books.json")
        .then(response => response.json())
        .then(data => {
          const filteredBooks = data.filter(book => {
            return book.title.toLowerCase().includes(searchTerm) || book.author.toLowerCase().includes(searchTerm);
          });
          displayBooks(filteredBooks);
        })
        .catch(error => console.error("Error searching books:", error));
    }

    // Exibir os livros na página
    function displayBooks(books) {
      const bookList = document.getElementById("book-list");
      bookList.innerHTML = ""; // Limpar a lista antes de exibir os livros

      books.forEach(book => {
        const bookDiv = document.createElement("div");
        bookDiv.classList.add("book");
        bookDiv.innerHTML = `
          <img src="${book.image}" alt="${book.title}">
          <h2>${book.title}</h2>
          <p>${book.author}</p>
          <p>${book.price}</p>
        `;
        bookList.appendChild(bookDiv);
      });
    }

    // Adicionar funcionalidade ao menu horizontal
    const navLinks = document.querySelectorAll("nav ul li a");
    navLinks.forEach(link => {
      link.addEventListener("click", function(event) {
        event.preventDefault(); // Impedir o comportamento padrão de navegação

        const category = this.textContent.toLowerCase(); // Obter o texto do link
        if (category === "home") {
          loadBooks(); // Se clicar em "Home", carregar todos os livros
        } else {
          filterBooksByCategory(category); // Caso contrário, filtrar os livros pela categoria selecionada
        }
      });
    });

    // Filtrar os livros pela categoria selecionada
    function filterBooksByCategory(category) {
      fetch("books.json")
        .then(response => response.json())
        .then(data => {
          const filteredBooks = data.filter(book => {
            return book.category.toLowerCase() === category;
          });
          displayBooks(filteredBooks);
        })
        .catch(error => console.error("Error filtering books:", error));
    }
  });