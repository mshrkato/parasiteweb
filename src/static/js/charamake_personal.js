//読みこみ完了後に処理
jQuery(function () {
	//パーソナリティ
	$('.personal').append($('<option></option>').attr('value',0).html('--'));		
	for(var i=11; i<=66;i++){
		$('.personal').append($('<option></option>').attr('value',i).html(i));		
	}
	
	//パーソナリティ一括ロール
	$('#rolePersonal').click(function(){
		$('#selectBirth').val(rolld66());
		$('#selectExperience').val(rolld66());
		$('#selectCauseOfParasite').val(rolld66());
		$('#selectFeature').val(rolld66());
		$('#selectFeeling').val(rolld66());
		$('#selectPurpose').val(rolld66());
		$('#selectspecies').val(rolld66());
		$('#selectAppearance').val(rolld66());
	});
	
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

//nd6ダイスロール
function rolld66(){
	var num = 0;
	num += Math.floor(Math.random() * 6) +1;
	num = num*10 + Math.floor(Math.random() * 6) +1;
	
	return num;
}