    function ajaxxx(adr, fsccss, ffl, data)
    {
    return $.ajax({

        url: adr,
       data: data,
        type: 'get', // This is the default though, you don't actually need to always mention it
        success: fsccss,
        failure: ffl
    });
    }

var New = true;
var Now = {};

function butt_gen(id, addr, f1=(function () {}), f2=(function () {}))
{
    return function ()
    {
        let data_a = {id: id};
        ajaxxx(addr, f1, f2, data_a);
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
            $("#delete").click(butt_gen(Now.id, "del_note/"));
            $("#roy").click(butt_gen(Now.id, "read_only/", function (data) {
                if (data=='True')
                    document.getElementById('text').contentEditable = 'false';
                else
                    document.getElementById('text').contentEditable = 'true';
            }));
        }
        else{
            console.log("KO");
        }

    }, function () {
    }, data_a );
}