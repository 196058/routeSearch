function clickBtn1(){
    const cgroup = document.getElementsByName("group");

    if(cgroup[0].checked){
        if(cgroup[1].checked) {
            cgroup[1].checked = false;
        }
    }
}

function clickBtn2(){
    const cgroup = document.getElementsByName("group");

    if (cgroup[1].checked){
        if(cgroup[0].checked) {
            cgroup[0].checked = false;
        }
    }
}