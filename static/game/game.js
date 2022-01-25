var user = "KT"
var answer = "qwert";
var answer_list = new Array();
var answer_list = Array.from(answer);
var my_oppertunity = 0;
var opportunity = answer_list.length + 1;
document.write(answer_list.length);
document.write("자 제한");
var user_input_list = new Array();

//초기화면 설정 : 정답글자수에 맞춰서 칸이 나오게함
for(j = 0; j< opportunity; j++){
    for(i = 0; i < answer_list.length; i++){
        s = '<input class="textbox" id="' +String(i+j*100) + '" name ="'+String(i)+'" type="text">'
        document.getElementById("box").innerHTML += s;
        if(answer_list.length-i == 1){
            document.getElementById("box").innerHTML += '<br/>'
        }
    }
}

//값을 입력하고 확인눌렀을때 정답과 입력값을 비교
function game() {
    user_input_list = []
    jvalue = (my_oppertunity)*100
    for (i = 0; i<answer_list.length; i++){
        ivalue = String(jvalue+i)
        user_input_list.push(document.getElementById(ivalue).value)
    }
    for (i = 0; i < answer_list.length; i++) {
        c = String(jvalue+i)
        if (answer_list[i] != user_input_list[i]) {
            if (answer_list.includes(user_input_list[i])) {
                document.getElementById(c).className = 'textboxErr'
                document.getElementById(c).setAttribute('readonly', 'true')
            }
            else {
                document.getElementById(c).className = 'textboxDef'
                document.getElementById(c).setAttribute('readonly', 'true')
            }
        }
        else {
            document.getElementById(c).className = 'textboxCorr'
            document.getElementById(c).setAttribute('readonly', 'true')
        }
    }
    if (my_oppertunity < opportunity) {
        my_oppertunity += 1;
    }
    else {
        alert("x");
    }
    document.getElementById("trygame").innerHTML = my_oppertunity + "회 시도"
}