$(document).ready(function() {

    $('#package-number-save').on('click', function() {
        var package_number = document.getElementById('package_number').value
        var order_id = $(this).data('order-id');
        var button_id = "order-delivered-" + order_id;
        $.ajax({
            url: $(this).data('order-id') + '/delivery-save/',
            type: 'post',
            data: 'number=' + package_number,
            success: function(data) {
                 $("#cc-order-modal").modal('hide');
                 document.getElementById(button_id).hidden = true;
                 var elem_id = "cc-order-delivery-" + order_id;
                 console.log("elem_id");
                 console.log(elem_id);
                 var container = document.getElementById(elem_id);
                 var content = "TTN: " + package_number + "<br/>"
                 container.innerHTML= content;
            }
        });
    });
});

//location.reload();