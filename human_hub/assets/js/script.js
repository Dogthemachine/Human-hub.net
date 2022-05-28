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

    $('#ordr-deliv-worldwide').on('switch-change', function (event) {
        console.log('TEST');
    });

    $(‘input[name=”DelivUkraine”]’).on(‘switchChange.bootstrapSwitch’, function (event, state) {
        console.log('TEST');
    });
  

    $('#ordr-deliv-byukraine').change(function(event){
        console.log('TEST222');
        $('#collapseDeliveryByUkraine').show();
        $('#collapseDeliveryWorldWide').hide();
    });



});