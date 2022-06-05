let button = document.getElementById('button');

button.addEventListener('click', () => {
   // 2つの入力フォームの値を取得
    let formA = document.getElementById("formA").value;
    let formB = document.getElementById("formB").value; 
    
    // 入力フォームの値を数値に変換
    let formA_num = Number(formA);
    let formB_num = Number(formB);

    // 秒数に変換
    let sectime = formA_num * 60 + formB_num;
    
    // 予測タイムを計算
    let prediction_time = sectime * 42.195;

    // 時間、分、秒に変換
    let hour = Math.floor(prediction_time / 3600);
    let min = Math.floor((prediction_time - hour * 3600) / 60);
    let sec = Math.round(prediction_time - hour * 3600 - min * 60);

    // 結果を表示
    document.getElementById("result").innerHTML = hour + "時間" + min + "分" + sec + "秒";
});