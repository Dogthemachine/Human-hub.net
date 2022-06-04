$(document).ready(function() {


    const cart = document.getElementById("pop")
    cart.addEventListener('click', function(event) {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    });


    const makeorder = document.getElementById("pop-order")
    makeorder.addEventListener('click', function(event) {
        $.ajax({
            url: '/orders/order',
            type: 'get',
            success: function(data) {
                $('#hb-order-content').html(data.html);
            }
        });
    });


    const toggle = document.querySelector('.toggle input')
    toggle.addEventListener('click', () => {
        const onOff = toggle.parentNode.querySelector('.onoff');
        document.getElementById('icontoggler').src = toggle.checked ? "/static/img/category_toggle.png" : "/static/img/category_toggle_checked.png";
        if (document.getElementById("category-style").classList.contains('collection-template__products')) {
            document.getElementById("category-style").classList.remove('collection-template__products');
            document.getElementById("category-style").classList.add('collection-template--column-view')
        } else {document.getElementById("category-style").classList.remove('collection-template--column-view')
            document.getElementById("category-style").classList.add('collection-template__products')
            }
    })

});