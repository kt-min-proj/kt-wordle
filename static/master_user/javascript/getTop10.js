const ajax = fetch('/master/get_todayRanker');

ajax.then(function(response){
    return response.json()
}).then(function(result){
    let ranker = document.querySelector('.rankar');
    for(let i =0; i < result.length; i++){
        let div = document.createElement('div');
        div.innerHTML = result[i].user_rank+'등    ' + result[i].user_name;
        div.style = 'margin: 15px 0; text-align: center; font-family : "Gill Sans MT"; font-size: 20px; color : black;'
        ranker.appendChild(div)
    }
})