$(document).ready(function() {

//-----------   CATEGORY TOGGLER     -----------
    var all_item_names = document.getElementsByClassName("kuku");
    var i;
    for (i = 0; i < all_item_names.length; i++) {
        all_item_names[i].classList.remove('item-name-in-category-page');
        all_item_names[i].classList.add('item-name-in-category-page-two-columns');
        };


    const toggle = document.querySelector('.toggle input');
    toggle.addEventListener('click', () => {
        const onOff = toggle.parentNode.querySelector('.onoff');
        document.getElementById('icontoggler').src = toggle.checked ? "/static/img/category_toggle.png" : "/static/img/category_toggle_checked.png";
        if (document.getElementById("category-style").classList.contains('collection-template__products')) {
            document.getElementById("category-style").classList.remove('collection-template__products');
            document.getElementById("category-style").classList.add('collection-template--column-view');
            for (i = 0; i < all_item_names.length; i++) {
                all_item_names[i].classList.remove('item-name-in-category-page-two-columns');
                all_item_names[i].classList.add('item-name-in-category-page');
                };
            } else {
                document.getElementById("category-style").classList.remove('collection-template--column-view');
                document.getElementById("category-style").classList.add('collection-template__products');
                for (i = 0; i < all_item_names.length; i++) {
                    all_item_names[i].classList.remove('item-name-in-category-page');
                    all_item_names[i].classList.add('item-name-in-category-page-two-columns');
                    };
                }
    });
    var modal_sizes_windows = document.getElementsByClassName("choose-size");
    var i;
    for (i = 0; i < modal_sizes_windows.length; i++) {
        modal_sizes_windows[i].addEventListener("click", function() {
            $.ajax({
                url: '/category/' + $(this).data('id') +'/sizes/',
                type: 'post',
                success: function(data) {
                if (data.success) {
                $('#modal-sizes').html(data.html);
                }
                },
            });
    })};
//-----------   CATEGORY TOGGLER     -----------
});