$(document).ready(function() {

    var item_id = document.getElementsByClassName("item-modal-sizes")[0].id;
    var modal_sizes_buttons = document.getElementsByClassName("size-class");
    var i;
    for (i = 0; i < modal_sizes_buttons.length; i++) {
        modal_sizes_buttons[i].addEventListener("click", function() {
            size_item_id = $(this).data('id');
            $.ajax({
                url: '/orders/cart/' + item_id + '/' + size_item_id + '/add/',
                type: 'post',
                success: function(data) {
                if (data.success) {
                $("#hb-cart-total").html(data.cart_amount);
                size_item_id = 0;
                location.reload();
                } else {document.getElementById("must-choose").hidden = false}
                },
            });
        });
    };


});