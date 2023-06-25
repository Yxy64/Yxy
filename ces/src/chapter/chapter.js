let chapter = (text, companyName) => {
    let canvas = document.getElementById("canvas");
    let context = canvas.getContext("2d");
  
    //let text = "XXX专用章";
    //let companyName = "XXX科技股份有限公司";
  
    // 绘制印章边框
    let width = canvas.width / 2;
    let height = canvas.height / 2;
    context.lineWidth = 5;
    context.strokeStyle = "#f00";
    context.beginPath();
    context.arc(width, height, 90, 0, Math.PI * 2); //宽、高、半径
    context.stroke();
  
    //画五角星
    create5star(context, width, height, 25, "#f00", 0);
  
    // 绘制印章名称
    context.font = "20px 宋体";
    context.textBaseline = "middle"; //设置文本的垂直对齐方式
    context.textAlign = "center"; //设置文本的水平对对齐方式
    context.lineWidth = 1;
    context.strokeStyle = "#f00";
    context.strokeText(text, width, height + 60);
  
    // 绘制印章单位
    context.translate(width, height); // 平移到此位置,
    context.font = "23px 宋体";
    let count = companyName.length; // 字数
    let angle = (4 * Math.PI) / (3 * (count - 1)); // 字间角度
    let chars = companyName.split("");
    let c;
    for (let i = 0; i < count; i++) {
      c = chars[i]; // 需要绘制的字符
      if (i == 0) {
        context.rotate((5 * Math.PI) / 6);
      } else {
        context.rotate(angle);
      }
  
      context.save();
      context.translate(70, 0); // 平移到此位置,此时字和x轴垂直，公司名称和最外圈的距离
      context.rotate(Math.PI / 2); // 旋转90度,让字平行于x轴
      context.strokeText(c, 0, 0); // 此点为字的中心点
      context.restore();
    }
  
    //绘制五角星
    function create5star(context, sx, sy, radius, color, rotato) {
      context.save();
      context.fillStyle = color;
      context.translate(sx, sy); //移动坐标原点
      context.rotate(Math.PI + rotato); //旋转
      context.beginPath(); //创建路径
      // let x = Math.sin(0);
      // let y = Math.cos(0);
      let dig = (Math.PI / 5) * 4;
      for (let i = 0; i < 5; i++) {
        //画五角星的五条边
        let x = Math.sin(i * dig);
        let y = Math.cos(i * dig);
        context.lineTo(x * radius, y * radius);
      }
      context.closePath();
      context.stroke();
      context.fill();
      context.restore();
    }
  };
  
  export default chapter;
  
  
  