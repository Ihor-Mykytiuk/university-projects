function toggleOverlay() {
    $("#overlay").toggleClass("hidden");

    if ($("#overlay").hasClass("hidden")) {
        $('body').css('overflow', 'auto');
    }
    else {
        $('body').css('overflow', 'hidden');
    }
}
function openForm(formUrl) {
    $('.form-container').load(formUrl);
    toggleOverlay();
}
function closeForm() {
    $('.form-container').empty();
    toggleOverlay();
}
$(document).ready(function() {
    $('#registration-button').click(function() {
        openForm('http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/templates/register_form.html');
    });

    $('#login-button').click(function() {
        openForm('http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/templates/login_form.html');
    });

    $('#password-recovery-button').click(function() {
        openForm('http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/templates/forgot_password_form.html');
    });

    $('#new-product-button').click(function() {
        openForm('http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/templates/add_product_form.html');
    });

    
    $('.form-container').on('click', '.total-sum__close, .user-form__close-button', function() {
        closeForm();
    });

    $(document).on('submit', '#register-form', function() {
        let form = $(this);
        let formData = {
            name: {
                value: form.find('input[name="name"]').val(),
                pattern: /^[A-Z][a-z]{1,20}$/,
                message: 'Ім\'я на латині з великої букви'
            },
            surname: {
                value: form.find('input[name="surname"]').val(),
                pattern: /^[A-Z][a-z]{1,20}$/,
                message: 'Прізвище на латині з великої букви'
            },
            email: {
                value: form.find('input[name="email"]').val(),
                pattern: /^[a-zA-Z0-9_.+-]+@pnu.edu.ua$/,
                message: 'Email домену @pnu.edu.ua'
            },
            password: {
                value: form.find('input[name="password"]').val(),
                pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_@#$%^&!?\*]).{6,}$/,
                message: 'Пароль повинен містити мінімум 6 символів, велику літеру, цифру та спецсимвол'
            },
            password_confirm: {
                value: form.find('input[name="password_confirm"]').val(),
                pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_@#$%^&!?\*]).{6,}$/,
                message: 'Пароль повинен містити мінімум 6 символів, велику літеру, цифру та спецсимвол'
            },
            role: {
                value: form.find('input[name="role"]:checked').val(),
                pattern: /^Seller|Buyer$/,
                message: 'Оберіть категорію'
            }
        }
        let isValid = true;
        $.each(formData, function(key, data) {
            if (data.value === "") {
                form.find('input[name="' + key + '"]').addClass('invalid-input');
                form.find('#' + key + '-message').text('Заповніть поле');
                isValid = false;
            }
            else if ((!data.pattern.test(data.value)) ) {
                form.find('input[name="' + key + '"]').addClass('invalid-input');
                form.find('#' + key + '-message').text(data.message);
                isValid = false;
            }
            else {
                form.find('input[name="' + key + '"]').removeClass('invalid-input');
                form.find('#' + key + '-message').empty();
            }
        });
        
        if (formData.password.value !== formData.password_confirm.value && formData.password.value !== "" && formData.password_confirm.value !== "") {
            form.find('input[name="password"], input[name="password_confirm"]').addClass('invalid-input');
            form.find('#password_confirm-message').text('Паролі не співпадають');
            isValid = false;
        }
        if (!isValid) {
            form.find('#register-result').text('Заповніть всі поля');
            return false;
        }

        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_register_handler.php',
            type: 'POST',
            data: form.serialize(),
            success: function(data) {
                $('#register-result').text(data);
            }
        });
        return false;
    });

    $(document).on('submit', '#login-form', function() {
        let form = $(this);
        let isValid = true;
        
        form.find('input').each(function() {
            if ($(this).val() === '') {
                $(this).addClass('invalid-input');
                isValid = false;
            }
            else {
                $(this).removeClass('invalid-input');
            }
        });

        if (form.find('input[name="role"]:checked').length === 0) {
            isValid = false;
        }

        if (!isValid) {
            form.find('#login-result').text('Заповніть всі поля');
            return false;
        }
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_login_handler.php',
            type: 'POST',
            data: form.serialize(),
            success: function(data) {
                if (data == 'success') {
                    location.reload();
                }
                else {
                    form.find('#login-result').text(data);
                }
            }
        });
        return false;
    });

    $(document).on('submit', '#forgot-password-form', function() {
        let form = $(this);
        let isValid = true;
        form.find('input').each(function() {
            if ($(this).val() === '') {
                $(this).addClass('invalid-input');
                isValid = false;
            }
            else {
                $(this).removeClass('invalid-input');
            }
            
        });
        
        if (form.find('input[name="role[]"]:checked').length === 0) {
            isValid = false;
        }
        if (!isValid) {
            $('#forgot-password-result').text('Заповніть всі поля');
            return false;
        }
        
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_forgot_password_handler.php',
            type: 'POST',
            data: form.serialize(),
            dataType: 'json',
            success: function(response) {
                if (response.length === 0) {
                    $('#forgot-password-result').empty().text('Користувача з таким email не знайдено');
                    return;
                }
                let table = $('<table>');
                let headerRow = $('<tr>').append($('<th>').text('Логін'), $('<th>').text('Пароль'));
                table.append(headerRow);
                $.each(response, function(index, user) {
                    let row = $('<tr>').append($('<td>').text(user.email), $('<td>').text(user.password));
                    table.append(row);
                });
                $('#forgot-password-result').empty().append(table);
            },
            error: function() {
                alert('Помилка');
            }
            
        });
        return false;
    });

    $(document).on('click', '#logout-button', function() {
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_logout_handler.php',
            success: function() {
            window.location.href = 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/index.php';
            },
            error: function() {
            alert('Помилка');
            }
        });
    });

    $(document).on('submit', '#add-product-form', function() {
        let form = $(this);
        let formData = new FormData(form[0]);
        $.ajax({
            url: 'handlers/mykytiuk_new_product_handler.php',
            type: 'POST',
            data: formData,
            success: function(data) {
                if (data === 'success') {
                    location.reload();
                }
                else {
                    form.find('#add-product-result').text(data);
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    });

    $(document).on('click', '#audit-button', function() {
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_audit_handler.php',
            type: 'POST',
            success: function(data) {
                toggleOverlay();
                $('.form-container').html(data);
            }
        });
    });

    $('#cart-button').on('click', function() {
        $('.cart').toggleClass('open');
        if ($('.cart').hasClass('open')) {
            loadCartContent();
            toggleOverlay();
        } 
    });

    $('.cart').on('click', '.cart-item__remove-button', function() {
        let productId = $(this).data('id');
        removeCartItem(productId);
    });

    function loadCartContent() {
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/pages/mykytiuk_card.php',
            type: 'POST',
            success: function(data) {
                $('.cart').html(data);
            },
            error: function() {
                $('.cart').html('Error loading cart content');
            }
        });
    }

    function removeCartItem(productId) {
        $.ajax({
            url: 'http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/handlers/mykytiuk_remove_cart_item_handler.php',
            type: 'POST',
            data: { product_id: productId },
            success: function(data) {
                if (data === 'success') {
                    loadCartContent();
                }
            }
        });
    }
    
    $('.cart').on('click', '.cart__close-button', function() {
        $('.cart').removeClass('open');
        $("#overlay").addClass("hidden");
        $('body').css('overflow', 'auto');
    });
});