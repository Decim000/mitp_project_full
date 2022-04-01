$(document).ready(function(){
    var url_dir = $(this).attr('action_url')

    $('.delete').click(function() {
        var id_todelete = $(this).attr('id_del')
        
        $.ajax ({
            //url: url_dir,
            url: '/favs/',
            type: "POST",
            data: {'id_del': id_todelete},
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            success: function (data) {
                console.log(id_todelete);
            },
        });
    });
});