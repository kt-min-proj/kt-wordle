$(function () {
  var today = new Date();
  var date = new Date();

  $("input[name=preMon]").click(function () {
    // 이전달
    $("#calendar > tbody > td").remove();
    $("#calendar > tbody > tr").remove();
    today = new Date(today.getFullYear(), today.getMonth() - 1, today.getDate());
    buildCalendar();
  });

  $("input[name=nextMon]").click(function () {
    // 다음달
    $("#calendar > tbody > td").remove();
    $("#calendar > tbody > tr").remove();
    today = new Date(today.getFullYear(), today.getMonth() + 1, today.getDate());
    buildCalendar();
  });

  function buildCalendar() {
    nowYear = today.getFullYear();
    nowMonth = today.getMonth();
    firstDate = new Date(nowYear, nowMonth, 1).getDate();
    firstDay = new Date(nowYear, nowMonth, 1).getDay(); //1st의 요일
    lastDate = new Date(nowYear, nowMonth + 1, 0).getDate();

    if ((nowYear % 4 === 0 && nowYear % 100 !== 0) || nowYear % 400 === 0) {
      //윤년 적용
      lastDate[1] = 29;
    }

    $(".year_month").text(nowYear + " - " + (nowMonth + 1));

    for (i = 0; i < firstDay; i++) {
      //첫번째 줄 빈칸
      $("#calendar tbody:last").append("<td></td>");
    }
    for (i = 1; i <= lastDate; i++) {
      // 날짜 채우기
      plusDate = new Date(nowYear, nowMonth, i).getDay();
      if (plusDate == 0) {
        $("#calendar tbody:last").append("<tr></tr>");
      }

      $("#calendar tbody:last").append(`<td><input class='date' name='date' type='button' value=${i} /></td>`);
    }
    if ($("#calendar > tbody > td").length % 7 != 0) {
      //마지막 줄 빈칸
      for (i = 1; i <= $("#calendar > tbody > td").length % 7; i++) {
        $("#calendar tbody:last").append("<td></td>");
      }
    }
    $("td > input.date").each(function (index) {
      // 오늘 날짜 표시
      if (nowYear == date.getFullYear() && nowMonth == date.getMonth() && $("td > input.date").eq(index).val() == date.getDate()) {
        $("td > input.date").eq(index).addClass("colToday");
      }
    });
    $("input[name=date]").click(function (index) {
      clicked_Days = index.currentTarget.value
      submitData(`${nowYear}-${twoNumber(nowMonth + 1)}-${twoNumber(clicked_Days)}`).then(res => {
        rankView(res)
      })
    })

  }

  function twoNumber(num) {
    let variable = Number(num).toString();
    if (Number(variable) < 10 && variable.length === 1) {
      variable = "0" + variable;
    }
    return variable;
  }

  buildCalendar();
});

// Rendering data
const rankView = async (data) => {
  $("#dayrankname").remove()
  $("#scoreboard > div > div").remove()

  let o
  for (let i = 0; i <= 9; i++) {
    o = data.rank[i]
    if (typeof (o[0]) != 'undefined') {
      $("#scoreboard").append(`<div id="rankBoard">
        <div id="dayrankRank">${i + 1}</div>
        <div id="dayrankName">${o[0]}</div>
        <div id="dayrankAccount">${o[1]}</div>
      </div>`)
    }
  }
}

const submitData = async (data) => {
  let res = await axios.post("/calendar/post/", {
    date: data, answer: "", rank: {
      0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []
    }
  })
  document.getElementById("date_name").text = res.data.answer;
  console.log(res.data)
  return res.data;
}