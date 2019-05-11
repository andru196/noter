    function ajaxxx(adr, fsccss, ffl, data){
    return $.ajax({

        url: adr,

       data: data,

        type: 'get', // This is the default though, you don't actually need to always mention it
        success: fsccss,

        failure: ffl
});}

var New = true;
var Now = {};

function del_gen(id) {
    return function () {
        data_a = {
            id: id
    }
    ajaxxx("del_note/", function () {},
        function () {}, data_a);
    }
}

function get_note(id)
{
    data_a = {
            id: id
    }
    ajaxxx("get_note/", function (data) {
        if (data != "!KO!")
        {
            data = JSON.parse(data);
            data.text = data.text.replace('\r\n', '<br>');
            $("#text").html(data.text);
            New = false;
            Now = data;
            $("#delete").click(del_gen(Now.id));
        }
        else{
            console.log("KO");
        }

    }, function () {
    }, data_a );
}