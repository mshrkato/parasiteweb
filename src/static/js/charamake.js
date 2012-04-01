//種族ごとの寄生体選択
//※印将来的には寄生体情報データベースを作って統合すべきかも
var parasiteOfHuman = [
	"セルティス",
	"クレイモア",
	"ヴォージェ",
	"ブリガンダイン",
	"アルバレスト",
	"カラドボルグ",
	"モリオン",
	"ウォーコイト"
];

var parasiteOfAnimal = [
	"ジャベリン",
	"バルディッシュ",
	"カラドボルグ",
	"モリオン",
	"ウォーコイト"	
];

//種族ごとの職業(スキルとの対応付けは優先度低い)
var jobOfHuman = [
	"学生(通常)",
	"学生(優等生)",
	"学生(不良)",
	"講師",
	"科学者",
	"医療関係者",
	"探偵",
	"バウンサー",
	"家政婦(or夫)",
	"ドライバー",
	"芸能人",
	"起業家",
	"司法関係者",
	"ディレッタント",
	"DUSTコマンド",
	"DUSTアサルト",
	"DUSTスカウト",
	"DUSTイサー"
];

//動物の職業
var jobOfAnimal = [
	"野良",
	"ペット",
	"訓練動物"
];

//読みこみ完了後に処理
jQuery(function () {
	//元値
	$('.original').append($('<option></option>').html('--'));		
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


	//種族ごとの寄生体と職業選択
	$('select#selectspecies').change(function(){
		$('#selectParasite').empty();
		$('#selectParasite').append($('<option></option>').html('--'));		

		$('#selectJob').empty();
		$('#selectJob').append($('<option></option>').html('--'));		

		var species = jQuery('#selectspecies option:selected').val();
		var parasiteList;
		var jobList;
		if(species == '人間'){
			parasiteList = parasiteOfHuman;
			jobList = jobOfHuman;
			$('#itemsLabel').html('所持品');
		}
		else{
			parasiteList = parasiteOfAnimal;
			jobList = jobOfAnimal;
			$('#itemsLabel').html('特性');
		}

		for(var i = 0; i < parasiteList.length; i++){
			$('#selectParasite').append($('<option></option>').html(parasiteList[i]));		
		}
		for(var i = 0; i < jobList.length; i++){
			$('#selectJob').append($('<option></option>').html(jobList[i]));		
		}

	});
	
	//skillレベル
	for(var i = 0; i <= 3; i++){
		$('.skillLv').append($('<option></option>').attr('value',i).html(i*5));		
	}
	
	//artSkill追加ボタン
	$('#addArtSkillAdd').click(function(){
		var count = $('.artrow').size() + 1;
		var rowElement = $('<div></div>').addClass('row artrow').attr('id','artrow' + count);
		var prependElement = $('<div></div>').addClass('span4 offset2').append(
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
	
	//パーソナリティ
	$('.personal').append($('<option></option>').attr('value',0).html('--'));		
	for(var i=11; i<=66;i++){
		$('.personal').append($('<option></option>').attr('value',i).html(i));		
	}
});

//nd6ダイスロール
function roll(numOfDise){
	var num = 0;
	for(var i=0; i < numOfDise;i++){
		num += Math.floor(Math.random() * 6) +1;
	}
	
	return num;
}