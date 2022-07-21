$(document).ready(function() {

    $('.cc-order-link').on('click', function() {
        $.ajax({
            url: $(this).data('order-id') + '/info/',
            type: 'get',
            success: function(data) {
                $('#cc-order-modal .modal-title').html(data.title);
                $('#cc-order-modal .modal-body').html(data.html);
            }
        });
    });

    $('.order-packed').on('click', function() {
        button_id = "order-packed-" + $(this).data('order-id');
        $.ajax({
            url: $(this).data('order-id') + '/packed/',
            type: 'get',
            success: function(data) {
                console.log(button_id);
                document.getElementById(button_id).hidden = true;
            }
        });
    });

    $('.delivery-link').on('click', function() {
        $.ajax({
            url: $(this).data('order-id') + '/delivery/',
            type: 'get',
            success: function(data) {
                $('#cc-order-modal .modal-title').html(data.title);
                $('#cc-order-modal .modal-body').html(data.html);
            }
        });
    });


    $('.payment-link').on('click', function() {
        $.ajax({
            url: $(this).data('order-id') + '/payed/',
            type: 'get',
            success: function(data) {
                $('#cc-order-modal .modal-title').html(data.title);
                $('#cc-order-modal .modal-body').html(data.html);
            }
        });
    });

});