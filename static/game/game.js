var user = "KT"
var answer = "4567";
var answer_list = new Array();
var answer_list = Array.from(answer);
var my_oppertunity = 0;
var opportunity = answer_list.length + 1;
var user_input_list = new Array();

//초기화면 설정 : 정답글자수에 맞춰서 칸이 나오게함
for (j = 0; j < opportunity; j++) {
    for (i = 0; i < answer_list.length; i++) {
        s = '<input class="textbox" id="' + String(i + j * 100) + '" name ="' + String(i + j * 100) + '" type="text" maxlength = "1"'
         + 'onkeyup="if(document.getElementById('+String(i + j * 100)+').value.length == 1) document.getElementById('+String(i + j * 100+1)+').focus();">'
        document.getElementById("box").innerHTML += s;

        document.getElementById(String(i + j * 100)).onkeydown = function() {
            if (this.value.length === parseInt(this.attributes["maxlength"].value)) {
                String(i + j * 100+1).focus();
            }
        }
        if (answer_list.length - i == 1) {
            document.getElementById(i + j * 100).setAttribute('onkeyup', 'game()')
            document.getElementById("box").innerHTML += '<br/>'
        }
    }
}

//값을 입력하고 확인눌렀을때 정답과 입력값을 비교
function game() {
    if (window.event.keyCode == 13) {
        user_input_list = []
        jvalue = (my_oppertunity) * 100
        for (i = 0; i < answer_list.length; i++) {
            ivalue = String(jvalue + i)
            user_input_list.push(document.getElementById(ivalue).value)
        }
        for (i = 0; i < answer_list.length; i++) {
            c = String(jvalue + i)
            if (answer_list[i] != user_input_list[i]) {
                if (answer_list.includes(user_input_list[i])) {
                    document.getElementById(c).className = 'textboxErr'
                    document.getElementById(c).setAttribute('readonly', 'true')
                }
                else {
                    document.getElementById(c).setAttribute('readonly', 'true')
                }
            }
            else {

                document.getElementById(c).className = 'textboxDef'
                document.getElementById(c).setAttribute('readonly', 'true')
            }
        }
        if (my_oppertunity < opportunity) {
            my_oppertunity += 1;
        }
        else {
            alert("x");
        }
    }

}