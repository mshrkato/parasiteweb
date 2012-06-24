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

//ヒーロースタンスリスト
var heroStance = [
	"トゥルーヒーロー",
	"イモータルヒーロー",
	"ガーディアンヒーロー",
	"ダークヒーロー",
	"クレバーヒーロー"
];

//所属組織リスト
var organizations = [
	"DUST",
	"セラフィム",
	"フリーランス"
];

//ライブラリ
function ParasiteWeb(){};

//寄生体リスト
ParasiteWeb.makeParasiteSelectList = function(target,species){
	var parasiteList;
	if(species == '人間'){
		parasiteList = parasiteOfHuman;
	}
	else{
		parasiteList = parasiteOfAnimal;
	}

	$(target).empty();
	$(target).append($('<option></option>').attr('value','0').html('--'));

	for(var i = 0; i < parasiteList.length; i++){
		$(target).append($('<option></option>').html(parasiteList[i]));		
	}
	
	return;
}

//職業リスト
ParasiteWeb.makeJobSelectList = function(target,species){
	var jobList;
	if(species == '人間'){
		jobList = jobOfHuman;
	}
	else{
		jobList = jobOfAnimal;
	}

	$(target).empty();
	$(target).append($('<option></option>').attr('value','0').html('--'));

	for(var i = 0; i < jobList.length; i++){
		$('#selectJob').append($('<option></option>').html(jobList[i]));		
	}

	return;
}

//元値リスト
ParasiteWeb.makeOriginalSelectList = function(target,min){
	if(min <= 0){
		$(target).append($('<option></option>').attr('value',0).html('--'));		
	}

	for(var i = min; i <= 12; i++){
		$(target).append($('<option></option>').attr('value',i).html(i));
	}

}

//Roll
ParasiteWeb.Rollnd6 = function(numOfDise){
	var num = 0;
	for(var i=0; i < numOfDise;i++){
		num += Math.floor(Math.random() * 6) +1;
	}
	
	return num;
}

//技能レベルリスト
ParasiteWeb.makeSkillLevelSelectList = function(target, min){
	if(min <= 0){
		$(target).append($('<option></option>').attr('value',0).html('--'));
	}
	
	if(min <= 5){
		$(target).append($('<option></option>').attr('value',5).html('初級'));
	}

	if(min <= 10){
		$(target).append($('<option></option>').attr('value',10).html('中級'));
	}

	if(min <= 15){
		$(target).append($('<option></option>').attr('value',15).html('上級'));
	}
	
	if(min == 15){
		$(target).attr("disabled", true);
	}
}

//可変個スキル
ParasiteWeb.addValiableSkills = function(appendElement, skillNameAttr, skillName, skillOriNameId, skillOriLvId){
	//select要素の識別し
	var date = new Date();
	var rowIdentifer = 'row' + date.getMinutes() + date.getSeconds() + date.getMilliseconds();
	var selectIdentifer = 'select' + date.getMinutes() + date.getSeconds() + date.getMilliseconds();
	
	//要素作成
	//大枠
	var rowElement = $('<div></div>').addClass('row').attr('id',rowIdentifer);
	
	//text
	var prependElement = $('<div></div>').addClass('input-prepend span4')
		.append($('<span></span>').addClass('add-on').html(skillName + '：')	)
		.append($('<input>').attr('name', skillNameAttr).attr('size','16').attr('type','text'));
	//lv
	var inputElement = $('<div></div>').addClass('span1').append(
		$('<select></select>').attr('name',skillNameAttr).addClass('skillLv span1').attr('id',selectIdentifer)
	);
	var deleteElement = $('<div></div>').addClass('span1')
		.append($('<span></span>').addClass('btn btn-danger').html('<i class="icon-minus icon-white"></i>')
			.click(function(){
				$('#' + rowIdentifer).remove();
			})
		);

	//合成
	$('#' + appendElement).append(
		rowElement.append(prependElement).append(inputElement).append(deleteElement)
	);
	//Lv書き換え
	ParasiteWeb.makeSkillLevelSelectList('#' + selectIdentifer, 0)
}

//パーソナリティダイス
ParasiteWeb.makePersonalList = function(target){
	$(target).append($('<option></option>').attr('value',0).html('--'));		
	for(var i=11; i<=66;i++){
		$(target).append($('<option></option>').attr('value',i).html(i));
	}
}

//Rolld66
ParasiteWeb.Rolld66 = function(){
	var num = 0;
	num += Math.floor(Math.random() * 6) +1;
	num = num*10 + Math.floor(Math.random() * 6) +1;
	
	return num;
}

//ヒーロースタンスリスト
ParasiteWeb.makeHeroStanceList = function(target){
	$(target).append($('<option></option>').attr('value',0).html('--'));		
	for(var i = 0; i < heroStance.length; i++){
		$(target).append($('<option></option>').html(heroStance[i]));		
	}
}

//所属リスト
ParasiteWeb.makeOrganizationsList = function(target,now){
	if(now == 0){
		$(target).append($('<option></option>').attr('value',0).html('--'));		
	}

	for(var i = 0; i < organizations.length; i++){
		if(now == organizations[i]){
			$(target).append($('<option></option>').attr('selected','true').html(organizations[i]));
		}
		else{
			$(target).append($('<option></option>').html(organizations[i]));
		}
	}
}