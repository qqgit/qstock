import itertools
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.optimizer import server


def parameters_generator():
    instrument = ["dia"]
    entrySMA = list(range(150, 155))
    exitSMA = list(range(5, 6))
    rsiPeriod = list(range(2, 5))
    overBoughtThreshold = list(range(88, 92))
    overSoldThreshold = list(range(16, 20))
    return itertools.product(instrument, entrySMA, exitSMA, rsiPeriod, overBoughtThreshold, overSoldThreshold)

# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    # Load the feed from the CSV files.
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("dia", "dia-2009.csv")
    feed.addBarsFromCSV("dia", "dia-2010.csv")
    feed.addBarsFromCSV("dia", "dia-2011.csv")

    # Run the server.
    server.serve(feed, parameters_generator(), "localhost", 6000)