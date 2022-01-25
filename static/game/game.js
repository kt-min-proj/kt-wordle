var answer = "1234";
var answer_list = new Array();
var answer_list = Array.from(answer);
var my_oppertunity = 0;
var opportunity = answer_list.length + 1;
document.write(answer_list.length);
document.write("자 제한");
var result = " "
var user_input_list = new Array();
for(j = 0; j< opportunity; j++){
    for(i = 0; i < answer_list.length; i++){
        s = '<input class="textbox" id="' +String(i+j*100) + '" name ="'+String(i)+'" type="text"></textarea>'
        document.getElementById("box").innerHTML += s;
        if(answer_list.length-i == 1){
            document.getElementById("box").innerHTML += '<br/>'
        }
    }
}

function game() {
    user_input_list = []
    jvalue = (my_oppertunity)*100
    for (i = 0; i<answer_list.length; i++){
        ivalue = String(jvalue+i)
        user_input_list.push(document.getElementById(ivalue).value)
    }
    for (i = 0; i < answer_list.length; i++) {
        if (answer_list[i] != user_input_list[i]) {
            if (answer_list.includes(user_input_list[i])) {
                result += user_input_list[i].fontcolor("red")
            }
            else {
                result += user_input_list[i]
            }
        }
        else {
            result += user_input_list[i].fontcolor("green")
        }
    }
    document.getElementById("message").innerHTML = result
    result += '<br/>'

    if (my_oppertunity < opportunity) {
        my_oppertunity += 1;
    }
    else {
        alert("x");
    }
    document.getElementById("trygame").innerHTML = my_oppertunity + "회 시도"
}