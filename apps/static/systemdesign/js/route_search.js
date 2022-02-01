function route_search_init() {
    const route_proposal = JSON.parse(JSON.stringify(route));
    let row_length = route_proposal.max_row           //内周最大(door_way_x_position)   8
    let column_length = route_proposal.max_column         //内周最大(door_way_y_position)   9
    let door_way_x_position = route_proposal.door_way_list[0]       //出入口(door_way_x_position)        23
    let door_way_y_position = route_proposal.door_way_list[1]       //出入口(door_way_y_position)        0
    console.log('door_way_list' + route["door_way_list"])     //出入口
    let image_height = 13;
    let image_width = 13;

//テーブル定義
    let table = document.createElement('table');
    table.id = 'table';
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

//テーブル作成
    for (let i = 0; i < row_length; i++) {
        let row = document.createElement('tr');
        for (let j = 0; j < column_length; j++) {
            let heading = document.createElement('td');
            row.appendChild(heading);
        }
        thead.appendChild(row);
    }

    table.appendChild(thead);
    table.appendChild(tbody);


//出入口設定
    const im = document.createElement("img");
    im.height = image_height;
    im.width = image_width;
    if (route_proposal.all_move_list[0].step_move_list[0].string === "上") {
        im.style.transform = "rotate(-90deg)";
    } else if (route_proposal.all_move_list[1].step_move_list[0].string === "下") {
        im.style.transform = "rotate(90deg)";
    } else if (route_proposal.all_move_list[1].step_move_list[0].string === "右") {
    } else if (route_proposal.all_move_list[1].step_move_list[0].string === "左") {
        im.style.transform = "rotate(180deg)";
    }
    im.src = image2;
    table.rows[door_way_y_position].cells[door_way_x_position].appendChild(im);

//ルート表示
    for(const step_move_list of route_proposal.all_move_list) {
        for (const move of step_move_list.step_move_list) {
            const img = document.createElement("img");
            img.height = image_height;
            img.width = image_width;
            const y = move.row_position;
            const x = move.column_position;
            if (move.plant) {
                if (move.string === "上") {
                    img.style.transform = "rotate(180deg)";
                } else if (move.string === "右") {
                    img.style.transform = "rotate(-90deg)";
                } else if (move.string === "左") {
                    img.style.transform = "rotate(90deg)";
                }
                img.src = image;
                //plantがfalseの時(植えない時)
            } else {
                if (move.string === "上") {
                } else if (move.string === "下") {
                    img.style.transform = "rotate(180deg)";
                } else if (move.string === "右") {
                    img.style.transform = "rotate(90deg)";
                } else if (move.string === "左") {
                    img.style.transform = "rotate(-90deg)";
                }
                img.src = image1;
            }
            table.rows[y].cells[x].appendChild(img);
        }
    }

//bodyに作成したtableを追加
    document.getElementById('route').appendChild(table);
}
//背景設定
// url = "../images/kakouine.png";
// document.body.background = "../images/kakouine.png";

// $('#body').css({
//     backgroundImage: 'url("images/kakouine.png")'
// });