$(document).ready(function() {
    $("#controlbox input, #controlbox label, #controlbox textarea").each(function () {
        $(this).css('display', "none")
    });
    $("#controlbox input[type=button]").css('display', 'inline');
    $("#col").click(function ()
    {
       $("#id_color").css('display', "inline");
    });
                            });

function save_note() {
    if (New)
    {
        Now.id = "NEW";
    }
    document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.replace("<div>", "<br>")
    document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.replace("</div>", "")
    $("#id_id").val(Now.id);
    $("#id_text").val($("#text").html());
    document.getElementById("onlyform").submit();
}

function textChanged() {
    $("#controlbox").show("slow");
    if ($("#text").text() == '')
        $("#controlbox").hide();
}
