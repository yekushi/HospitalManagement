// content

// 电击科室
$('#ks').click(function () {
    alert('1');
    $('.img_c').load('footer.html');
});

// 图片变化
$(function () {
    var curIndex = 0;
    //时间间隔(单位毫秒) ,每秒钟显示一张
    var timeInterval = 3000;
    var arr = new Array();
    arr[0] = "../static/images/service.jpg"
    arr[1] = "../static/images/equip.jpg"
    arr[2] = "../static/images/operation.jpg"
    function changeImg() {
        if (curIndex == arr.length-1){
            curIndex = 0;
        }
        else{
            curIndex += 1;
        }
        $('#image').attr('src',arr[curIndex]);
        // 此处arr[curIndex]不需要加引号#}
    }
    setInterval(changeImg,timeInterval);
 })

// 图片轮播
// window.onload = function () {
//     var tupd = document.getElementById('.home');
//     tupul = document.getElementById('#tup');
//     tupul.innerHTML += tupul.innerHTML;
//     // 循环
//     tupli = document.getElementById('#tup li');
//     tupul.style.width = tupli.length * 1263 + 'px';
//     var speed = 2;
//     //每一百毫米偏移量，速度
//     function move() {
//         if (tupul.offsetLeft < -(tupul.offsetWidth/2))
//         {
//             alert('3');
//             tupul.style.left = -50 + 'px';//重新初始化，原本为多少就设为多少
//         }
//         if (tupul.offsetLeft > -50){
//             //图一移出边框时
//             alert('4');
//             tupul.style.left =- (tupul.offsetWidth/2) + 'px';
//         }
//         tupul.style.left = tupul.offsetLeft + speed + 'px';
//         alert('2');
//     }
//     setInterval(move,100);
//     //定时器
// }

// home导航栏

// 点击出诊时间
$('.r_content').load('time.html');
$('#l_time').click(function () {
    $('.r_content').load('time.html');
})
// 点击健康知识
$('#l_knowledge').click(function () {
    $('.r_content').load('healthy.html');
    $('.right').css('height','4900px');
})