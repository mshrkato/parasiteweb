//読みこみ完了後に処理
jQuery(function () {
	//種族ごとの寄生体と職業選択
	$('select#selectspecies').change(function(){
		var species = jQuery('#selectspecies option:selected').val();
		ParasiteWeb.makeParasiteSelectList ('select#selectParasite',species);
		ParasiteWeb.makeJobSelectList('select#selectJob',species);
	});
	
	//validation
	$("#inputCharaName").validate({
        expression: "if (VAL) return true; else return false;",
        message: "キャラクター名を入力して下さい"
    });

	$("#inputCharaAge").validate({
        expression: "if (VAL) return true; else return false;",
        message: "キャラクターの年齢を入力して下さい"
    });
	$("#optionsCharaSex").validate({
        expression: "if (isChecked(SelfID)) return true; else return false;",
        message: "性別を選択して下さい"
    });
    $("#selectspecies").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "種族を選んで下さい"
    });
    $("#selectParasite").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "悪魔寄生体を選んで下さい"
    });
    $("#selectJob").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "職業を選んで下さい"
    });
});