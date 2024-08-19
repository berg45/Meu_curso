document.addEventListener("DOMContentLoaded", function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const bookId = urlParams.get('id');
  
    fetch("books.json")
      .then(response => response.json())
      .then(data => {
        const book = data[bookId];
        displayBookDetails(book);
      })
      .catch(error => console.error("Error fetching book details:", error));
  
    function displayBookDetails(book) {
      const bookImage = document.getElementById("book-image");
      const bookTitle = document.getElementById("book-title");
      const bookDescription = document.getElementById("book-description");
      const bookAuthor = document.getElementById("book-author");
      const bookPrice = document.getElementById("book-price");
  
      bookImage.src = book.image;
      bookTitle.textContent = book.title;
      bookDescription.textContent = book.description;
      bookAuthor.textContent = "Autor: " + book.author;
      bookPrice.textContent = "Preço: " + book.price;
  
      const buyButton = document.getElementById("buy-button");
      buyButton.addEventListener("click", function() {
        // Adicionar lógica para adicionar ao carrinho
        alert("Livro adicionado ao carrinho!");
      });
    }
  });
  
  