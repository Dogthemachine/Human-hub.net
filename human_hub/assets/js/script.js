$(document).ready(function() {

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

    $('#ordr-deliv-worldwide').change(function(){
        console.log('TEST');
        $('#collapseDeliveryByUkraine').hide();
        $('#collapseDeliveryWorldWide').show();
    });


    $('#ordr-deliv-byukraine').change(function(){
        console.log('TEST222');
        $('#collapseDeliveryByUkraine').show();
        $('#collapseDeliveryWorldWide').hide();
    });



});