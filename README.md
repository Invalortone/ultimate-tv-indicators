# Ultimate TV Indicators

![Python Version](https://img.shields.io/badge/Python-v3.8.0+-blue)
![Author](https://camo.githubusercontent.com/71e71561f012ff5bf69138d546adc1b1551d0045dd325c96c9490e2a4358eacd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f417574686f722d496e76616c6f72746f6e653f6c696e6b3d68747470732533412532462532466769746875622e636f6d253246696e76616c6f72746f6e65)
![Project Version](https://img.shields.io/badge/Newest_Version-v1.0.0-red)

## Description

Ultimate TV Indicators is a Python package that provides the conversion of popular indicators from TradingView to Python. This package includes over 15 indicators commonly used in trading, making it easier for traders to analyze market data and make informed decisions.

## Installation

You can install Ultimate TV Indicators using pip:

```bash
pip install ultimate-tv-indicators
```

## Usage

Once installed, you can import the desired indicators into your Python code and use them as follows:

```python
from ultimate_tv_indicators import <indicator_name>

data = <indicator_name>(x, y, z) # Usually takes a list as input as the source/bars.

print(data) # Returns a list or a tuple of lists depending on the indicator.

# Use the indicator value in your trading strategy
...
```

Replace `<indicator_name>` with the name of the desired indicator. For example, if you want to use the Moving Average indicator:

```python
from ultimate_tv_indicators import MovingAverage

# List of close prices.
close_bars = [42.65, 27.29, 28.30, 20.93, 43.22, 53.47, 50.56, 57.2, 61.78, 65.234, 80.99]

# Returns the simple moving average of the close prices with a length of 4 and containing null values.
ma = sma(source=close_bars, length=4, has_null=true)

# Prints the moving average list.
print(ma)

# Use the moving average value in your trading strategy
...
```

## List of Indicators

The package includes the following indicators:

- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Running Moving Average (RMA)
- Relative Strength Index (RSI)
- True Range (TR)
- Average True Range (ATR)
- Standard Deviation (STDEV)
- Traders Dynamic Index by GoldMinds (TDIGM)
- Kaufman's Adaptive Moving Average (KAMA)
- WaveTrend by LazyBear (WTLB)
- Double WaveTrend by Mynicknameislion
- Mayer Multiple by Jacknyc
- Baseline from the Ichimoku Cloud
- Trailing Sharpe Ratio by Rashad
- Spring with Tanning Lines by Iceberg
- Gaussian Channel by DonovanWall (GC_DW)
- CT Reverse MACD Cross by The_Caretaker (RMACD)
- Directional Movement Index indicator by Tradingview (DMI & ADX)

Each indicator has its own unique parameters and additional options for customization.


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue on the GitHub repository
<p align = "center"><strong><i>
✦•······················•✦•······················•✦ <br>
May you reach the stars. <br>
✦•······················•✦•······················•✦ <br>
</i></strong></p>
