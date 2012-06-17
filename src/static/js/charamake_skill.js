//読みこみ完了後に処理
jQuery(function () {
	//元値
	ParasiteWeb.makeOriginalSelectList('.original',0)
	
	//元値ロール関数
	$('#roleall').click(function(){
		$('#selectpow').val(ParasiteWeb.Rollnd6(2));
		$('#selectagi').val(ParasiteWeb.Rollnd6(2));
		$('#selectfeal').val(ParasiteWeb.Rollnd6(2));
		$('#selectluc').val(ParasiteWeb.Rollnd6(2));
		$('#selectint').val(ParasiteWeb.Rollnd6(2));
		$('#selectment').val(ParasiteWeb.Rollnd6(2));
	});
	
	//skillレベル
	ParasiteWeb.makeSkillLevelSelectList('.skillLv',0)
	
	//artSkill追加ボタン
	$('#addArtSkill').click(function(){
		ParasiteWeb.addValiableSkills('artSkillRow', 'artSkills', '芸術', 'artOriginalName', 'artOriginalLv')
	});

	//Skill追加ボタン
	$('#addKnowledgeSkill').click(function(){
		ParasiteWeb.addValiableSkills('knowledgeSkillRow', 'knowledgeSkills' ,'知識', 'knowOriginalName', 'knowOriginalLv')
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