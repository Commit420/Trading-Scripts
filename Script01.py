//@version=5
indicator("Moving Average Crossover Strategy", shorttitle="MA Crossover", overlay=true)

// Input für die gleitenden Durchschnitte
fastLength = input.int(9, title="Fast MA Length", minval=1)
slowLength = input.int(21, title="Slow MA Length", minval=1)

// Berechnung der gleitenden Durchschnitte
fastMA = ta.sma(close, fastLength)
slowMA = ta.sma(close, slowLength)

// Plot der gleitenden Durchschnitte
plot(fastMA, color=color.blue, title="Fast MA")
plot(slowMA, color=color.red, title="Slow MA")

// Kauf- und Verkaufssignale
longCondition = ta.crossover(fastMA, slowMA)
shortCondition = ta.crossunder(fastMA, slowMA)

// Anzeige der Signale auf dem Chart
plotshape(longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(shortCondition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")

// Strategiebedingungen
if (longCondition)
    label.new(bar_index, low, "Buy", style=label.style_label_up, color=color.green, textcolor=color.white)

if (shortCondition)
    label.new(bar_index, high, "Sell", style=label.style_label_down, color=color.red, textcolor=color.white)
