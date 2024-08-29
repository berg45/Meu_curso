// static/js/form_validation.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        const requiredFields = form.querySelectorAll('input[required], select[required]');
        let isValid = true;

        requiredFields.forEach(field => {
            if (!field.value) {
                isValid = false;
                field.classList.add('is-invalid');
                field.nextElementSibling.textContent = 'Este campo é obrigatório.';
            } else {
                field.classList.remove('is-invalid');
                field.nextElementSibling.textContent = '';
            }
        });

        if (!isValid) {
            event.preventDefault(); // Cancela o envio do formulário se algum campo não for válido
        }
    });
});
