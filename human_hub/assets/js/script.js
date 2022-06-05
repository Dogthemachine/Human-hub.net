$(document).ready(function() {


    const cart = document.getElementById("show-cart-modal")
    cart.addEventListener('click', showCarModal);

    function showCarModal() {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    };


    const makeorder = document.getElementById("show-order-modal");
    makeorder.addEventListener('click', showOrderModal);

    function showOrderModal() {
        $.ajax({
            url: '/orders/order',
            type: 'get',
            success: makeorderSuccess
        });
    };

    function makeorderSuccess(data) {
        $('#hb-order-content').html(data.html);

        const worldwide = document.getElementById("ordr-deliv-worldwide");
        const novpostobranch = document.getElementById("ordr-deliv-novpostobranch");
        const novpostodoor = document.getElementById("ordr-deliv-novpostodoor");
        const urkpostobranch = document.getElementById("ordr-deliv-urkpostobranch");
        const urkpostodoor = document.getElementById("ordr-deliv-urkpostodoor");
        const justintobranch = document.getElementById("ordr-deliv-justintobranch");

        const collapsing = document.getElementById("collapseDeliveryInfo");

        worldwide.addEventListener('click', () => {
            if (worldwide.checked) {
                novpostobranch.checked = false
                novpostodoor.checked = false
                urkpostobranch.checked = false
                urkpostodoor.checked = false
                justintobranch.checked = false
            };
        });
        novpostobranch.addEventListener('click', () => {
            if (novpostobranch.checked) {
                worldwide.checked = false
                novpostodoor.checked = false
                urkpostobranch.checked = false
                urkpostodoor.checked = false
                justintobranch.checked = false
            };
        });
        novpostodoor.addEventListener('click', () => {
            if (novpostodoor.checked) {
                novpostobranch.checked = false
                worldwide.checked = false
                urkpostobranch.checked = false
                urkpostodoor.checked = false
                justintobranch.checked = false
            };
        });
        urkpostobranch.addEventListener('click', () => {
            if (urkpostobranch.checked) {
                novpostobranch.checked = false
                novpostodoor.checked = false
                worldwide.checked = false
                urkpostodoor.checked = false
                justintobranch.checked = false
            };
        });
        urkpostodoor.addEventListener('click', () => {
            if (urkpostodoor.checked) {
                novpostobranch.checked = false
                novpostodoor.checked = false
                urkpostobranch.checked = false
                worldwide.checked = false
                justintobranch.checked = false
            };
        });
        justintobranch.addEventListener('click', () => {
            if (justintobranch.checked) {
                novpostobranch.checked = false
                novpostodoor.checked = false
                urkpostobranch.checked = false
                urkpostodoor.checked = false
                worldwide.checked = false
            };
        });
    };


    const toggle = document.querySelector('.toggle input');
    toggle.addEventListener('click', () => {
        const onOff = toggle.parentNode.querySelector('.onoff');
        document.getElementById('icontoggler').src = toggle.checked ? "/static/img/category_toggle.png" : "/static/img/category_toggle_checked.png";
        if (document.getElementById("category-style").classList.contains('collection-template__products')) {
            document.getElementById("category-style").classList.remove('collection-template__products');
            document.getElementById("category-style").classList.add('collection-template--column-view')
        } else {document.getElementById("category-style").classList.remove('collection-template--column-view')
            document.getElementById("category-style").classList.add('collection-template__products')
            }
    });




});