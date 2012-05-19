//読みこみ完了後に処理
jQuery(function () {
	//パーソナリティ
	ParasiteWeb.makePersonalList('select.personal');
	
	//パーソナリティ一括ロール
	$('#rolePersonal').click(function(){
		$('#selectBirth').html(ParasiteWeb.Rolld66());
		$('#selectExperience').html(ParasiteWeb.Rolld66());
		$('#selectCauseOfParasite').html(ParasiteWeb.Rolld66());
		$('#selectFeature').html(ParasiteWeb.Rolld66());
		$('#selectFeeling').html(ParasiteWeb.Rolld66());
		$('#selectPurpose').html(ParasiteWeb.Rolld66());
		$('#selectspecies').html(ParasiteWeb.Rolld66());
		$('#selectAppearance').html(ParasiteWeb.Rolld66());
	});
	
	//スタンス
	ParasiteWeb.makeHeroStanceList('select#selectStance');

	//所属組織
	ParasiteWeb.makeOrganizationsList('select#selectOrganization',0);
		
	//validation
	$("#inputBirth").validate({
        expression: "if (VAL) return true; else return false;",
        message: "生まれをd66から決定して下さい"
    });

	$("#inputExperience").validate({
        expression: "if (VAL) return true; else return false;",
        message: "人生経験をd66から決定して下さい"
    });
	$("#inputCauseOfParasite").validate({
        expression: "if (VAL) return true; else return false;",
        message: "寄生された理由をd66から決定して下さい"
    });
	$("#inputFeature").validate({
        expression: "if (VAL) return true; else return false;",
        message: "特徴をd66から決定して下さい"
    });
	$("#inputFeeling").validate({
        expression: "if (VAL) return true; else return false;",
        message: "感情をd66から決定して下さい"
    });
	$("#inputPurpose").validate({
        expression: "if (VAL) return true; else return false;",
        message: "目的をd66から決定して下さい"
    });
	$("#inputAppearance").validate({
        expression: "if (VAL) return true; else return false;",
        message: "外見をd66から決定して下さい"
    });
    
        $("#selectStance").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "スタンスを選んで下さい"
    });
    $("#selectOrganization").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "所属を選んで下さい"
    });
});