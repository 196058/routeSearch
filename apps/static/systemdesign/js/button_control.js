/*２回押しでラジオボタンの選択解除
　---------------------------------------------------------------------------*/
var remove = 0;

function radioDeselection(already, numeric) {
    if(remove == numeric) {
        already.checked = false;
        remove = 0;
    } else {
        remove = numeric;
    }
}