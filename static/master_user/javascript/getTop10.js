const ajax = fetch('/master/get_todayRanker');

ajax.then(function(response){
    return response.json()
}).then(function(result){
    let ranker = document.querySelector('.rankar');
    for(let i =0; i < result.length; i++){
        let div = document.createElement('div');
        div.innerHTML = result[i].user_rank + ' ' + result[i].user_name;
        ranker.appendChild(div)
    }
})