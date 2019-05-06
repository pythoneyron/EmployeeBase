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

    // Выборка по алфавиту
    var filter = $('#filterAlphabet button');
    $(filter).click(function (e) {
        var data = this.value;
        var url_res = '?alphabet_range=' + data;
        var url = new Url();

        if ('paginate_by' in url.query) {
            url_res += '&paginate_by=' + url.query.paginate_by;
        }
        location.href = url_res;
    });

    // Фильтрация
    var form = $('#filterForm');
    $(form).submit(function (e) {
        e.preventDefault();
        var data = form.serialize();
        var url_res = '?' + data;
        var url = new Url();

        if ('paginate_by' in url.query) {
            url_res += '&paginate_by=' + url.query.paginate_by;
        }
        location.href = url_res;
    });

    // Сброс фильтрации
    $('.btn-reset-js').on('click', function () {
        var url = new Url();
        var paginate_by = url.query.paginate_by;
        // var sort_val =  url.query.sort_val;

        url.clearQuery(); // Removes all query string parameters from the URL

        if (paginate_by){
            url.query.paginate_by = paginate_by;
        }

        // if (sort_val){
        //     url.query.sort_val = sort_val;
        // }

        location.href = url.toString();
    });

});