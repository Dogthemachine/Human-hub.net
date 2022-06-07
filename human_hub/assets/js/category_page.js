$(document).ready(function() {
//-----------   CATEGORY TOGGLER     -----------
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
//-----------   CATEGORY TOGGLER     -----------
});