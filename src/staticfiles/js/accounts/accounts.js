$(document).ready(function () {

    // Пагинация количества вывода
    $('.custom-select-js').on('change', function () {
        var url = new Url();
        if ('page' in url.query) {
            delete (url.query.page);
        }
        url.query.paginate_by = $(this).val();
        location.href = url;
    });

});