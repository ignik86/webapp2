am4core.useTheme(am4themes_animated);

var chart = am4core.create("chartdiv", am4charts.RadarChart);

chart.data = [
    {
        category: "One",
        value1: 8,
        value2: 2,
        value3: 4,
        value4: 3
    },
    {
        category: "Two",
        value1: 11,
        value2: 4,
        value3: 2,
        value4: 4
    },
    {
        category: "Three",
        value1: 7,
        value2: 6,
        value3: 6,
        value4: 2
    },
    {
        category: "Four",
        value1: 13,
        value2: 8,
        value3: 3,
        value4: 2
    },
    {
        category: "Five",
        value1: 12,
        value2: 10,
        value3: 5,
        value4: 1
    },
    {
        category: "Six",
        value1: 15,
        value2: 12,
        value3: 4,
        value4: 4
    },
    {
        category: "Seven",
        value1: 9,
        value2: 14,
        value3: 6,
        value4: 2
    },
    {
        category: "Eight",
        value1: 6,
        value2: 16,
        value3: 5,
        value4: 1
    }
];

chart.padding(20, 20, 20, 20);
chart.colors.step = 4;

var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "category";
categoryAxis.renderer.labels.template.location = 0.5;
categoryAxis.renderer.labels.template.horizontalCenter = "right";
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.renderer.tooltipLocation = 0.5;
categoryAxis.renderer.grid.template.strokeOpacity = 0.07;
categoryAxis.interactionsEnabled = false;

var valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
valueAxis.tooltip.disabled = true;
valueAxis.renderer.labels.template.horizontalCenter = "left";
valueAxis.min = 0;
valueAxis.max = 60;
valueAxis.strictMinMax = true;
valueAxis.renderer.maxLabelPosition = 0.99;
valueAxis.renderer.minGridDistance = 10;
valueAxis.renderer.grid.template.strokeOpacity = 0.07;
valueAxis.interactionsEnabled = false;

var series1 = chart.series.push(new am4charts.RadarColumnSeries());
series1.columns.template.width = am4core.percent(80);
series1.columns.template.tooltipText = "{name}: {valueX.value}";
series1.name = "Series 1";
series1.dataFields.categoryY = "category";
series1.dataFields.valueX = "value2";
series1.stacked = true;
alue2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2";
sere2