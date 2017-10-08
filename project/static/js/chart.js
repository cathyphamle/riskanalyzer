var request = new XMLHttpRequest();
request.open("GET", '../static/js/chartdata1.json', false);
request.send(null);
var data1 = JSON.parse(request.responseText);
var chart1 = new Chartist.Line('#chart1', data1, {
    showPoint: false,
    axisX: {
        showGrid: false,
        showLabel: false
    },
    fullWidth: true
});

chart1.on('draw', function(data) {
    if (data.type === 'line' || data.type === 'area') {
        data.element.animate({
            d: {
                begin: 2000 * data.index,
                dur: 2000,
                from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                to: data.path.clone().stringify(),
                easing: Chartist.Svg.Easing.easeOutQuint
            }
        });
    }
});

var request = new XMLHttpRequest();
request.open("GET", '../static/js/chartdata2.json', false);
request.send(null);
var data2 = JSON.parse(request.responseText);
var chart2 = new Chartist.Line('#chart2', data2, {
    showPoint: false,
    axisX: {
        showGrid: false,
        showLabel: false
    },
    fullWidth: true
});

chart2.on('draw', function(data) {
    if (data.type === 'line' || data.type === 'area') {
        data.element.animate({
            d: {
                begin: 2000 * data.index,
                dur: 2000,
                from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                to: data.path.clone().stringify(),
                easing: Chartist.Svg.Easing.easeOutQuint
            }
        });
    }
});


var request = new XMLHttpRequest();
request.open("GET", '../static/js/chartdata3.json', false);
request.send(null);
var data3 = JSON.parse(request.responseText);
var chart3 = new Chartist.Line('#chart3', data3, {
    showPoint: false,
    axisX: {
        showGrid: false,
        showLabel: false
    },
    fullWidth: true
});

chart3.on('draw', function(data) {
    if (data.type === 'line' || data.type === 'area') {
        data.element.animate({
            d: {
                begin: 2000 * data.index,
                dur: 2000,
                from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                to: data.path.clone().stringify(),
                easing: Chartist.Svg.Easing.easeOutQuint
            }
        });
    }
});