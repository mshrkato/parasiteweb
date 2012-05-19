//ダイアログ作成関数
var Page = {
    show_ok_dialog: function (dialog_id) {
        $(dialog_id).dialog({
            bgiframe: true,
            modal: true,
            buttons: {
                "OK": function () {
                    $(this).dialog("destroy");
                }
            }
        });
    },

    show_confirm_dialog: function (dialog_id, ok_func, cancel_func) {
        $(dialog_id).dialog({
            bgiframe: true,
            modal: true,
            buttons: {
                "OK": ok_func,
                "Cancel": cancel_func
            }
        });
    }
};

jQuery(function () {
	$(".btn-danger").each(function(){
		$(this).click(function (e) {
	        e.preventDefault();
	        var key = $(this).attr('id');
	        $(".dialog").html(key + "を削除します");
	        Page.show_confirm_dialog("#delete-confirm-dialog",
	            function () {
	                // OKボタンをクリックした時の処理
			        $(".dialog").html("処理中です…");
			        $(".dialog").html($("#mode").attr('value'));
			        $("#mode").attr('value','delete');
			        $(".dialog").html($("#mode").attr('value'));
			        $(".dialog").html($("#deleteKey").attr('value'));
			        $("#deleteKey").attr('value',key);
			        $(".dialog").html($("#deleteKey").attr('value'));
	                $("form").submit();
/*
	                $("form").submit(function() {
						return true;
					});
*/
	                //$(this).dialog("destroy"); // ダイアログを削除
	            },
	            function () {
	                // キャンセルボタンをクリックした時の処理
	                //submit中止
	                $(this).dialog("destroy");
	                
	            }
        	)
		})
	})
});