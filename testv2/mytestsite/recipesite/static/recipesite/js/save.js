$(document).ready(function(){
    var url_dir = $(this).attr('action_url')
    

    $('.save').click(function() {
        var ident = $(this).attr('idef')
        
        $.ajax ({
            //url: url_dir,
            url: '/favs/',
            type: "POST",
            data: {'idef': ident },
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            success: function (data) {
                console.log(ident);
            },
        });
    });
});