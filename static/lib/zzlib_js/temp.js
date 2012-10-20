/**
 * User: zwm
 * Date: 12-10-20
 * Time: 上午2:28
 * 用于保存为整理的，或是尚处于测试的功能模块
 */

function array_unique(a,strict){
    /**
     * 接受一个数组，去掉重复项，返回一个不含重复项的数组
     * @param a 原始数组
     * @param strict ？？？？
     * @returns [] 不含重复项的数组
     */
    var o = {},
        arr = [],
        key;
    for(var i = 0; i < a.length; ++i){
        key = a[i];
        if(strict){
            if(typeof(a[i]) == 'number'){
                key = a[i]+'.number';
            }
            if(typeof(a[i]) == 'string'){
                key = a[i]+'.string';
            }
        }
        if(!o[key]){
            o[key] = true;
            arr.push(a[i]);
        }
    }
    return arr;
}

function coord_to_mapbar(x,y){
    /**
     * 将真实地理坐标加密为Mapbar经纬度坐标
     * @param x 经度值
     * @param y 维度值
     * @returns [x,y]
     */
    x = parseFloat(x)*100000%36000000;
    y = parseFloat(y)*100000%36000000;

    _X = intval(((Math.cos(y/100000))*(x/18000))+((Math.sin(x/100000))*(y/9000))+x);
    _Y = intval(((Math.sin(y/100000))*(x/18000))+((Math.cos(x/100000))*(y/9000))+y);

    return [_X/100000.0,_Y/100000.0];
}

function mapbar_to_coord(x,y){
    /**
     * 将Mapbar经纬坐标解密为真实地理坐标
     * @param x 经度值
     * @param y 维度值
     * @returns [x,y]
     */
    x = parseFloat(x)*100000%36000000;
    y = parseFloat(y)*100000%36000000;

    x1 = parseInt(-(((Math.cos(y/100000))*(x/18000))+((Math.sin(x/100000))*(y/9000)))+x);
    y1 = parseInt(-(((Math.sin(y/100000))*(x/18000))+((Math.cos(x/100000))*(y/9000)))+y);

    x2 = parseInt(-(((Math.cos(y1/100000))*(x1/18000))+((Math.sin(x1/100000))*(y1/9000)))+x+((x>0)?1:-1));
    y2 = parseInt(-(((Math.sin(y1/100000))*(x1/18000))+((Math.cos(x1/100000))*(y1/9000)))+y+((y>0)?1:-1));

    return [x2/100000.0,y2/100000.0];
}

function dianping_to_mapbar(C) {
    /**
     * 将点评网字符串的POI解码为mapbar的坐标
     * @param C 待转换的POI字符串，在商户页面可以找到，类似于：HHDFJGZVVIHIJG
     * @returns obj = {lat, lgn} 返回一个对象，包含lat, lng两个属性
     */
    var digi=16;
    var add= 10;
    var plus=7;
    var cha=36;
    var I = -1;
    var H = 0;
    var B = "";
    var J = C.length;
    var G = C.charCodeAt(J - 1);
    C = C.substring(0, J - 1);
    J--;
    for (var E = 0; E < J; E++) {
        var D = parseInt(C.charAt(E), cha) - add;
        if (D >= add) {
            D = D - plus
        }
        B += (D).toString(cha);
        if (D > H) {
            I = E;
            H = D
        }
    }
    var A = parseInt(B.substring(0, I), digi);
    var F = parseInt(B.substring(I + 1), digi);
    var L = (A + F - parseInt(G)) / 2;
    var K = (F - L) / 100000;
    L /= 100000;
    return {
        lat: K,
        lng: L
    }
}