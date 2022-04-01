$(document).ready(function(){
    var url_dir = $(this).attr('action_url')
    

    $('.show').onclick(function() {
        var ident = $(this).attr('idef')
        
        $.ajax ({
            //url: url_dir,
            url: '/recipe/',
            type: "POST",
            data: {'idef': ident },
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            success: function (data) {
                console.log(ident);
            },
        });
    });
});