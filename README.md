# dorahackAITradeSignals
Blockchain AI Trade Signals for Crypto

Team:
Ganesh APP
Tania Akinini

What is DorAi?
It is an AI Crypto Trade Signal Bot.

Why do we need it?
Crypto trading is volatile. It is still hugely affected by sentiments. Sentiments are swayed by news. Before a news gets popular, there are signals.

But Signals are difficult to track as there is no single source which aggregates them. There are bots, but they use selected credible source such as Yahoo News, CNN.

By the team the information is available in Yahoo or CNN, it is already too late.

There are Blockchain projects like Cindicator, which takes the crowd wisdom, but it doesn't have AI and always needs people.

People get data, make decisions and then input the result into cindicator. But a better way is to gather the data source and train the AI to make the prediction.

How does DorAi work?

First Part:
Information hunters, hunt for information (it could be a website, blog or tweet). They enter the URL in the blockchain. They stake some DorAi coins to represent confidence.

They also input their opinion whether the information in the URL is positive, negative or neutral.

The Smart Contract holds the DorAi tokens in escrow and waits for 4 days.

Second Part:
A large amount of historical data is scrapped from CoinMarketCap and CrytoCal (which lists all the events). ML sentiment is trained on this data to cluster the events/headlines and their effect on market price (in 1 day, 2 day, 3 day and 4 day interval).

The Information Hunter's URLs are the fed and the tweets/headers of the articles from the website are scrapped. The ML then uses the trained data to predict the effect on price (positive/negative/neutral) and magnitude.

4 days later the prices are checked. If the ML got it wrong, it checks what the Information Hunter's opinion was. And corrects itself.

At the end of 4 days, the smart contract self executes and based on the relevance of the url and the right opinion of the user, returns the escrow coin and pays BTC for their contribution.

Third Part:
Investors go to DorAi service, and seek information. A summarized buy/sell/hold prediction is given to them by the AI. They pay a price for the service, which is then shared with the information hunter.

Over a period of time, with more high quality URLs submitted, the AI is able to accurately predict whether the signal is good or bad (training from data provided by Info Hunters).

Current status:
A simplified JS blockchain is made to show how Signal hunters can put their url on the blockchain. A proper implementation on Ethereum or NEO will be made.

Data scrapping of Coinmarket Cap and CryptoCal is done. The training is yet to be done. Current logic uses TextBlob sentiment analysis.

URL scrapping, tweet scrapping is done. TextBlob uses this data to calculate the sentiment and weights and apply it to the prediction.

Basic UI for investor to get signal summary is done. A facebook chat bot to auto push signals can be implemented later.

Smart Contract to execute after 4 days is to be made.





