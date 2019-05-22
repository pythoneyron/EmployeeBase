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
    // var filter = $('#filterAlphabet button');
    // $(filter).click(function (e) {
    //     var data = this.value;
    //     var url_res = '?alphabet_range=' + data;
    //     var url = new Url();
    //
    //     if ('paginate_by' in url.query) {
    //         url_res += '&paginate_by=' + url.query.paginate_by;
    //     }
    //     location.href = url_res;
    // });

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

    if (window.location.href.indexOf("alphabet") > -1){
        // Создание подключения к WebSocket
        let webSocket = new WebSocket('ws://' + window.location.host + '/ws/users/');

        // Обработка событий
        webSocket.onmessage = function (event) {
            let message = JSON.parse(event.data);

            if (message && message.connected) {
                console.info(message.connected);
            }

            if (message && message['users_json']) {
                const $mainTbodyUsers = $('#tbody-users-id');

                $.each(message['users_json'], function (i, userJSON) {
                    $mainTbodyUsers.append('<tr></tr>');
                    $mainTbodyUsers.append('<td>' + userJSON['id'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_full_name'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_age'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_company'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['position'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_section'] + '</td>');

                    const start_date = new Date(userJSON['start_date']);
                    const start_date_f = start_date.toLocaleString('ru', { year: 'numeric', month: 'long', day: 'numeric'});
                    $mainTbodyUsers.append('<td>' + start_date_f + '</td>');

                    if (!userJSON['end_date']){
                        $mainTbodyUsers.append('<td>Работает в настоящее время.</td>');
                    } else {
                        const end_date = new Date(userJSON['end_date']);
                        const end_date_f = end_date.toLocaleString('ru', { year: 'numeric', month: 'long', day: 'numeric'});
                        $mainTbodyUsers.append('<td>' + end_date_f + '</td>');
                    }

                    $mainTbodyUsers.append('<td>' + userJSON['get_status'] + '</td>');
                });

            } else if (message && message['users_alphabet']){
                const $mainTbodyUsers = $('#tbody-users-id');
                $mainTbodyUsers.empty();
                $.each(message['users_alphabet'], function (i, userJSON) {
                    $mainTbodyUsers.append('<tr></tr>');
                    $mainTbodyUsers.append('<td>' + userJSON['id'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_full_name'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_age'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_company'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['position'] + '</td>');
                    $mainTbodyUsers.append('<td>' + userJSON['get_section'] + '</td>');

                    const start_date = new Date(userJSON['start_date']);
                    const start_date_f = start_date.toLocaleString('ru', { year: 'numeric', month: 'long', day: 'numeric'});
                    $mainTbodyUsers.append('<td>' + start_date_f + '</td>');

                    if (!userJSON['end_date']){
                        $mainTbodyUsers.append('<td>Работает в настоящее время.</td>');
                    } else {
                        const end_date = new Date(userJSON['end_date']);
                        const end_date_f = end_date.toLocaleString('ru', { year: 'numeric', month: 'long', day: 'numeric'});
                        $mainTbodyUsers.append('<td>' + end_date_f + '</td>');
                    }

                    $mainTbodyUsers.append('<td>' + userJSON['get_status'] + '</td>');
                });
            }
            console.log(message)
        };

        // Выборка по алфавиту. Отправка сообщения на WebSocket
        var filter = $('#filterAlphabet button');
        $(filter).click(function (e) {
            e.preventDefault();
            filter.removeClass('active');
            $(this).addClass('active');
            var range_alphabet = this.value;

            let message = JSON.stringify({'get_users_alphabet': {'range_alphabet': range_alphabet}});
            webSocket.send(message);

            // if ('paginate_by' in url.query) {
            //     url_res += '&paginate_by=' + url.query.paginate_by;
            // }
        });

        // Сообщение об отключении WebSocket
        webSocket.onclose = function (e) {
            console.error('WebSocket disconnected');
        };
    }

});