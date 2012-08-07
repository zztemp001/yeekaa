$(document).ready(function() {
    $("#getting").click(function() {
       $.get("/baseinfo/testajax/", function(data) {
           $("#result").html(data);
       });
    });

    $("#posting").click(function() {
       $.post("/baseinfo/testajax/", {title: "Monty 中文", foo:"bar"}, function(data) {
           $("#result").html(data);
       });
    });

    $(".target").change(function() {
        $.post("/baseinfo/testajax/", {title: $(this).val(), foo:"bar"}, function(data) {
            $("#result").html(data);
        });
    });

    $("#json").click(function() {
        $.get("/baseinfo/testjson/", function(data) {
            obj= $.parseJSON(data);
            $("#result").html(obj[1].fields.title);
        });
    });
});