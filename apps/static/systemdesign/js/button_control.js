/*２回押しでラジオボタンの選択解除
　---------------------------------------------------------------------------*/
let remove = 0;

function radioDeselection(already, numeric) {
    if(remove === numeric) {
        already.checked = false;
        remove = 0;
    } else {
        remove = numeric;
    }
}