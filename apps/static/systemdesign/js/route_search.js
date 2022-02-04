let height = route["max_row"]           //内周最大(x)   8
let width = route["max_column"]         //内周最大(y)   9
let x = route["door_way_list"][1]       //出入口(x)        23
let y = route["door_way_list"][0]       //出入口(y)        0
console.log('door_way_list' + route["door_way_list"])     //出入口
let image_height = 13;
let image_width = 13;

//テーブル定義
let table = document.createElement('table');
table.id = 'table';
let thead = document.createElement('thead');
let tbody = document.createElement('tbody');
table.appendChild(thead);
table.appendChild(tbody);

//テーブル作成
for (let i=0; i<height; i++){
    let row = document.createElement('tr');
    for(let j=0; j<width+1; j++) {
        let heading = document.createElement('td');
        if(j === width) {
            // テスト時に何行目かを見るため
            heading.innerHTML = i;
        }else {
            heading.innerHTML = "　";
        }
        row.appendChild(heading);
    }
    thead.appendChild(row);
}

//出入口設定
const im = document.createElement("img");
im.height = image_height;
im.width = image_width;
if (route["all_move_list"][0]["step_move_list"][0]["string"] === "上") {
        im.style.transform = "rotate(-90deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "下") {
    im.style.transform = "rotate(90deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "右") {
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "左") {
    im.style.transform = "rotate(180deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "上左") {
    im.style.transform = "rotate(-135deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "上右") {
    im.style.transform = "rotate(-45deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "下左") {
    im.style.transform = "rotate(135deg)";
} else if(route["all_move_list"][1]["step_move_list"][0]["string"] === "下右") {
    im.style.transform = "rotate(45deg)";
}
im.src = image2;
table.rows[ x ].cells[ y ].appendChild(im);
//最初の進行方向への設定
// x = x + route["all_move_list"][0]["step_move_list"][0]["vector"][0]
// y = y + route["all_move_list"][0]["step_move_list"][0]["vector"][1]

//ルート表示
for(let i=0; i<route["all_move_list"].length; i++) {
    for (let j=0; j<route["all_move_list"][i]["step_move_list"].length; j++) {
        const img = document.createElement("img");
        img.height = image_height;
        img.width = image_width;
        //plantがtrueの時(植える時)
        if(route["all_move_list"][i]["step_move_list"][j]["plant"]) {
            if (route["all_move_list"][i]["step_move_list"][j]["string"] === "上") {
                img.style.transform = "rotate(180deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "右") {
                img.style.transform = "rotate(-90deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "左") {
                img.style.transform = "rotate(90deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "上左") {
                img.style.transform = "rotate(135deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "上右") {
                img.style.transform = "rotate(-135deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "下左") {
                img.style.transform = "rotate(45deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "下右") {
                img.style.transform = "rotate(-45deg)";
            }
            img.src = image;
            //plantがfalseの時(植えない時)
        }else{
            if (route["all_move_list"][i]["step_move_list"][j]["string"] === "上") {
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "下") {
                img.style.transform = "rotate(180deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "右") {
                img.style.transform = "rotate(90deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "左") {
                img.style.transform = "rotate(-90deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "上左") {
                img.style.transform = "rotate(-45deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "上右") {
                img.style.transform = "rotate(45deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "下左") {
                img.style.transform = "rotate(-135deg)";
            } else if(route["all_move_list"][i]["step_move_list"][j]["string"] === "下右") {
                img.style.transform = "rotate(135deg)";
            }
            img.src = image1;
        }
        table.rows[ x ].cells[ y ].appendChild(img);
        x = x + route["all_move_list"][i]["step_move_list"][j]["vector"][0]
        y = y + route["all_move_list"][i]["step_move_list"][j]["vector"][1]
    }
}
//bodyに作成したtableを追加
document.getElementById('route').appendChild(table);

//背景設定
// url = "../images/kakouine.png";
// document.body.background = "../images/kakouine.png";

// $('#body').css({
//     backgroundImage: 'url("images/kakouine.png")'
// });