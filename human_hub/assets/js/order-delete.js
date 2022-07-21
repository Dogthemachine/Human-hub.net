$(document).ready(function() {

    $('#order-delete').on('click', function() {
        var order_id = $(this).data('order-id');
        $.ajax({
            url: $(this).data('order-id') + '/order-delete/',
            type: 'post',
            data: 'order_id=' + order_id,
            success: function(data) {
                location.reload();
            }
        });
    });
});

