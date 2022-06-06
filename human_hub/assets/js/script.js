$(document).ready(function() {


    const cart = document.getElementById("show-cart-modal");
    cart.addEventListener('click', showCarModal);

    const choose_size = document.getElementsByClassName("size_button");
    for (var i = 0; i< choose_size.length; i++) {
        choose_size[i].onclick = addSizeToCart
    };

    function showCarModal() {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    };

    function addSizeToCart() {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    };


//-----------   MAKE ORDER MODAL WINDOW     -----------

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

        const WorldWide = document.getElementById("collapseDeliveryWorldWide");
        const NovaPoshtaToBranch = document.getElementById("collapseDeliveryNovaPoshtaToBranch");
        const NovaPoshtaToDoor = document.getElementById("collapseDeliveryNovaPoshtaToDoor");
        const UkrposhtaToBranch = document.getElementById("collapseDeliveryUkrposhtaToBranch");
        const UkrposhtaToDoor = document.getElementById("collapseDeliveryUkrposhtaToDoor");
        const JustinToBranch = document.getElementById("collapseDeliveryJustinToBranch");

        NovaPoshtaToBranch.style.display = 'none';
        NovaPoshtaToDoor.style.display = 'none';
        UkrposhtaToBranch.style.display = 'none';
        JustinToBranch.style.display = 'none';
        UkrposhtaToDoor.style.display = 'none';
        WorldWide.style.display = 'none';

        worldwide.addEventListener('click', () => {
            if (worldwide.checked) {
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                WorldWide.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            WorldWide.style.display = 'none';
            };
        });
        novpostobranch.addEventListener('click', () => {
            if (novpostobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'block';
                worldwide.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            NovaPoshtaToBranch.style.display = 'none';
            };
        });
        novpostodoor.addEventListener('click', () => {
            WorldWide.style.display = 'none';
            NovaPoshtaToBranch.style.display = 'none';
            UkrposhtaToBranch.style.display = 'none';
            JustinToBranch.style.display = 'none';
            UkrposhtaToDoor.style.display = 'none';
            NovaPoshtaToDoor.style.display = 'block';
            if (novpostodoor.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'block';
                novpostobranch.checked = false;
                worldwide.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            NovaPoshtaToDoor.style.display = 'none';
            };
        });
        urkpostobranch.addEventListener('click', () => {
            if (urkpostobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                worldwide.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            UkrposhtaToBranch.style.display = 'none';
            };
        });
        urkpostodoor.addEventListener('click', () => {
            if (urkpostodoor.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                worldwide.checked = false;
                justintobranch.checked = false;
                } else {
            UkrposhtaToDoor.style.display = 'none';
            };
        });
        justintobranch.addEventListener('click', () => {
            if (justintobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                JustinToBranch.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                worldwide.checked = false;
                } else {
            JustinToBranch.style.display = 'none';
            };
        });
   };

    const checkout = document.getElementById("pop-order-checkout");
    checkout.addEventListener('click', () => {
        if (worldwide.checked) {
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (novpostobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (novpostodoor.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (urkpostobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (urkpostodoor.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (justintobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
        };
    });
//-----------   MAKE ORDER MODAL WINDOW     -----------


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