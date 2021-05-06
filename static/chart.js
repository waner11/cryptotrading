var chart = LightweightCharts.createChart(document.getElementById("chart"), {
  width: 600,
  height: 300,
  layout: {
    backgroundColor: "#808080 ",
    textColor: "#000",
  },
  grid: {
    vertLines: {
      color: "rgba(197, 203, 206, 0.5)",
    },
    horzLines: {
      color: "rgba(197, 203, 206, 0.5)",
    },
  },
  crosshair: {
    mode: LightweightCharts.CrosshairMode.Normal,
  },
  rightPriceScale: {
    borderColor: "rgba(197, 203, 206, 0.8)",
  },
  timeScale: {
    borderColor: "rgba(197, 203, 206, 0.8)",
  },
});

var candleSeries = chart.addCandlestickSeries({
  upColor: "#00ff00",
  downColor: "#ff0000",
  borderDownColor: "#ff0000",
  borderUpColor: "#00ff00",
  wickDownColor: "#ff0000",
  wickUpColor: "#00ff00",
});

fetch('http://127.0.0.1:5000/history')
      .then((r) => r.json())
      .then((response) => {
        candleSeries.setData(response);

        //console.log(response)
      })

var socket = new WebSocket("wss://stream.binance.com:9443/ws/maticusdt@kline_5m");

socket.onmessage = function (e) {
  console.log(e.data);

  var message = JSON.parse(e.data);

  var candlestick = message.k;

  candleSeries.update({
    time: candlestick.t,
    open: candlestick.o,
    high: candlestick.h,
    low: candlestick.l,
    close: candlestick.c
  });
};
