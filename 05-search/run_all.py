# simple script to run the examples from the book for this chapter
# 
# 
#
import os 
import searchengine

fn = 'searchindex1.db'
if( False ): os.unlink(fn) # execute if we want to "recrawl" the Perl web pages 

crawler = searchengine.crawler(fn)
crawler.createindextables()

# crawl some pages: 
# pagelist=['https://en.wikipedia.org/wiki/Python_(programming_language)']
pagelist=['http://www.pythonscraping.com']

# pagelist=['http://victoriacollege.edu/']
crawler.crawl(pagelist)

# pagelist=['http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html']
# crawler.crawl(pagelist)

[row for row in crawler.con.execute('select rowid from wordlocation where wordid=1')] 

e = searchengine.searcher(fn)
# e.getmatchrows('functional programming')
e.getmatchrows('scraping')

# create the needed tables for the page rank algorithm:
crawler.calculatepagerank()
# before adding in the page rank algorithm into the weights that form the scoring function 
e.query('scraping') 

cur = crawler.con.execute('select * from pagerank order by score desc')
for i in range(3): print cur.next()
e.geturlname(21)

# after adding in the page rank algorithm into the weights that form the scoring function
reload(searchengine)
e = searchengine.searcher(fn)
e.query('scraping') 

# after adding in the linktextscore algorithm into the weights that form the scoring function 
reload(searchengine)
e = searchengine.searcher(fn)
e.query('scraping') 


# starting the neural network click learning:
#
# import nn
# mynet = nn.searchnet('nn.db')
# mynet.maketables()

# wWorld,wRiver,wBank = 101,102,103
# uWorldBank,uRiver,uEarth = 201,202,203
# mynet.generatehiddennode( [wWorld,wBank], [uWorldBank,uRiver,uEarth])

# for c in mynet.con.execute('select * from hiddenurl' ): print c

# mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])
# mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
# mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])

# allurls = [ uWorldBank, uRiver, uEarth ]
# for i in range(30):
#     mynet.trainquery([wWorld,wBank],allurls,uWorldBank)
#     mynet.trainquery([wRiver,wBank],allurls,uRiver)
#     mynet.trainquery([wWorld],allurls,uEarth)

# mynet.getresult([wWorld,wBank],allurls)
# mynet.getresult([wRiver,wBank],allurls)
# mynet.getresult([wBank],allurls)





