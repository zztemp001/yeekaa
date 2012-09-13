$(document).ready(function() {
    $("#getting").click(function() {
        $.get("/baseinfo/testajax/", function(data) {
            // alert($("#result").html());
            // $("#result").html(data);
            // document.getElementById("result").innerHTML=data;
            // alert(document.getElementById("result").innerHTML);
            // alert($("#result").html());
            $("#result").html(data);
            $("#dks").change(function() {
                $.post("/baseinfo/testajax/", {title: $(this).val(), foo:"bar"}, function(data) {
                    $("#sub_result").html(data);
                });
            });
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
            //$("#result").html(obj[1].fields.title);
            alert(data);
            alert(obj);
            $.each(obj, function(key, value) {
                alert(key + ":" + value);
            });
        });
    });

    $("#dks").change(function() {
        $.post("/baseinfo/testajax/", {title: $(this).val(), foo:"bar"}, function(data) {
            $("#sub_result").html(data);
        });
    });

    $("select.parent").hide();

    $("#id_level").change(function() {
        $("select.parent").hide();
        var lv = $(this).val() - 1;
        if (lv > 0){
            $("select.parent:lt(" + lv +")").show();
            $.post(
                "/baseinfo/getparent/",
                {"level": $(this).val()},  //传递的是拟增加地点的真是层级数
                function(data) {
                    $.each(data, function(k, v) {
                        //alert(k + ":" + v);
                        $("select.parent:[level=" + k +"]").html(v);
                    });
                },
                "json");  //1.4版本后的jquery需要指定服务器返回数据的类型，可以是（(xml, json, script, or html）
            }
        $("#id_title").focus();
    });

    $("select.parent").change(function() {
        var lv = $(this).attr("level");
        if (lv < $("#id_level").val()-1) {
            $(this).nextAll().empty();
            var next = $(this).next();
            $.post(
                "/baseinfo/getnextparent/",
                {"level": lv, "parent": $(this).val()},
                function(data) {
                    if (data.length==0) {
                        alert("下一级尚无内容");
                    }
                    else {
                        next.html(data);
                    }
                });
        }
        else {
            $("#id_title").focus();
        }
    });

    $("#place_form").submit(function() {
        var lv = $("#id_level").val() - 1;  //得到拟新增地点层级向上一级，就是最后一个下拉框的顺序
        var pr = $("select.parent:[level=" + lv +"]").val();  //得到最后一个下拉框的值，就是新增地点的父节点
        $("#id_parent").val(pr);  //将表单的parent设置为父节点的值
        // alert($("#id_parent").val());
        if (!$("#id_parent").val().length || !$("#id_title").val().length) {
            return false;
        }  //如果parent的值为空，则取消提交
    });
});