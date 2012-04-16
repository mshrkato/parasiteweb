//読みこみ完了後に処理
jQuery(function () {
	//元値
	$('.original').append($('<option></option>').attr('value',0).html('--'));		
	for(var i = 2; i <= 12; i++){
		$('.original').append($('<option></option>').attr('value',i).html(i));
	}
	
	//元値ロール関数
	$('#roleall').click(function(){
		$('#selectpow').val(roll(2));
		$('#selectagi').val(roll(2));
		$('#selectfeal').val(roll(2));
		$('#selectluc').val(roll(2));
		$('#selectint').val(roll(2));
		$('#selectment').val(roll(2));
	});
	
	//skillレベル
	for(var i = 0; i <= 3; i++){
		$('.skillLv').append($('<option></option>').attr('value',i).html(i*5));		
	}
	
	//artSkill追加ボタン
	$('#addArtSkill').click(function(){
		var count = $('.artrow').size() + 1;
		var rowElement = $('<div></div>').addClass('row artrow').attr('id','artrow' + count);
		var prependElement = $('<div></div>').addClass('span4 offset1').append(
			$('<div></div>').addClass('input-prepend').append(
				$('<span></span>').addClass('add-on').html('芸術：')
			).append(
				$('<input>').attr('name', 'prependedInputArt' + count).attr('size','16').attr('type','text')
			)
		);
		var inputElement = $('<div></div>').addClass('span1').append(
			$('<select></select>').addClass('skillLv span1').attr('id','selectArtSkill' + count).attr('name','selectArtSkill' + count)
		);
		var deleteElement = $('<div></div>').addClass('span1').append(
			$('<span></span>').addClass('btn btn-danger').html('-').click(function(){
				$('#artrow' + count).remove();
			})
		);
				
		$('#artskill').append(
			rowElement.append(prependElement).append(inputElement).append(deleteElement)
		);

		for(var i = 0; i <= 3; i++){
			$('#selectArtSkill' + count).append($('<option></option>').attr('value',i).html(i*5));	
		}	
	});

	//Skill追加ボタン
	$('#addKnowledgeSkill').click(function(){
		var count = $('.knowledgerow').size() + 1;
		var rowElement = $('<div></div>').addClass('row knowledgerow').attr('id','knowledgerow' + count);
		var prependElement = $('<div></div>').addClass('span4 offset1').append(
			$('<div></div>').addClass('input-prepend').append(
				$('<span></span>').addClass('add-on').html('知識：')
			).append(
				$('<input>').attr('name', 'prependedInputKnowledge' + count).attr('size','16').attr('type','text')
			)
		);
		var inputElement = $('<div></div>').addClass('span1').append(
			$('<select></select>').addClass('skillLv span1').attr('id','selectKnowledgeSkill' + count).attr('name','selectKnowledgeSkill' + count)
		);
		var deleteElement = $('<div></div>').addClass('span1').append(
			$('<span></span>').addClass('btn btn-danger').html('-').click(function(){
				$('#knowledgerow' + count).remove();
			})
		);
				
		$('#knowledgeSkill').append(
			rowElement.append(prependElement).append(inputElement).append(deleteElement)
		);

		for(var i = 0; i <= 3; i++){
			$('#selectKnowledgeSkill' + count).append($('<option></option>').attr('value',i).html(i*5));	
		}	
	});
	
	//validation
    $("#selectpow").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });
    $("#selectagi").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });
    $("#selectfeal").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });
    $("#selectluc").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });
    $("#selectint").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });
    $("#selectment").validate({
        expression: "if (VAL != '0') return true; else return false;",
        message: "2d6で振って下さい"
    });

});

//nd6ダイスロール
function roll(numOfDise){
	var num = 0;
	for(var i=0; i < numOfDise;i++){
		num += Math.floor(Math.random() * 6) +1;
	}
	
	return num;
}