$(document).ready(function() {

    console.log('START');

    $('#pop').on('click', function() {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    });

    $('#pop-order').on('click', function() {
        $.ajax({
            url: '/orders/order',
            type: 'get',
            success: function(data) {
                $('#hb-order-content').html(data.html);
            }
        });
    });


//-------------------------------------------------------------------------------------


    const toggle = document.querySelector('.toggle input')

    toggle.addEventListener('click', () => {
        const onOff = toggle.parentNode.querySelector('.onoff');
        document.getElementById('icontoggler').src = toggle.checked ? "/static/img/category_toggle.png" : "/static/img/category_toggle_checked.png";
        if (document.getElementById("category-style").classList.contains('collection-template__products')) {
            document.getElementById("category-style").classList.remove('collection-template__products');
        } else {document.getElementById("category-style").classList.add('collection-template__products')}
    })

});